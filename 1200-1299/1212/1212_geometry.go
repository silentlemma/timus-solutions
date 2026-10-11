package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

// zone holds the cells a ship may not use: rows top..bottom, columns
// left..right.
type zone struct{ top, bottom, left, right int64 }

// countLines counts places for a ship lying along the rows of a rows x cols
// board.
func countLines(rows, cols int64, zones []zone, k int64) int64 {
	set := map[int64]bool{1: true, rows + 1: true}
	for _, z := range zones {
		for _, e := range []int64{z.top, z.bottom + 1} {
			if e > 1 && e <= rows {
				set[e] = true
			}
		}
	}
	var cuts []int64
	for e := range set {
		cuts = append(cuts, e)
	}
	sort.Slice(cuts, func(a, b int) bool { return cuts[a] < cuts[b] })
	total := int64(0)
	// rows between two cuts meet the same zones, so they count the same
	for i := 0; i+1 < len(cuts); i++ {
		top := cuts[i]
		var spans []zone
		for _, z := range zones {
			if z.top <= top && top <= z.bottom {
				spans = append(spans, z)
			}
		}
		sort.Slice(spans, func(a, b int) bool { return spans[a].left < spans[b].left })
		spans = append(spans, zone{left: cols + 1, right: cols + 1})
		free, start := int64(0), int64(1)
		for _, s := range spans {
			if s.left > start && s.left-start-k+1 > 0 {
				free += s.left - start - k + 1
			}
			if s.right+1 > start {
				start = s.right + 1
			}
		}
		total += free * (cuts[i+1] - top)
	}
	return total
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, m, k int64
	var ships int
	fmt.Fscan(in, &n, &m, &ships)
	zones := make([]zone, 0, ships)
	for i := 0; i < ships; i++ {
		var col, row, size int64
		var way string
		fmt.Fscan(in, &col, &row, &size, &way)
		bottom, right := row, col+size-1
		if way == "V" {
			bottom, right = row+size-1, col
		}
		// no other ship may touch this one, even at a corner
		zones = append(zones, zone{row - 1, bottom + 1, col - 1, right + 1})
	}
	fmt.Fscan(in, &k)
	total := countLines(n, m, zones, k)
	if k > 1 {
		flipped := make([]zone, len(zones))
		for i, z := range zones {
			flipped[i] = zone{z.left, z.right, z.top, z.bottom}
		}
		total += countLines(m, n, flipped, k)
	}
	fmt.Println(total)
}
