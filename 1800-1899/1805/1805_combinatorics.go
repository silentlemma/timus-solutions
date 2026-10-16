package main

import (
	"fmt"
	"strings"
)

const turns = 4

func main() {
	var n int
	var k uint64
	if _, err := fmt.Scan(&n, &k); err != nil {
		return
	}
	// the four cells a quarter turn takes into each other form an orbit; a
	// grille opens exactly one cell of every orbit
	orbit := make([][]int, n)
	for r := range orbit {
		orbit[r] = make([]int, n)
		for c := range orbit[r] {
			orbit[r][c] = -1
		}
	}
	orbits := 0
	for r := 0; r < n; r++ {
		for c := 0; c < n; c++ {
			if orbit[r][c] != -1 {
				continue
			}
			rr, cc := r, c
			for t := 0; t < turns; t++ {
				orbit[rr][cc] = orbits
				rr, cc = cc, n-1-rr
			}
			orbits++
		}
	}
	// left[o]: cells of orbit o not passed yet, -1 once its window is cut
	left := make([]int, orbits)
	for o := range left {
		left[o] = turns
	}
	var out strings.Builder
	for r := 0; r < n; r++ {
		for c := 0; c < n; c++ {
			o := orbit[r][c]
			if left[o] == -1 {
				out.WriteByte('0')
				continue
			}
			left[o]--
			// grilles with a 0 here: every open orbit picks one of its
			// remaining cells
			withZero := uint64(1)
			for _, rest := range left {
				if rest != -1 {
					withZero *= uint64(rest)
				}
			}
			if k <= withZero {
				out.WriteByte('0')
			} else {
				k -= withZero
				out.WriteByte('1')
				left[o] = -1
			}
		}
		out.WriteByte('\n')
	}
	fmt.Print(out.String())
}
