package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	corners     = 4
	tetrahedron = 6 // a corner with legs a, b, c cuts off abc/6
)

func volume(side int64, h []int64) string {
	// the surface is a plane, so the levels at opposite corners add up to
	// the same sum; a sensor reads max(0, level), and 0 hides the level
	dry, at := 0, -1
	var diagonal [2]int64
	var hidden [2]bool
	var total int64
	for i, v := range h {
		diagonal[i%2] += v
		total += v
		if v == 0 {
			dry++
			at = i
			hidden[i%2] = true
		}
	}
	area := float64(side) * float64(side)
	switch dry {
	case corners:
		return "0.000000"
	case 0:
		if diagonal[0] != diagonal[1] {
			return "error"
		}
		return fmt.Sprintf("%.6f", area*float64(total)/corners)
	case 1:
		left, far := h[(at+1)%corners], h[(at+2)%corners]
		right := h[(at+corners-1)%corners]
		x := left + right - far
		if x > 0 {
			return "error"
		}
		// the plane dips below the bottom at the dry corner in a tetrahedron
		// with legs -x up and -x/(left - x), -x/(right - x) along the edges,
		// so that much negative water is added back
		dip := -float64(x)
		level := float64(total+x)/corners +
			dip*dip*dip/(tetrahedron*float64(left-x)*float64(right-x))
		return fmt.Sprintf("%.6f", area*level)
	}
	// two or more hidden levels: they only have to be at most 0 and keep
	// the two diagonal sums equal, and when that is possible they can move
	if hidden[0] && hidden[1] {
		return "ambiguous"
	}
	low := 1
	if hidden[0] {
		low = 0
	}
	if diagonal[1-low] > diagonal[low] {
		return "error"
	}
	return "ambiguous"
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var t int
	if _, err := fmt.Fscan(in, &t); err != nil {
		return
	}
	for ; t > 0; t-- {
		var side int64
		h := make([]int64, corners)
		fmt.Fscan(in, &side)
		for i := range h {
			fmt.Fscan(in, &h[i])
		}
		fmt.Fprintln(out, volume(side, h))
	}
}
