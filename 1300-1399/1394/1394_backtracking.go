package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
	"strconv"
	"strings"
	"time"
)

// Three exact searches with growing time slices and perturbed orders, tried in
// turns until one places all ships: B (rows one at a time), C (B over the
// rare lengths only), D (C with residues modulo K checked exactly).
const (
	maxShips   = 100
	maxRows    = 10
	maxLen     = 100
	maxSum     = 10001 // fewer than 100 ships of at most 100
	timeLimit  = 900 * time.Millisecond
	clockEvery = 256 // nodes between looks at the clock
	word       = 64
	words      = (maxSum + word - 1) / word
)

type hash = uint64

var (
	n, m       int
	ships      [maxShips]int
	rowLen     [maxRows]int
	v, shipID  [maxShips]int // current ship order: lengths and input positions
	rowID      [maxRows]int  // the input row of search row b
	placed     [maxShips]int // the search row of ship i
	nodes      int64
	attemptEnd time.Duration // the time when the current attempt stops
	aborted    bool
	started    time.Time
	rngState   uint32 = rngSeed
)

const xsA, xsB, xsC = 13, 17, 5 // xorshift32 shifts

// the seed of the xorshift32 generator, the usual one from Marsaglia's paper
const rngSeed = 2463534242

func rnd() uint32 {
	rngState ^= rngState << xsA
	rngState ^= rngState >> xsB
	rngState ^= rngState << xsC
	return rngState
}

func rnd64() hash {
	high := hash(rnd())
	return high<<(word/2) | hash(rnd())
}

// splitmix64 finalizer
const (
	golden              = 0x9E3779B97F4A7C15
	mix1                = 0xBF58476D1CE4E5B9
	mix2                = 0x94D049BB133111EB
	mixS1, mixS2, mixS3 = 30, 27, 31
)

func mix(x hash) hash {
	x += golden
	x = (x ^ (x >> mixS1)) * mix1
	x = (x ^ (x >> mixS2)) * mix2
	return x ^ (x >> mixS3)
}

func elapsed() time.Duration { return time.Since(started) }

func tick() bool {
	nodes++
	if nodes%clockEvery == 0 && elapsed() > attemptEnd {
		aborted = true
		return false
	}
	return true
}

// bits is a bitset of run-time width: a row search needs sums up to its longest row.
type bits []hash

func (b bits) get(x int) bool { return (b[x/word]>>uint(x%word))&1 != 0 }

func (b bits) one() {
	for i := range b {
		b[i] = 0
	}
	b[0] = 1
}

// b = s | s << sh over the width of b; s may be b
func (b bits) shiftOr(s bits, sh int) {
	ws, bs := sh/word, uint(sh%word)
	for i := len(b) - 1; i >= 0; i-- {
		x := s[i]
		if j := i - ws; j >= 0 {
			x |= s[j] << bs
			if bs != 0 && j > 0 {
				x |= s[j-1] >> (word - bs)
			}
		}
		b[i] = x
	}
}

func contains(list []int, x int) bool {
	for _, y := range list {
		if y == x {
			return true
		}
	}
	return false
}

// Failed states of the row searches, by a hash of the unused ships and the
// open rows; they do not depend on the order, so they survive restarts.
const (
	memoBits = 20
	memoSize = 1 << memoBits
	probes   = 8
)

var (
	zobrist [maxLen + 1]hash // a random key per ship length
	memo    = make([]hash, memoSize)
)

func known(k hash) bool {
	p := int(k >> (word - memoBits))
	for t := 0; t < probes; t++ {
		e := memo[(p+t)%memoSize]
		if e == k {
			return true
		}
		if e == 0 {
			return false
		}
	}
	return false
}

func remember(k hash) {
	p := int(k >> (word - memoBits))
	for t := 0; t < probes; t++ {
		if e := &memo[(p+t)%memoSize]; *e == 0 || *e == k {
			*e = k
			return
		}
	}
	memo[(p+int(k%probes))%memoSize] = k
}

// For strategy D: ships not divisible by mod fall into classes by residue.
// Rows b.. can only be completed if the class counts left split among them so
// that each row gets its length modulo mod: a DP over (row, counts), cached.
const (
	checkBits   = 21
	checkSize   = 1 << checkBits
	checkProbes = 4
	maxCodes    = 1e17 // the count vectors must fit in 64 bits
	queryBudget = 100000
	maxOver     = 5  // queries over budget before the check gives up
	rowRadix    = 16 // more than the rows
	slotShift   = 8
	salt        = 0x1234567
)

var checked = make([]hash, checkSize) // (key with the low bit cleared) | feasible

type residues struct {
	mod, classes   int
	residue, count [maxLen]int // classes by count, the largest last
	radix          [maxLen]hash
	target         [maxRows]int // row lengths modulo mod
	orderSalt      hash
	full           hash
	ops, budget    int64
	broken         bool // the current query is over budget: "feasible"
	overCount      int  // queries over budget in this attempt
}

func (z *residues) rotate(x hash, s int) hash {
	if s == 0 {
		return x
	}
	return ((x << uint(s)) | (x >> uint(z.mod-s))) & z.full
}

func (z *residues) overBudget() bool {
	z.ops++
	if z.ops > z.budget {
		z.broken = true
	}
	return z.broken
}

// Row b takes c of class j and of the classes after it (R: the counts left,
// r: the residue so far, reach[j]: residues the classes j.. give).
func (z *residues) split(b int, R *[maxLen]int, reach *[maxLen + 1]hash, code hash,
	j, r int, taken hash) bool {
	if z.overBudget() {
		return true
	}
	need := (z.target[b] - r + z.mod) % z.mod
	if (reach[j]>>uint(need))&1 == 0 {
		return false
	}
	if j == z.classes {
		return z.feasible(b+1, code-taken)
	}
	if j == z.classes-1 { // the last class: its count is fixed modulo mod
		for c := 0; c <= R[j] && c < z.mod; c++ {
			if c*z.residue[j]%z.mod != need {
				continue
			}
			for cc := c; cc <= R[j]; cc += z.mod {
				if z.overBudget() ||
					z.feasible(b+1, code-taken-hash(cc)*z.radix[j]) ||
					z.broken {
					return true
				}
			}
		}
		return false
	}
	for c := 0; c <= R[j]; c++ {
		next := (r + c*z.residue[j]) % z.mod
		if z.split(b, R, reach, code, j+1, next, taken+hash(c)*z.radix[j]) || z.broken {
			return true
		}
	}
	return false
}

func (z *residues) feasible(b int, code hash) bool {
	if z.broken {
		return true
	}
	var R [maxLen]int
	c := code
	for j := 0; j < z.classes; j++ {
		R[j] = int(c % hash(z.count[j]+1))
		c /= hash(z.count[j] + 1)
	}
	if b == m-1 {
		r := 0
		for j := 0; j < z.classes; j++ {
			r = (r + R[j]*z.residue[j]) % z.mod
		}
		return r == z.target[b]
	}
	key := mix(z.orderSalt^mix(code*rowRadix+hash(b))) &^ 1
	p := int(key >> (word - checkBits))
	for t := 0; t < checkProbes; t++ {
		if e := checked[(p+t)%checkSize]; e&^1 == key {
			return e&1 != 0
		}
	}
	var reach [maxLen + 1]hash
	reach[z.classes] = 1
	for j := z.classes - 1; j >= 0; j-- {
		for t := 0; t <= R[j] && t < z.mod; t++ {
			reach[j] |= z.rotate(reach[j+1], t*z.residue[j]%z.mod)
		}
		if R[j] < z.mod {
			z.ops += int64(R[j]) + 1
		} else {
			z.ops += int64(z.mod) + 1
		}
	}
	if z.ops > z.budget {
		z.broken = true
		return true
	}
	ok := z.split(b, &R, &reach, code, 0, 0, 0)
	if z.broken {
		return true
	}
	q := (p + int((key>>slotShift)%checkProbes)) % checkSize
	for t := 0; t < checkProbes; t++ {
		if checked[(p+t)%checkSize] == 0 {
			q = (p + t) % checkSize
			break
		}
	}
	checked[q] = key
	if ok {
		checked[q] |= 1
	}
	return ok
}

// the classes for modulus k; false if the count vectors do not fit in 64 bits
func (z *residues) init(k int) bool {
	var perResidue [maxLen]int
	for _, x := range ships[:n] {
		if x%k != 0 {
			perResidue[x%k]++
		}
	}
	z.mod, z.classes, z.full = k, 0, (1<<uint(k))-1
	type class struct{ count, residue int }
	var list []class
	for r := 1; r < k; r++ {
		if perResidue[r] > 0 {
			list = append(list, class{perResidue[r], r})
		}
	}
	sort.Slice(list, func(i, j int) bool {
		if list[i].count != list[j].count {
			return list[i].count < list[j].count
		}
		return list[i].residue < list[j].residue
	})
	total, s := 1.0, hash(1)
	for _, cl := range list {
		z.residue[z.classes] = cl.residue
		z.count[z.classes], z.radix[z.classes] = cl.count, s
		z.classes++
		total *= float64(cl.count + 1)
		if total > maxCodes {
			return false
		}
		s *= hash(cl.count + 1)
	}
	return true
}

func (z *residues) fullCode() hash {
	c := hash(0)
	for j := 0; j < z.classes; j++ {
		c += hash(z.count[j]) * z.radix[j]
	}
	return c
}

// a query from a search: limited effort, "feasible" when it runs out
func (z *residues) query(b int, code hash) bool {
	if z.overCount > maxOver || elapsed() > attemptEnd {
		return true
	}
	z.ops, z.broken = 0, false
	ok := z.feasible(b, code)
	if z.broken {
		z.overCount++
	}
	return ok
}

// a new attempt with these row lengths, in search order
func (z *residues) setRows(lens []int) {
	z.orderSalt = mix(salt + hash(z.mod))
	for b := 0; b < m; b++ {
		z.target[b] = lens[b] % z.mod
		z.orderSalt = mix(z.orderSalt ^ hash(lens[b]))
	}
	z.overCount, z.budget = 0, queryBudget
}

// Strategies B, C, D: rows are filled one at a time; inside a row each ship
// is taken or skipped (equal ships skipped together). Ships kept..n-1 are
// deferred: a row only needs a remainder they make, and sub places them last.
const (
	maxChecks     = 13
	rowSalt       = 0x51ED27
	remainderSalt = 0xC0FFEE
	tagSalt       = 0x7A6
)

type rowSearch struct {
	n, m, kept                    int
	v, where                      [maxShips]int
	len, remainder                [maxRows]int
	used                          [maxShips]bool
	tag, shipsHash, remainderHash hash // tag: which lengths are deferred (0: none)
	sums                          [maxRows][maxShips + 1]bits
	deferredSums                  bits
	sub                           *rowSearch
	checks                        []*residues // valid: closed rows are complete modulo each

	// the class of ship i in check t, -1 if divisible
	cls [maxChecks][maxShips]int

	// mixed-radix codes of the unused class counts
	code [maxChecks]hash
}

func (s *rowSearch) take(pos int, sign hash) {
	for t, z := range s.checks {
		if s.cls[t][pos] >= 0 {
			s.code[t] += sign * z.radix[s.cls[t][pos]]
		}
	}
}

func (s *rowSearch) placeDeferred() bool {
	d := s.sub
	d.n, d.kept, d.m, d.checks = s.n-s.kept, s.n-s.kept, s.m, nil
	copy(d.v[:], s.v[s.kept:s.n])
	copy(d.len[:], s.remainder[:s.m])
	if !d.run(0) {
		return false
	}
	copy(s.where[s.kept:], d.where[:d.n])
	return true
}

func (s *rowSearch) fill(b, pos, r int) bool {
	if !tick() {
		return false
	}
	for pos < s.kept && s.used[pos] {
		pos++
	}
	if r == 0 || pos >= s.kept { // row b is done; the rest comes from deferred ships
		if r > 0 && (s.kept == s.n || !s.deferredSums.get(r)) {
			return false
		}
		s.remainder[b] = r
		if s.kept < s.n {
			s.remainderHash += mix(hash(r))
		}
		ok := s.open(b + 1)
		if s.kept < s.n {
			s.remainderHash -= mix(hash(r))
		}
		return ok
	}
	x := s.v[pos]
	if x <= r && s.sums[b][pos+1].get(r-x) {
		s.used[pos], s.where[pos] = true, b
		s.shipsHash -= zobrist[x]
		s.take(pos, ^hash(0))
		if s.fill(b, pos+1, r-x) {
			return true
		}
		s.used[pos] = false
		s.shipsHash += zobrist[x]
		s.take(pos, 1)
		if aborted {
			return false
		}
	}
	q := pos + 1 // skip ship x and all its copies
	for q < s.kept && s.v[q] == x {
		q++
	}
	return s.sums[b][q].get(r) && s.fill(b, q, r)
}

func (s *rowSearch) open(b int) bool {
	if b == s.m {
		return s.placeDeferred()
	}
	if b == s.m-1 { // the last row takes all the ships left
		sum := 0
		for i := 0; i < s.kept; i++ {
			if !s.used[i] {
				sum += s.v[i]
				s.where[i] = b
			}
		}
		if s.kept == s.n {
			return true
		}
		r := s.len[b] - sum
		if r < 0 || !s.deferredSums.get(r) {
			return false
		}
		s.remainder[b] = r
		return s.placeDeferred()
	}
	rowsHash := s.tag
	for c := b; c < s.m; c++ {
		rowsHash += mix(hash(s.len[c]) + rowSalt)
	}
	key := (mix(s.shipsHash^mix(rowsHash)) + mix(s.remainderHash^remainderSalt)) | 1
	if known(key) {
		return false
	}
	for t, z := range s.checks {
		if !z.query(b, s.code[t]) {
			remember(key)
			return false
		}
	}
	sums := s.sums[b][:]
	if s.kept == s.n {
		sums[s.kept].one()
	} else {
		copy(sums[s.kept], s.deferredSums)
	}
	for i := s.kept - 1; i >= 0; i-- {
		if s.used[i] {
			copy(sums[i], sums[i+1])
		} else {
			sums[i].shiftOr(sums[i+1], s.v[i])
		}
	}
	for c := b; c < s.m; c++ {
		if !sums[0].get(s.len[c]) {
			remember(key)
			return false
		}
	}
	ok := s.fill(b, 0, s.len[b])
	if !ok && !aborted {
		remember(key)
	}
	return ok
}

func (s *rowSearch) run(tag hash) bool {
	s.tag = tag
	longest := 0
	for _, l := range s.len[:s.m] {
		if l > longest {
			longest = l
		}
	}
	width := longest/word + 1
	for b := range s.sums {
		for i := range s.sums[b] {
			if cap(s.sums[b][i]) < width {
				s.sums[b][i] = make(bits, words)
			}
			s.sums[b][i] = s.sums[b][i][:width]
		}
	}
	if cap(s.deferredSums) < width {
		s.deferredSums = make(bits, words)
	}
	s.deferredSums = s.deferredSums[:width]
	s.shipsHash, s.remainderHash = 0, 0
	for t, z := range s.checks {
		s.code[t] = z.fullCode()
	}
	for i := 0; i < s.n; i++ {
		s.used[i] = false
	}
	for i := 0; i < s.kept; i++ {
		s.shipsHash += zobrist[s.v[i]]
	}
	if s.kept < s.n {
		s.deferredSums.one()
		for i := s.kept; i < s.n; i++ {
			s.deferredSums.shiftOr(s.deferredSums, s.v[i])
		}
	}
	return s.open(0)
}

var (
	mainSearch, subSearch rowSearch
	residuePool           [maxChecks]residues
)

func runRows(kept int, checks []*residues) bool {
	s := &mainSearch
	s.n, s.m, s.kept, s.sub, s.checks = n, m, kept, &subSearch, checks
	copy(s.v[:], v[:n])
	for b := 0; b < m; b++ {
		s.len[b] = rowLen[rowID[b]]
	}
	for t, z := range checks {
		var classOf [maxLen]int
		classOf[0] = -1
		for j := 0; j < z.classes; j++ {
			classOf[z.residue[j]] = j
		}
		for i := 0; i < n; i++ {
			s.cls[t][i] = classOf[v[i]%z.mod]
		}
		z.setRows(s.len[:m])
	}
	tag := hash(0)
	if kept < n {
		var rare [maxLen + 1]bool
		for i := 0; i < kept; i++ {
			rare[v[i]] = true
		}
		tag = tagSalt
		for x := 1; x <= maxLen; x++ {
			if rare[x] {
				tag = mix(tag ^ hash(x))
			}
		}
	}
	if !s.run(tag) {
		return false
	}
	copy(placed[:], s.where[:n])
	return true
}

const (
	modMin, modMax = 2, 50 // moduli for D
	smallModMax    = 6     // B also checks moduli up to this
	topMods        = 4
	scoreScale     = 100
	slots          = 5 // B, B with rows ascending, C, D, B again
	share          = 4 // a modulus must divide a quarter of the ships
	strategyB      = 0
	strategyC      = 1
	strategyD      = 2
	rareLevels     = 3    // C: "rare" means at most 1..3 copies
	keyScale       = 1000 // ship order keys
	maxNoise       = 30
	rareFirst      = 1000000000
	firstSlice     = 0.003 // seconds
	sliceGrowth    = 1.6
	maxGrowth      = 20
)

// B gets three slots of five: the hardest tests need its row-by-row search.
var slotStrategy = [slots]int{strategyB, strategyB, strategyC, strategyD, strategyB}

func main() {
	in := bufio.NewReader(os.Stdin)
	fmt.Fscan(in, &n, &m)
	for i := 0; i < n; i++ {
		fmt.Fscan(in, &ships[i])
	}
	for j := 0; j < m; j++ {
		fmt.Fscan(in, &rowLen[j])
	}
	started = time.Now()
	var copies [maxLen + 1]int
	for _, x := range ships[:n] {
		copies[x]++
	}
	for x := range zobrist {
		zobrist[x] = rnd64()
	}
	sane := true
	for _, l := range rowLen[:m] {
		sane = sane && l > 0 && l < maxSum
	}

	// moduli for D from two rankings: many multiples of a large k, and the
	// fewest non-multiples (say all ships even but one odd ship per row)
	type ranked struct{ score, k int }
	var byScore, byFew []ranked
	for k := modMin; k <= modMax; k++ {
		d := 0
		for _, x := range ships[:n] {
			if x%k == 0 {
				d++
			}
		}
		if d < n && d >= modMin && d >= n/share {
			byScore = append(byScore, ranked{-d * k, k})
			byFew = append(byFew, ranked{(n-d)*scoreScale - k, k})
		}
	}
	for _, list := range [][]ranked{byScore, byFew} {
		sort.Slice(list, func(i, j int) bool {
			if list[i].score != list[j].score {
				return list[i].score < list[j].score
			}
			return list[i].k < list[j].k
		})
	}
	var dMods []int
	for c := 0; c < topMods; c++ {
		for _, list := range [][]ranked{byScore, byFew} {
			if c < len(list) && !contains(dMods, list[c].k) {
				dMods = append(dMods, list[c].k)
			}
		}
	}
	// residue checks: D's moduli, plus small ones that B checks with them
	dChecks := make([]*residues, len(dMods))
	var bChecks []*residues
	mods := append([]int(nil), dMods...)
	for k := modMin; k <= smallModMax; k++ {
		if !contains(mods, k) {
			mods = append(mods, k)
		}
	}
	for c, k := range mods {
		z := &residuePool[len(bChecks)]
		ok := z.init(k) && z.classes > 0
		if c < len(dMods) && ok {
			dChecks[c] = z
		}
		if ok {
			bChecks = append(bChecks, z)
		}
	}

	key := make([]int64, n)
	order := make([]int, n)
	solved := false
	for attempt := 0; sane && !solved; attempt++ {
		slot, round := attempt%slots, attempt/slots
		strategy := slotStrategy[slot]
		rowsUp := slot == 1
		rareLevel := 1 + round%rareLevels
		ci, K := -1, 0
		if len(dMods) > 0 {
			ci = round % len(dMods)
			K = dMods[ci]
		}
		var rare [maxLen + 1]bool
		for x := 1; x <= maxLen; x++ {
			if strategy == strategyC {
				rare[x] = copies[x] <= rareLevel
			} else {
				rare[x] = strategy == strategyD && K != 0 && x%K != 0
			}
		}
		if strategy == strategyD && K == 0 {
			strategy = strategyB
		}
		kept := 0
		for _, x := range ships[:n] {
			if rare[x] {
				kept++
			}
		}
		if (strategy == strategyC || strategy == strategyD) && (kept == 0 || kept == n) {
			strategy = strategyB
		}

		// ship order: B longest first, C and D rare lengths first,
		// later rounds add noise, equal lengths stay together
		var lengthKey [maxLen + 1]int64
		for x := 1; x <= maxLen; x++ {
			lengthKey[x] = int64(x) * keyScale
			if round > 0 {
				noise := round + 1
				if noise > maxNoise {
					noise = maxNoise
				}
				lengthKey[x] += int64(rnd() % uint32(keyScale*noise))
			}
			if (strategy == strategyC || strategy == strategyD) && rare[x] {
				lengthKey[x] += rareFirst
			}
		}
		for i := 0; i < n; i++ {
			order[i], key[i] = i, lengthKey[ships[i]]
		}
		sort.Slice(order, func(p, q int) bool {
			a, b := order[p], order[q]
			if key[a] != key[b] {
				return key[a] > key[b]
			}
			if ships[a] != ships[b] {
				return ships[a] > ships[b]
			}
			return a < b
		})
		for i, id := range order {
			shipID[i], v[i] = id, ships[id]
		}
		// rows: longest first in round 0, then random; shortest first for the
		// second B slot and for D in even rounds (the last row absorbs the rest)
		for j := 0; j < m; j++ {
			rowID[j] = j
		}
		rows := rowID[:m]
		if rowsUp || (strategy == strategyD && round%2 == 0) {
			sort.SliceStable(rows, func(p, q int) bool {
				return rowLen[rows[p]] < rowLen[rows[q]]
			})
		} else if round == 0 {
			sort.SliceStable(rows, func(p, q int) bool {
				return rowLen[rows[p]] > rowLen[rows[q]]
			})
		} else {
			for j := m - 1; j > 0; j-- {
				k := int(rnd() % uint32(j+1))
				rows[j], rows[k] = rows[k], rows[j]
			}
		}

		nodes, aborted = 0, false
		growth := round
		if growth > maxGrowth {
			growth = maxGrowth
		}
		slice := firstSlice * math.Pow(sliceGrowth, float64(growth))
		attemptEnd = elapsed() + time.Duration(slice*float64(time.Second))
		if attemptEnd > timeLimit {
			attemptEnd = timeLimit
		}
		switch strategy {
		case strategyB:
			if (round+slot)%2 == 0 {
				solved = runRows(n, bChecks)
			} else {
				solved = runRows(n, nil)
			}
		case strategyC:
			solved = runRows(kept, nil)
		default:
			if dChecks[ci] != nil {
				solved = runRows(kept, []*residues{dChecks[ci]})
			} else {
				solved = runRows(kept, nil)
			}
		}
		if !solved && elapsed() > timeLimit {
			break
		}
	}

	rows := make([][]string, m)
	for i := 0; i < n; i++ {
		r := rowID[placed[i]]
		rows[r] = append(rows[r], strconv.Itoa(ships[shipID[i]]))
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for _, row := range rows {
		fmt.Fprintln(out, len(row))
		fmt.Fprintln(out, strings.Join(row, " "))
	}
}
