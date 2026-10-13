package main

import (
	"fmt"
	"math"
)

const gravity = 10

func main() {
	var n, m int
	fmt.Scan(&n, &m)
	// the speed at depth d is sqrt(2 g d), whatever the way down was
	speed := make([]float64, m+1)
	for d := range speed {
		speed[d] = math.Sqrt(2 * gravity * float64(d))
	}
	// best holds the least time to reach each depth and distance to the left,
	// where a board with constant acceleration takes 2 L / (v1 + v2)
	best := make([][]float64, m+1)
	for d := range best {
		best[d] = make([]float64, n+1)
		for x := range best[d] {
			best[d][x] = math.Inf(1)
		}
	}
	best[0][0] = 0
	for d := 1; d <= m; d++ {
		for e := 0; e < d; e++ {
			vs := speed[d] + speed[e]
			for x := 0; x <= n; x++ {
				if math.IsInf(best[e][x], 1) {
					continue
				}
				for y := x; y <= n; y++ {
					c := best[e][x] + 2*math.Hypot(float64(y-x), float64(d-e))/vs
					if c < best[d][y] {
						best[d][y] = c
					}
				}
			}
		}
	}
	fmt.Printf("%.4f\n", best[m][n])
}
