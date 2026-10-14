package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strings"
)

const (
	letterBits = 5 // letters 1 to 26
	headLen    = 12
	gapBits    = 4 // a place in the rest, at most 14
	cutBits    = 2 // 0, 1 or 2 letters deleted
	idShift    = cutBits + 2*gapBits
	idBits     = 13 // word numbers below 8192
	lowBits    = idBits + idShift
	gapMask    = 1<<gapBits - 1
	cutMask    = 1<<cutBits - 1
	idMask     = 1<<idBits - 1
)

// key is the rest of a word: its first headLen letters in hi, the others
// in lo above the word number, the number of deleted letters and their gaps
type key struct{ hi, lo uint64 }

func (a key) sameRest(b key) bool { return a.hi == b.hi && a.lo>>lowBits == b.lo>>lowBits }

func pack(w string, skip1, skip2 int, low uint64) key {
	var k key
	pos := 0
	for i := 0; i < len(w); i++ {
		if i == skip1 || i == skip2 {
			continue
		}
		c := uint64(w[i]-'a') + 1
		if pos < headLen {
			k.hi = k.hi<<letterBits | c
		} else {
			k.lo = k.lo<<letterBits | c
		}
		pos++
	}
	k.lo = k.lo<<lowBits | low
	return k
}

func less(a, b key) bool { return a.hi < b.hi || a.hi == b.hi && a.lo < b.lo }

func main() {
	in := bufio.NewReader(os.Stdin)
	var k int
	fmt.Fscan(in, &k)
	words := make([]string, k)
	for i := range words {
		fmt.Fscan(in, &words[i])
	}
	// two words are at most two edits apart when deleting at most two letters
	// from each leaves the same rest and, gap by gap of the rest, the larger
	// number of deleted letters adds up to at most two
	var keys []key
	for id, w := range words {
		n := len(w)
		tag := uint64(id) << idShift
		keys = append(keys, pack(w, -1, -1, tag))
		for i := 0; i < n; i++ {
			keys = append(keys, pack(w, i, -1, tag|1<<(2*gapBits)|uint64(i)))
			// the second deleted letter, w[j + 1], sits in gap j of the rest
			for j := i; j < n-1; j++ {
				keys = append(keys, pack(w, i, j+1, tag|2<<(2*gapBits)|uint64(i)<<gapBits|uint64(j)))
			}
		}
	}
	sort.Slice(keys, func(a, b int) bool { return less(keys[a], keys[b]) })
	found := make([]bool, k)
	for start := 0; start < len(keys); {
		end := start + 1
		for end < len(keys) && keys[end].sameRest(keys[start]) {
			end++
		}
		if end-start > 1 {
			markGroup(keys[start:end], found)
		}
		start = end
	}
	var chosen []string
	for id, w := range words {
		if found[id] {
			chosen = append(chosen, w)
		}
	}
	sort.Strings(chosen)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	fmt.Fprintln(out, len(chosen))
	if len(chosen) > 0 {
		fmt.Fprintln(out, strings.Join(chosen, "\n"))
	}
}

// markGroup marks the words of one rest that have a close word in it; the keys
// of one word differ in their gaps, so equal pairs come from different words
func markGroup(group []key, found []bool) {
	whole := false
	var singles, doubles []uint64
	for _, x := range group {
		low := x.lo & (1<<lowBits - 1)
		switch low >> (2 * gapBits) & cutMask {
		case 0:
			whole = true
		case 1:
			singles = append(singles, low)
		default:
			doubles = append(doubles, low)
		}
	}
	if whole {
		// the rest is a word itself, at most two deletions from every other
		for _, x := range group {
			found[x.lo&(1<<lowBits-1)>>idShift] = true
		}
		return
	}
	var gapsWith [gapMask + 1]bool
	many := false
	for _, low := range singles {
		gapsWith[low&gapMask] = true
		many = many || low>>idShift != singles[0]>>idShift
	}
	// one deletion from each costs at most two edits
	if many {
		for _, low := range singles {
			found[low>>idShift] = true
		}
	}
	var nearGap [gapMask + 1]bool
	pairOf := func(low uint64) uint64 { return low & (1<<(2*gapBits) - 1) }
	sort.Slice(doubles, func(a, b int) bool { return pairOf(doubles[a]) < pairOf(doubles[b]) })
	for a, low := range doubles {
		g1, g2 := low>>gapBits&gapMask, low&gapMask
		// the same two gaps from another word: two substitutions
		same := a > 0 && pairOf(doubles[a-1]) == pairOf(low) ||
			a+1 < len(doubles) && pairOf(doubles[a+1]) == pairOf(low)
		// one more letter in a gap shared with a single deletion
		near := gapsWith[g1] || gapsWith[g2]
		if same || near {
			found[low>>idShift] = true
		}
		if near {
			nearGap[g1], nearGap[g2] = true, true
		}
	}
	for _, low := range singles {
		if nearGap[low&gapMask] {
			found[low>>idShift] = true
		}
	}
}
