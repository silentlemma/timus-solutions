package main

import (
	"bufio"
	"fmt"
	"math/bits"
	"os"
	"runtime"
	"runtime/debug"
	"sort"
	"strings"
)

const (
	longest   = 15 // no minimal forbidden multiset is longer for bases up to 36
	shift     = 6  // bits per digit in a word code
	digitMask = 1<<shift - 1
	lowBits   = 64 // a word keeps its low 64 bits apart
	lengthAt  = 28 // the length sits above the 26 high bits of the word

	star       = 15 // a pattern count meaning "any number of this digit"
	field      = 4  // bits per count in a packed vector
	fields     = 16 // counts per 64-bit word
	words      = 3
	countMask  = 1<<field - 1
	mix1       = 0x9e3779b97f4a7c15
	mix2       = 0xbf58476d1ce4e5b9
	mix3       = 0x94d049bb133111eb
	mixShift1  = 30
	mixShift2  = 27
	mixShift3  = 31
	loadDen    = 2  // the hash table is kept at most half full
	keyAt      = 32 // a table slot keeps the key above the index
	gcPercent  = 25
	estimateBy = 2 // about base^4 / 2 least words exist
	digitChars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
)

func mix(x uint64) uint64 {
	x += mix1
	x = (x ^ x>>mixShift1) * mix2
	x = (x ^ x>>mixShift2) * mix3
	return x ^ x>>mixShift3
}

// a least number of a pair: length and sorted digits, shift bits each, as
// high and low parts, so that comparing (high, low) compares length first
type number struct {
	high uint64
	low  uint64
}

func encode(length int, hi, lo uint64) number {
	return number{uint64(length)<<lengthAt | hi, lo}
}

func (a number) less(b number) bool {
	return a.high < b.high || a.high == b.high && a.low < b.low
}

func (a number) length() int {
	return int(a.high >> lengthAt)
}

// append a digit to the word (hi, lo)
func push(hi, lo uint64, d int) (uint64, uint64) {
	return hi<<shift | lo>>(lowBits-shift), lo<<shift | uint64(d)
}

// least keeps a number in 16 bytes, its high part fitting 32 bits
type least struct {
	low  uint64
	high uint32
	key  uint32
}

func (r *least) value() number {
	return number{uint64(r.high), r.low}
}

func (r *least) set(v number) {
	r.high, r.low = uint32(v.high), v.low
}

// table is open addressing from a pair key to the index of its least word:
// a slot holds (key+1)<<keyAt | index, and 0 marks an empty one
type table struct {
	slots []uint64
	bits  uint
	used  int
}

func newTable(expected int) *table {
	t := &table{bits: 1}
	for 1<<t.bits < expected*loadDen {
		t.bits++
	}
	t.slots = make([]uint64, 1<<t.bits)
	return t
}

func (t *table) slot(key uint32) int {
	mask := len(t.slots) - 1
	pos := int(uint64(key) * mix1 >> (lowBits - t.bits))
	for t.slots[pos] != 0 && t.slots[pos]>>keyAt != uint64(key)+1 {
		pos = (pos + 1) & mask
	}
	return pos
}

func (t *table) get(key uint32) int32 {
	s := t.slots[t.slot(key)]
	if s == 0 {
		return -1
	}
	return int32(uint32(s))
}

func (t *table) put(key uint32, value int32) {
	if (t.used+1)*loadDen > len(t.slots) {
		old := t.slots
		t.bits++
		t.slots = make([]uint64, len(old)*2)
		for _, s := range old {
			if s != 0 {
				t.slots[t.slot(uint32(s>>keyAt)-1)] = s
			}
		}
	}
	t.slots[t.slot(key)] = (uint64(key)+1)<<keyAt | uint64(uint32(value))
	t.used++
}

// counts of the digits 1 .. m, field bits each, with the set of nonzero
// counts and their total
type counts struct {
	w    [words]uint64
	mask uint64
	sum  int
}

func (v *counts) get(i int) int {
	return int(v.w[i/fields] >> uint(i%fields*field) & countMask)
}

func (v *counts) put(i, c int) {
	at := uint(i % fields * field)
	v.sum += c - v.get(i)
	v.w[i/fields] = v.w[i/fields]&^(countMask<<at) | uint64(c)<<at
	if c != 0 {
		v.mask |= 1 << uint(i)
	} else {
		v.mask &^= 1 << uint(i)
	}
}

func without(v counts, i int) counts {
	v.put(i, 0)
	return v
}

// below tells whether every count of g is at most that of f
func below(g, f *counts) bool {
	for rest := g.mask; rest != 0; rest &= rest - 1 {
		i := bits.TrailingZeros64(rest)
		if g.get(i) > f.get(i) {
			return false
		}
	}
	return true
}

// index keeps vectors sorted by their sets of nonzero counts, to find
// quickly whether one of them lies below a given vector
type index struct {
	items    []counts
	supports []uint64 // the distinct sets, increasing
	begin    []int    // items of supports[s] are begin[s] .. begin[s+1]-1
}

// byMask and byTotal order vectors by their sets of nonzero counts and by
// their totals, with ties by the counts
type byMask []counts
type byTotal []counts

func (v byMask) Len() int           { return len(v) }
func (v byMask) Swap(a, b int)      { v[a], v[b] = v[b], v[a] }
func (v byMask) Less(a, b int) bool { return v[a].mask < v[b].mask }

func (v byTotal) Len() int      { return len(v) }
func (v byTotal) Swap(a, b int) { v[a], v[b] = v[b], v[a] }
func (v byTotal) Less(a, b int) bool {
	x, y := &v[a], &v[b]
	if x.sum != y.sum {
		return x.sum < y.sum
	}
	for k := 0; k < words; k++ {
		if x.w[k] != y.w[k] {
			return x.w[k] < y.w[k]
		}
	}
	return false
}

func newIndex(items []counts) *index {
	sort.Sort(byMask(items))
	x := &index{items: items}
	for i := range items {
		if i == 0 || items[i].mask != items[i-1].mask {
			x.supports = append(x.supports, items[i].mask)
			x.begin = append(x.begin, i)
		}
	}
	x.begin = append(x.begin, len(items))
	return x
}

func (x *index) inGroup(s int, f *counts) bool {
	for j := x.begin[s]; j < x.begin[s+1]; j++ {
		if below(&x.items[j], f) {
			return true
		}
	}
	return false
}

// covers tells whether some item lies below f: by the subsets of its support
// or by a scan of the supports, whichever is shorter
func (x *index) covers(f *counts) bool {
	if 1<<uint(bits.OnesCount64(f.mask)) < len(x.supports) {
		for sub := f.mask; ; sub = (sub - 1) & f.mask {
			lo, hi := 0, len(x.supports)
			for lo < hi {
				mid := (lo + hi) / 2
				if x.supports[mid] < sub {
					lo = mid + 1
				} else {
					hi = mid
				}
			}
			if lo < len(x.supports) && x.supports[lo] == sub && x.inGroup(lo, f) {
				return true
			}
			if sub == 0 {
				return false
			}
		}
	}
	for s, sup := range x.supports {
		if sup&^f.mask == 0 && x.inGroup(s, f) {
			return true
		}
	}
	return false
}

// minimal keeps the minimal vectors: one that lies below another has a
// smaller total, so the vectors are taken by total, and those of one total
// are checked against the smaller ones only
func minimal(vectors []counts) []counts {
	sort.Sort(byTotal(vectors))
	var kept []counts
	smaller := newIndex(nil)
	for i := 0; i < len(vectors); {
		j := i
		grown := false
		for ; j < len(vectors) && vectors[j].sum == vectors[i].sum; j++ {
			repeat := j > i && vectors[j].w == vectors[j-1].w
			if !repeat && !smaller.covers(&vectors[j]) {
				kept = append(kept, vectors[j])
				grown = true
			}
		}
		if grown && j < len(vectors) {
			smaller = newIndex(append([]counts(nil), kept...))
		}
		i = j
	}
	return kept
}

// run is the consecutive nodes start, start+1, ..., start+count-1
type run struct{ start, count uint32 }

// patterns over the first n digits, stored as a trie of (parent, count)
// nodes; the patterns of one solved set are a few runs of consecutive nodes
type patterns struct {
	nodes    []uint32 // parent<<field | count; node 0 is empty
	stars    []uint32
	memo     map[uint64]int
	runs     []run
	firstRun []int // the runs of result i are firstRun[i] .. firstRun[i+1]-1
}

func newPatterns(digits int) *patterns {
	p := &patterns{nodes: []uint32{0}, stars: []uint32{0}, memo: map[uint64]int{}, firstRun: []int{0}}
	for i := 0; i < digits; i++ {
		p.stars = append(p.stars, p.extend(p.stars[i], star))
	}
	return p
}

func (p *patterns) extend(parent uint32, count int) uint32 {
	p.nodes = append(p.nodes, parent<<field|uint32(count))
	return uint32(len(p.nodes) - 1)
}

func (p *patterns) members(result int) []uint32 {
	var out []uint32
	for _, r := range p.runs[p.firstRun[result]:p.firstRun[result+1]] {
		for i := uint32(0); i < r.count; i++ {
			out = append(out, r.start+i)
		}
	}
	return out
}

func (p *patterns) decode(node uint32, n int) counts {
	var v counts
	for i := n - 1; i >= 0; i-- {
		c := uint64(p.nodes[node] & countMask)
		v.w[i/fields] |= c << uint(i%fields*field)
		if c != 0 {
			v.mask |= 1 << uint(i)
		}
		node = p.nodes[node] >> field
	}
	return v
}

// solve returns the index of the result: patterns covering exactly the count
// vectors over the first n digits above none of gens (minimal vectors); the
// last digit takes each fixed count below the largest in gens, then any
func (p *patterns) solve(gens []counts, n int) int {
	key := mix(uint64(n)) + uint64(len(gens))
	for _, g := range gens {
		key += mix(g.w[0]) ^ mix(g.w[1]+mix1)*mix3 ^ mix(g.w[2]+mix2)
	}
	if found, ok := p.memo[key]; ok {
		return found
	}
	var result []run
	if len(gens) == 0 {
		result = append(result, run{p.stars[n], 1})
	} else if gens[0].mask != 0 {
		last := n - 1
		top := 0
		for j := range gens {
			if c := gens[j].get(last); c > top {
				top = c
			}
		}
		// levels[k]: the minimal gens that apply with k copies of the last
		// digit; as gens are minimal, a newcomer with k copies never lies
		// above an earlier one, and the last level serves any count
		levels := make([][]counts, top+1)
		for k := 0; k <= top; k++ {
			var fresh []counts
			for j := range gens {
				if gens[j].get(last) == k {
					fresh = append(fresh, without(gens[j], last))
				}
			}
			if k > 0 {
				newcomers := newIndex(append([]counts(nil), fresh...))
				for j := range levels[k-1] {
					if !newcomers.covers(&levels[k-1][j]) {
						levels[k] = append(levels[k], levels[k-1][j])
					}
				}
			}
			levels[k] = append(levels[k], fresh...)
		}
		open := newIndex(levels[top])
		for k := 0; k < top; k++ {
			sub := p.solve(levels[k], last)
			r := run{uint32(len(p.nodes)), 0}
			for _, node := range p.members(sub) {
				// a prefix allowed with any count is already covered below
				v := p.decode(node, last)
				if open.covers(&v) {
					p.extend(node, k)
					r.count++
				}
			}
			result = append(result, r)
		}
		sub := p.solve(open.items, last)
		r := run{uint32(len(p.nodes)), 0}
		for _, node := range p.members(sub) {
			p.extend(node, star)
			r.count++
		}
		result = append(result, r)
	}
	p.runs = append(p.runs, result...)
	p.firstRun = append(p.firstRun, len(p.runs))
	p.memo[key] = len(p.firstRun) - 2
	return len(p.firstRun) - 2
}

func main() {
	// the memory limit is tight, so the heap may grow only a little over the
	// live data
	debug.SetGCPercent(gcPercent)
	var base int
	fmt.Fscan(bufio.NewReader(os.Stdin), &base)
	m := base - 1
	// the least number of every pair (sum of digits, sum of squares) with at most
	// longest digits: digits are appended in increasing order, and adding the
	// same digits to two words keeps their order, so the best per pair suffices
	width := uint32(longest*m*m + 1)
	estimate := base * base * base * base / estimateBy
	best := make([]least, 1, estimate+1)
	tab := newTable(estimate + 1)
	tab.put(0, 0)
	for d := 1; d < base; d++ {
		step := uint32(d)*width + uint32(d*d)
		count := len(best)
		for i := 0; i < count; i++ {
			key, length := best[i].key, best[i].value().length()
			hi, lo := best[i].value().high&(1<<lengthAt-1), best[i].low
			for grown := length + 1; grown <= longest; grown++ {
				key += step
				hi, lo = push(hi, lo, d)
				candidate := encode(grown, hi, lo)
				at := tab.get(key)
				if at < 0 {
					tab.put(key, int32(len(best)))
					best = append(best, least{candidate.low, uint32(candidate.high), key})
				} else if candidate.less(best[at].value()) {
					best[at].set(candidate)
				}
			}
		}
	}
	// a minimal forbidden multiset is not the least of its pair, while every
	// multiset with one digit fewer is; without its largest digit it is one
	// of the least words, so each least word is grown by one digit at its end
	var forbidden []counts
	var digits [longest]int
	for i := range best {
		r := &best[i]
		length := r.value().length()
		if length == 0 || length >= longest {
			continue
		}
		hi, lo := r.value().high&(1<<lengthAt-1), r.low
		for i := length - 1; i >= 0; i-- {
			digits[i] = int(lo & digitMask)
			lo = lo>>shift | (hi&digitMask)<<(lowBits-shift)
			hi >>= shift
		}
		hi, lo = r.value().high&(1<<lengthAt-1), r.low
		for add := digits[length-1]; add < base; add++ {
			key := r.key + uint32(add)*width + uint32(add*add)
			gh, gl := push(hi, lo, add)
			if best[tab.get(key)].value() == encode(length+1, gh, gl) {
				continue
			}
			isMinimal := true
			for i := 0; i < length && isMinimal; i++ {
				drop := digits[i]
				if drop == add || i > 0 && digits[i-1] == drop {
					continue
				}
				var rh, rl uint64
				for j := 0; j < length; j++ {
					if j != i {
						rh, rl = push(rh, rl, digits[j])
					}
				}
				rh, rl = push(rh, rl, add)
				shorter := key - uint32(drop)*width - uint32(drop*drop)
				isMinimal = best[tab.get(shorter)].value() == encode(length, rh, rl)
			}
			if isMinimal {
				var f counts
				for i := 0; i < length; i++ {
					f.put(digits[i]-1, f.get(digits[i]-1)+1)
				}
				f.put(add-1, f.get(add-1)+1)
				forbidden = append(forbidden, f)
			}
		}
	}
	best, tab = nil, nil
	// the least words are gone: give their memory back before the patterns
	runtime.GC()
	debug.FreeOSMemory()
	p := newPatterns(m)
	top := p.solve(minimal(forbidden), m)
	var lines []string
	for _, node := range p.members(top) {
		v := p.decode(node, m)
		var line strings.Builder
		for i := 0; i < m; i++ {
			ch := string(digitChars[i+1])
			if c := v.get(i); c == star {
				line.WriteString(ch + "*")
			} else {
				line.WriteString(strings.Repeat(ch, c))
			}
		}
		lines = append(lines, line.String())
	}
	sort.Strings(lines)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for _, line := range lines {
		out.WriteString(line)
		out.WriteString("\n")
	}
}
