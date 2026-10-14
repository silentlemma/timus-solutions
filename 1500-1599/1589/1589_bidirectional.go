package main

import (
	"bufio"
	"fmt"
	"math/bits"
	"os"
	"strings"
	"time"
)

// Mask is a set of grid cells, one bit each (grid <= 8 x 8).
type Mask = uint64

const (
	sides     = 4
	maxCells  = 64
	none      = -1
	inf       = 1000000
	timeLimit = 4850 * time.Millisecond // search before giving up (the limit is 5 s)
)

var (
	dRow = [sides]int{-1, 1, 0, 0}
	dCol = [sides]int{0, 0, -1, 1}
	step = "udlr"
	opp  = [sides]int{1, 0, 3, 2}
)

const (
	up, down, left, right = 0, 1, 2, 3
)

func low(x Mask) int         { return bits.TrailingZeros64(x) }
func has(m Mask, c int) bool { return (m>>uint(c))&1 != 0 }
func bit(c int) Mask         { return 1 << uint(c) }
func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
func minInt(a, b int) int {
	if a < b {
		return a
	}
	return b
}

var (
	started                         time.Time
	rows, cols, cells               int
	floorM, goalM, deadM, deadPullM Mask
	notFirstCol, notLastCol         Mask
	nb                              [sides][maxCells]int // the neighbour in a direction, none outside
	startPlayer                     int
	startBoxes                      Mask
	floorCount, goalCount           int
	floorCell, floorIndex           [maxCells]int
)

// the player's area: the floor reachable from p around the boxes, as bit-parallel growth
func grow(r Mask) Mask {
	sideways := ((r << 1) & notFirstCol) | ((r >> 1) & notLastCol)
	return r | sideways | (r << uint(cols)) | (r >> uint(cols))
}

func flood(seed, within Mask) Mask {
	r := seed
	for {
		x := grow(r) & within
		if x == r {
			return r
		}
		r = x
	}
}

func reach(p int, boxes Mask) Mask { return flood(bit(p), floorM&^boxes) }

// a state: a bit per floor cell for the boxes, then the floor index of the
// lowest cell of the player's area
func packKey(boxes Mask, player int) Mask {
	var k Mask
	for b := boxes; b != 0; b &= b - 1 {
		k |= bit(floorIndex[low(b)])
	}
	return k | Mask(floorIndex[player])<<uint(floorCount)
}

func keyBoxes(key Mask) Mask {
	var b Mask
	for k := key & (bit(floorCount) - 1); k != 0; k &= k - 1 {
		b |= bit(floorCell[low(k)])
	}
	return b
}

func keyPlayer(key Mask) int { return floorCell[key>>uint(floorCount)] }

// A box is frozen when it can move along neither axis: a wall or a frozen box
// on either side, or dead squares on both sides. Boxes already found frozen
// count as walls while their neighbours are checked.
var (
	frozenAsWall  Mask
	frozenOffGoal bool
)

func wallLike(c int) bool { return c < 0 || !has(floorM, c) || has(frozenAsWall, c) }

func axisBlocked(x, d1, d2 int, boxes Mask) bool {
	a, b := nb[d1][x], nb[d2][x]
	if wallLike(a) || wallLike(b) {
		return true
	}
	if has(deadM, a) && has(deadM, b) {
		return true
	}
	return (has(boxes, a) && frozen(a, boxes)) || (has(boxes, b) && frozen(b, boxes))
}

func frozen(x int, boxes Mask) bool {
	saved := frozenAsWall
	frozenAsWall |= bit(x)
	f := axisBlocked(x, left, right, boxes) && axisBlocked(x, up, down, boxes)
	frozenAsWall = saved
	if f && !has(goalM, x) {
		frozenOffGoal = true
	}
	return f
}

// the box just pushed to x froze a box that is not on a goal
func freezeDeadlock(x int, boxes Mask) bool {
	frozenAsWall = 0
	frozenOffGoal = false
	return frozen(x, boxes) && frozenOffGoal
}

// h: the sum of each box's push distance to its nearest target; boxes that
// cannot be matched to distinct reachable targets mean a deadlock
var (
	canReach   [2][maxCells]Mask // [push or pull search][cell]: targets a box there can get to
	nearest    [2][maxCells]int
	matchOf    [maxCells]int
	boxTargets [maxCells]Mask
	visited    Mask
)

func augment(i int) bool {
	for m := boxTargets[i] &^ visited; m != 0; m &= m - 1 {
		j := low(m)
		visited |= bit(j)
		if matchOf[j] < 0 || augment(matchOf[j]) {
			matchOf[j] = i
			return true
		}
	}
	return false
}

func heuristic(boxes Mask, dir int) int {
	k, h := 0, 0
	for b := boxes; b != 0; b &= b - 1 {
		h += nearest[dir][low(b)]
		boxTargets[k] = canReach[dir][low(b)]
		k++
	}
	for j := 0; j < goalCount; j++ {
		matchOf[j] = none
	}
	for i := 0; i < k; i++ {
		visited = 0
		if !augment(i) {
			return none
		}
	}
	return h
}

type push struct{ box, dir int }

var best, candidates []push

// The pushes worth trying, or a deadlock. If every push of the boxes around
// a region the player cannot reach goes inward and can be made now, one of
// them is needed first, so only those are tried.
func generatePushes(boxes, area Mask, out []push) ([]push, bool) {
	out = out[:0]
	for bb := boxes; bb != 0; bb &= bb - 1 {
		b := low(bb)
		for d := 0; d < sides; d++ {
			s, t := nb[opp[d]][b], nb[d][b]
			if s >= 0 && t >= 0 && has(area, s) && has(floorM, t) && !has(boxes, t) {
				out = append(out, push{b, d})
			}
		}
	}
	unreached := floorM &^ boxes &^ area
	best = best[:0]
	bestCount := len(out) + 1
	for unreached != 0 {
		corral := flood(unreached&(0-unreached), floorM&^boxes&^area)
		unreached &^= corral
		barrier := grow(corral) & boxes
		if corral&goalM == 0 && barrier&^goalM == 0 {
			continue // finished corral
		}
		inward, ready := true, true
		candidates = candidates[:0]
		for bb := barrier; bb != 0 && inward; bb &= bb - 1 {
			b := low(bb)
			for d := 0; d < sides; d++ {
				s, t := nb[opp[d]][b], nb[d][b]
				// the player stands outside the corral and off the barrier
				if s < 0 || !has(floorM, s) || has(corral, s) || has(barrier, s) {
					continue
				}
				if t < 0 || !has(floorM, t) || has(barrier, t) {
					continue // blocked for good
				}
				if !has(corral, t) {
					inward = false // a push away from the corral
					break
				}
				if has(area, s) {
					candidates = append(candidates, push{b, d})
				} else {
					ready = false
				}
			}
		}
		if !inward {
			continue
		}
		if ready && len(candidates) == 0 {
			return out, false // unfinished, and no push can ever enter it
		}
		if ready && len(candidates) < bestCount {
			bestCount = len(candidates)
			best = append(best[:0], candidates...)
		}
	}
	if bestCount <= len(out) {
		out = append(out[:0], best...)
	}
	return out, true
}

// One open-addressing table holds the states of both searches; pull-search
// keys carry pulled. A slot keeps the key and the move that made it.
const (
	pulled    Mask = 1 << 63
	tableBits      = 22
	table          = 1 << tableBits
	tableMask      = table - 1
	tableFill      = table / 100 * 88 // the most keys before the table counts as full
	root           = 255
	golden    Mask = 0x9E3779B97F4A7C15
	keyBits        = 64
	present        = -1
	full           = -2
)

var (
	tableKey  []Mask
	tableMove []uint8 // floor index of the moved box * 4 + direction
	keyCount  int
)

func slotOf(key Mask) int { return int((key * golden) >> (keyBits - tableBits)) }

func insertKey(key Mask) int {
	h := slotOf(key)
	for ; tableKey[h] != 0; h = (h + 1) & tableMask {
		if tableKey[h] == key {
			return present
		}
	}
	if keyCount >= tableFill {
		return full
	}
	keyCount++
	tableKey[h] = key
	return h
}

// the slot of key, or else the empty slot where it would go
func probe(key Mask) (int, bool) {
	h := slotOf(key)
	for ; tableKey[h] != 0; h = (h + 1) & tableMask {
		if tableKey[h] == key {
			return h, true
		}
	}
	return h, false
}

// put key into the empty slot s that probe found, unless the table is full
func insertAt(s int, key Mask) bool {
	if keyCount >= tableFill {
		return false
	}
	keyCount++
	tableKey[s] = key
	return true
}

func hasKey(key Mask) bool {
	for h := slotOf(key); tableKey[h] != 0; h = (h + 1) & tableMask {
		if tableKey[h] == key {
			return true
		}
	}
	return false
}

func findKey(key Mask) int {
	h := slotOf(key)
	for tableKey[h] != key {
		h = (h + 1) & tableMask
	}
	return h
}

// Open lists: buckets by f = g + weight * h, each a stack threaded through the
// table slots (a slot is queued at most once), so the memory stays fixed.
const (
	buckets = 4096
	gBits   = 9
	gMask   = 1<<gBits - 1
	weight  = 3
)

var tableNext []uint32 // (next slot + 1) << gBits | g

type open struct {
	head   [buckets]uint32 // slot + 1, 0 when empty
	lowest int
}

func (o *open) push(slot, g, f int) {
	f = minInt(f, buckets-1)
	tableNext[slot] = o.head[f]<<gBits | uint32(minInt(g, gMask))
	o.head[f] = uint32(slot + 1)
	if f < o.lowest {
		o.lowest = f
	}
}

func (o *open) pop() (int, int, bool) {
	for o.lowest < buckets && o.head[o.lowest] == 0 {
		o.lowest++
	}
	if o.lowest >= buckets {
		return 0, 0, false
	}
	slot := int(o.head[o.lowest] - 1)
	o.head[o.lowest] = tableNext[slot] >> gBits
	return slot, int(tableNext[slot] & gMask), true
}

var pushOpen, pullOpen = &open{lowest: buckets}, &open{lowest: buckets}

const pushRounds, pullRounds = 8, 1 // expansions of each search per round

func walk(from, to int, boxes Mask) string {
	if from == to {
		return ""
	}
	var prev [maxCells]int
	var queue [maxCells]int
	for i := 0; i < cells; i++ {
		prev[i] = -2
	}
	prev[from] = none
	head, tail := 0, 0
	queue[tail] = from
	tail++
	for head < tail {
		x := queue[head]
		head++
		if x == to {
			break
		}
		for d := 0; d < sides; d++ {
			y := nb[d][x]
			if y < 0 || !has(floorM, y) || has(boxes, y) || prev[y] != -2 {
				continue
			}
			prev[y] = x*sides + d
			queue[tail] = y
			tail++
		}
	}
	var s []byte
	for x := to; x != from; x = prev[x] / sides {
		s = append(s, step[prev[x]%sides])
	}
	for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
		s[i], s[j] = s[j], s[i]
	}
	return string(s)
}

// the plan through the state key, which both searches reached (or which is solved)
func buildAnswer(key Mask) string {
	var pushes []push
	for k := key; ; { // back from key to the start through the push search
		move := int(tableMove[findKey(k)])
		if move == root {
			break
		}
		b, d := floorCell[move/sides], move%sides
		t := nb[d][b]
		pushes = append(pushes, push{b, d})
		boxes := (keyBoxes(k) &^ bit(t)) | bit(b)
		k = packKey(boxes, low(reach(nb[opp[d]][b], boxes)))
	}
	for i, j := 0, len(pushes)-1; i < j; i, j = i+1, j-1 {
		pushes[i], pushes[j] = pushes[j], pushes[i]
	}
	if keyBoxes(key) != goalM {
		for k := key; ; { // forward to the goal: each pull, undone, is a push
			move := int(tableMove[findKey(k|pulled)])
			if move == root {
				break
			}
			x, d := floorCell[move/sides], move%sides
			b := nb[d][x]
			pushes = append(pushes, push{x, d})
			boxes := (keyBoxes(k) &^ bit(x)) | bit(b)
			k = packKey(boxes, low(reach(x, boxes)))
		}
	}
	var out strings.Builder
	boxes := startBoxes
	pos := startPlayer
	for _, p := range pushes {
		out.WriteString(walk(pos, nb[opp[p.dir]][p.box], boxes))
		out.WriteByte(step[p.dir] - 'a' + 'A')
		boxes = (boxes &^ bit(p.box)) | bit(nb[p.dir][p.box])
		pos = p.box
	}
	return out.String()
}

// For sets of k = 2..MOST cells, the player cells from which these boxes alone
// can be solved (a pull search from the goals) or reached (a push search from
// the start); a state with a failing subset is dead.
const (
	most     = 4
	trio     = 3
	byteBits = 8
	near     = 3 // sets of four only with boxes this close to the moved one
)

var (
	binom    [maxCells + 1][most + 2]int
	seenSet  []uint8
	setTable [2][most + 1][]Mask // [solvable or reachable][k][set]: player cells
)

func setIndex(boxes Mask) int { // the combinatorial number system
	index, i := 0, 1
	for b := boxes; b != 0; b &= b - 1 {
		index += binom[floorIndex[low(b)]][i]
		i++
	}
	return index
}

func firstVisit(set Mask, area int) bool {
	n := setIndex(set)*floorCount + floorIndex[area]
	if (seenSet[n/byteBits]>>uint(n%byteBits))&1 != 0 {
		return false
	}
	seenSet[n/byteBits] |= 1 << uint(n%byteBits)
	return true
}

func buildSetTable(dir, k int) {
	seenSet = make([]uint8, (binom[floorCount][k]*floorCount+byteBits-1)/byteBits)
	table := make([]Mask, binom[floorCount][k])
	setTable[dir][k] = table
	queue := tableKey
	head, tail := 0, 0
	var at [maxCells]int
	n := 0
	src := goalM
	if dir == 1 {
		src = startBoxes
	}
	for c := src; c != 0; c &= c - 1 {
		at[n] = low(c)
		n++
	}
	var pick [most]int
	for i := 0; i < k; i++ {
		pick[i] = i
	}
	for k <= n { // every k of the start boxes or the goals
		var set Mask
		for i := 0; i < k; i++ {
			set |= bit(at[pick[i]])
		}
		if dir == 1 { // the player where it starts
			area := low(reach(startPlayer, set))
			if firstVisit(set, area) {
				queue[tail] = packKey(set, area)
				tail++
			}
		} else { // the player in any free area
			for rest := floorM &^ set; rest != 0; {
				area := reach(low(rest), set)
				rest &^= area
				if firstVisit(set, low(area)) {
					queue[tail] = packKey(set, low(area))
					tail++
				}
			}
		}
		i := k - 1
		for i >= 0 && pick[i] == n-k+i {
			i--
		}
		if i < 0 {
			break
		}
		pick[i]++
		for j := i + 1; j < k; j++ {
			pick[j] = pick[j-1] + 1
		}
	}
	for head < tail {
		key := queue[head]
		head++
		boxes := keyBoxes(key)
		area := reach(keyPlayer(key), boxes)
		table[setIndex(boxes)] |= area
		for bb := boxes; bb != 0; bb &= bb - 1 {
			b := low(bb)
			for d := 0; d < sides; d++ {
				x := nb[opp[d]][b]
				if x < 0 || !has(area, x) {
					continue
				}
				// a push from x moves the box to y; a pull to x moves the player to y
				y, to, dest := nb[opp[d]][x], nb[opp[d]][x], x
				if dir == 1 {
					y, to, dest = nb[d][b], b, nb[d][b]
				}
				if y < 0 || !has(floorM, y) || has(boxes, y) {
					continue
				}
				moved := (boxes &^ bit(b)) | bit(dest)
				where := low(reach(to, moved))
				if firstVisit(moved, where) {
					queue[tail] = packKey(moved, where)
					tail++
				}
			}
		}
	}
	for i := 0; i < tail; i++ {
		queue[i] = 0
	}
}

// The set index of floor indexes a < b < ... with x added in its place:
// binom[v][rank] summed over the sorted values.
func index2(a, x int) int {
	if x < a {
		return binom[x][1] + binom[a][2]
	}
	return binom[a][1] + binom[x][2]
}

func index3(a, b, x int) int {
	switch {
	case x < a:
		return binom[x][1] + binom[a][2] + binom[b][trio]
	case x < b:
		return binom[a][1] + binom[x][2] + binom[b][trio]
	}
	return binom[a][1] + binom[b][2] + binom[x][trio]
}

func index4(a, b, c, x int) int {
	switch {
	case x < a:
		return binom[x][1] + binom[a][2] + binom[b][trio] + binom[c][most]
	case x < b:
		return binom[a][1] + binom[x][2] + binom[b][trio] + binom[c][most]
	case x < c:
		return binom[a][1] + binom[b][2] + binom[x][trio] + binom[c][most]
	}
	return binom[a][1] + binom[b][2] + binom[c][trio] + binom[x][most]
}

// every set of up to most boxes with the moved box t is in the table; the
// other boxes come by floor index in increasing order
func setsOK(dir int, boxes Mask, t, player int) bool {
	var other, close [maxCells]int
	n, nc := 0, 0
	for b := boxes &^ bit(t); b != 0; b &= b - 1 {
		c := low(b)
		other[n] = floorIndex[c]
		n++
		if abs(c/cols-t/cols) <= near && abs(c%cols-t%cols) <= near {
			close[nc] = floorIndex[c]
			nc++
		}
	}
	ft, pb := floorIndex[t], bit(player)
	pairs, trios, fours := setTable[dir][2], setTable[dir][trio], setTable[dir][most]
	for i := 0; i < n; i++ {
		if pairs[index2(other[i], ft)]&pb == 0 {
			return false
		}
	}
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			if trios[index3(other[i], other[j], ft)]&pb == 0 {
				return false
			}
		}
	}
	for i := 0; i < nc; i++ {
		for j := i + 1; j < nc; j++ {
			for l := j + 1; l < nc; l++ {
				if fours[index4(close[i], close[j], close[l], ft)]&pb == 0 {
					return false
				}
			}
		}
	}
	return true
}

// Both expansions return the key of a state where the searches met (or a
// solved state), 0 if none yet; tableFull is set when the table is full.
var (
	tableFull bool
	pushes    []push
)

func expandPush(slot, g int) Mask {
	g++
	key := tableKey[slot]
	boxes := keyBoxes(key)
	area := reach(keyPlayer(key), boxes)
	var ok bool
	if pushes, ok = generatePushes(boxes, area, pushes); !ok {
		return 0
	}
	for _, p := range pushes {
		b, d := p.box, p.dir
		t := nb[d][b]
		if has(deadM, t) {
			continue
		}
		moved := (boxes &^ bit(b)) | bit(t)
		if freezeDeadlock(t, moved) {
			continue
		}
		next := packKey(moved, low(reach(b, moved)))
		s, found := probe(next)
		if found || !setsOK(0, moved, t, b) {
			continue
		}
		if !insertAt(s, next) {
			tableFull = true
			return 0
		}
		tableMove[s] = uint8(floorIndex[b]*sides + d)
		if moved == goalM || hasKey(next|pulled) {
			return next
		}
		if h := heuristic(moved, 0); h != none { // a deadlocked state stays in the table as visited
			pushOpen.push(s, g, g+weight*h)
		}
	}
	return 0
}

func expandPull(slot, g int) Mask {
	g++
	key := tableKey[slot] &^ pulled
	boxes := keyBoxes(key)
	area := reach(keyPlayer(key), boxes)
	for bb := boxes; bb != 0; bb &= bb - 1 {
		b := low(bb)
		for d := 0; d < sides; d++ {
			// the player at x pulls the box from b to x and steps back to y
			x := nb[opp[d]][b]
			if x < 0 || !has(area, x) || has(deadPullM, x) {
				continue
			}
			y := nb[opp[d]][x]
			if y < 0 || !has(floorM, y) || has(boxes, y) {
				continue
			}
			moved := (boxes &^ bit(b)) | bit(x)
			next := packKey(moved, low(reach(y, moved)))
			s, found := probe(next | pulled)
			if found || !setsOK(1, moved, x, y) {
				continue
			}
			if !insertAt(s, next|pulled) {
				tableFull = true
				return 0
			}
			tableMove[s] = uint8(floorIndex[x]*sides + d)
			if hasKey(next) {
				return next
			}
			if h := heuristic(moved, 1); h != none {
				pullOpen.push(s, g, g+weight*h)
			}
		}
	}
	return 0
}

// The push search from the start and the pull search from the goal take
// turns until some state is in both.
func solve() Mask {
	rootKey := packKey(startBoxes, low(reach(startPlayer, startBoxes)))
	tableMove[insertKey(rootKey)] = root
	if h0 := heuristic(startBoxes, 0); h0 != none {
		pushOpen.push(findKey(rootKey), 0, weight*h0)
	}
	hg := heuristic(goalM, 1)
	for rest := floorM &^ goalM; rest != 0; { // the boxes on the goals, the player anywhere
		area := reach(low(rest), goalM)
		rest &^= area
		key := packKey(goalM, low(area))
		s := insertKey(key | pulled)
		if s < 0 {
			continue
		}
		tableMove[s] = root
		if key == rootKey {
			return key
		}
		if hg != none {
			pullOpen.push(s, 0, weight*hg)
		}
	}
	const clockEvery = 128
	for round := 0; ; round++ {
		if round%clockEvery == 0 && time.Since(started) > timeLimit {
			return 0
		}
		progress := false
		for i := 0; i < pushRounds; i++ {
			slot, g, ok := pushOpen.pop()
			if !ok {
				break
			}
			progress = true
			if k := expandPush(slot, g); k != 0 {
				return k
			}
			if tableFull {
				return 0
			}
		}
		for i := 0; i < pullRounds; i++ {
			slot, g, ok := pullOpen.pop()
			if !ok {
				break
			}
			progress = true
			if k := expandPull(slot, g); k != 0 {
				return k
			}
			if tableFull {
				return 0
			}
		}
		if !progress {
			return 0
		}
	}
}

// push distances of a lone box: dist[target][cell] to bring a box from cell
// to the target (pull = false), or from the target to cell (pull = true)
var dist [2][maxCells][maxCells]int

func boxDistances(targets Mask, dir int) Mask {
	unreachable := floorM
	j := 0
	for tg := targets; tg != 0; tg &= tg - 1 {
		D := &dist[dir][j]
		j++
		var queue [maxCells]int
		head, tail := 0, 0
		for i := range D {
			D[i] = inf
		}
		D[low(tg)] = 0
		queue[tail] = low(tg)
		tail++
		for head < tail {
			x := queue[head]
			head++
			unreachable &^= bit(x)
			for d := 0; d < sides; d++ {
				// a box pushed from y to x (the player behind y), or from x to y
				var y, p int
				if dir == 1 {
					y, p = nb[d][x], nb[opp[d]][x]
				} else {
					y, p = nb[opp[d]][x], none
					if y >= 0 {
						p = nb[opp[d]][y]
					}
				}
				if y < 0 || p < 0 || !has(floorM, y) || !has(floorM, p) || D[y] != inf {
					continue
				}
				D[y] = D[x] + 1
				queue[tail] = y
				tail++
			}
		}
	}
	return unreachable
}

func main() {
	started = time.Now()
	sc := bufio.NewScanner(os.Stdin)
	var lines []string
	for sc.Scan() {
		lines = append(lines, strings.TrimRight(sc.Text(), "\r\n "))
	}
	// drop the empty rows and columns around the level
	for len(lines) > 0 && lines[len(lines)-1] == "" {
		lines = lines[:len(lines)-1]
	}
	for len(lines) > 0 && lines[0] == "" {
		lines = lines[1:]
	}
	lead := maxCells
	for _, line := range lines {
		if line != "" {
			lead = minInt(lead, len(line)-len(strings.TrimLeft(line, " ")))
		}
	}
	for i, line := range lines {
		if len(line) > lead {
			lines[i] = line[lead:]
		} else {
			lines[i] = ""
		}
	}
	rows = len(lines)
	for _, line := range lines {
		if len(line) > cols {
			cols = len(line)
		}
	}
	cells = rows * cols
	var wallM Mask
	for r := 0; r < rows; r++ {
		for c := 0; c < cols; c++ {
			ch := byte(' ')
			if c < len(lines[r]) {
				ch = lines[r][c]
			}
			id := r*cols + c
			switch ch {
			case '#':
				wallM |= bit(id)
			case '.':
				goalM |= bit(id)
			case '$':
				startBoxes |= bit(id)
			case '*':
				goalM |= bit(id)
				startBoxes |= bit(id)
			case '@':
				startPlayer = id
			case '+':
				goalM |= bit(id)
				startPlayer = id
			}
		}
	}
	for i := 0; i < cells; i++ {
		for d := 0; d < sides; d++ {
			r, c := i/cols+dRow[d], i%cols+dCol[d]
			nb[d][i] = none
			if r >= 0 && r < rows && c >= 0 && c < cols {
				nb[d][i] = r*cols + c
			}
		}
		if i%cols != 0 {
			notFirstCol |= bit(i)
		}
		if i%cols != cols-1 {
			notLastCol |= bit(i)
		}
	}
	// the floor: the cells the player reaches through non-walls; boxes on
	// goals walled off from the player never move and count as walls
	floorM = ^wallM
	if cells < maxCells {
		floorM &= bit(cells) - 1
	}
	floorM = reach(startPlayer, 0)
	goalM &= floorM
	startBoxes &= floorM
	for f := floorM; f != 0; f &= f - 1 {
		floorIndex[low(f)] = floorCount
		floorCell[floorCount] = low(f)
		floorCount++
	}
	goalCount = bits.OnesCount64(goalM)
	tableKey = make([]Mask, table)
	tableMove = make([]uint8, table)
	tableNext = make([]uint32, table)
	deadM = boxDistances(goalM, 0)
	deadPullM = boxDistances(startBoxes, 1)
	for i := 0; i <= maxCells; i++ {
		for j := 0; j <= most+1; j++ {
			switch {
			case j == 0:
				binom[i][j] = 1
			case i == 0:
				binom[i][j] = 0
			default:
				binom[i][j] = binom[i-1][j-1] + binom[i-1][j]
			}
		}
	}
	for k := 2; k <= most && k <= goalCount; k++ {
		for dir := 0; dir < 2; dir++ {
			buildSetTable(dir, k)
		}
	}
	seenSet = nil
	for dir := 0; dir < 2; dir++ {
		for c := 0; c < cells; c++ {
			nearest[dir][c] = inf
			for j := 0; j < goalCount; j++ {
				if dist[dir][j][c] < inf {
					canReach[dir][c] |= bit(j)
				}
				nearest[dir][c] = minInt(nearest[dir][c], dist[dir][j][c])
			}
		}
	}
	answer := ""
	if startBoxes != goalM {
		if meet := solve(); meet != 0 {
			answer = buildAnswer(meet)
		}
	}
	fmt.Println(answer)
}
