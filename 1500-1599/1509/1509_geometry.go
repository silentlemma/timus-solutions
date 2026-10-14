package main

import (
	"bufio"
	"fmt"
	"math/cmplx"
	"os"
)

const (
	most    = 6    // dots in one square
	full    = 4    // from four dots on, all corners of the inner square are used
	quarter = 0.25 // the inner square's corners are L / 4 from the centre

	smallest, largest = 1.0, 100.0
	eps               = 2e-3 // the coordinates are given to 1e-4, and a fit spreads that error
)

// square returns the dots of a square with k dots around centre, for L = 1,
// with the domino lying along the x axis.
func square(k int, centre complex128) []complex128 {
	q := quarter
	var dots []complex128
	if k >= 2 {
		dots = append(dots, complex(-q, -q), complex(q, q))
	}
	if k >= full {
		dots = append(dots, complex(q, -q), complex(-q, q))
	}
	if k == most {
		dots = append(dots, complex(0, -q), complex(0, q)) // beside the long sides
	}
	if k%2 == 1 {
		dots = append(dots, 0)
	}
	for i := range dots {
		dots[i] += centre
	}
	return dots
}

// fits tells whether a similarity, maybe mirrored, with scale in the allowed
// range takes the template onto the given dots.
func fits(template, given []complex128) bool {
	g0, g1 := given[0], given[0]
	for _, g := range given {
		if cmplx.Abs(g-g0) > cmplx.Abs(g1-g0) {
			g1 = g
		}
	}
	for mirror := 0; mirror < 2; mirror++ {
		pts := make([]complex128, len(template))
		for i, t := range template {
			pts[i] = t
			if mirror == 1 {
				pts[i] = cmplx.Conj(t)
			}
		}
		for _, a := range pts {
			for _, b := range pts {
				if a == b {
					continue
				}
				turn := (g1 - g0) / (b - a) // rotation times the scale L
				if s := cmplx.Abs(turn); s < smallest-eps || s > largest+eps {
					continue
				}
				hit := map[int]bool{}
				ok := true
				for _, t := range pts {
					image := g0 + (t-a)*turn
					near := 0
					for i := range given {
						if cmplx.Abs(given[i]-image) < cmplx.Abs(given[near]-image) {
							near = i
						}
					}
					if cmplx.Abs(given[near]-image) > eps {
						ok = false
						break
					}
					hit[near] = true
				}
				if ok && len(hit) == len(given) {
					return true
				}
			}
		}
	}
	return false
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	given := make([]complex128, n)
	for i := range given {
		var x, y float64
		fmt.Fscan(in, &x, &y)
		given[i] = complex(x, y)
	}
	for a := 0; a <= most; a++ {
		b := n - a
		if a > b || b > most {
			continue
		}
		template := append(square(a, 0), square(b, 1)...)
		if n == 1 || fits(template, given) {
			fmt.Println(a, b)
		}
	}
}
