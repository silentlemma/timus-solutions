package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

const side = 100

type box struct{ lo, hi, lo2, hi2 int }

func grow(a, b box) box {
	return box{min(a.lo, b.lo), max(a.hi, b.hi), min(a.lo2, b.lo2), max(a.hi2, b.hi2)}
}

// area of the smallest picture holding the box, at least 100 by 100
func area(b box) int64 {
	return int64(max(b.hi-b.lo, side)) * int64(max(b.hi2-b.lo2, side))
}

// best splits the spots by a line across the first axis: sorted by their
// low edge, a prefix and the rest can hang apart exactly when the prefix
// ends no later than the rest begins
func best(spots []box) int64 {
	sort.Slice(spots, func(i, j int) bool { return spots[i].lo < spots[j].lo })
	n := len(spots)
	suffix := make([]box, n)
	suffix[n-1] = spots[n-1]
	for i := n - 2; i >= 0; i-- {
		suffix[i] = grow(spots[i], suffix[i+1])
	}
	result := area(suffix[0])
	prefix := spots[0]
	for k := 1; k < n; k++ {
		if prefix.hi <= spots[k].lo {
			result = min64(result, area(prefix)+area(suffix[k]))
		}
		prefix = grow(prefix, spots[k])
	}
	return result
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	// a picture must hold each spot whole, so it must hold its bounding square
	across, down := make([]box, n), make([]box, n)
	for i := range across {
		var r, x, y int
		fmt.Fscan(in, &r, &x, &y)
		across[i] = box{x - r, x + r, y - r, y + r}
		down[i] = box{y - r, y + r, x - r, x + r}
	}
	// two pictures that do not overlap are split by a vertical or a
	// horizontal line, and each can grow to 100 mm away from that line
	fmt.Println(min64(best(across), best(down)))
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min64(a, b int64) int64 {
	if a < b {
		return a
	}
	return b
}
