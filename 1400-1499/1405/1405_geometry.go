package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

const shortest, longest = 1.0, 50.0 // the allowed rope lengths
const eps = 1e-9

// bestPair: the largest a^2 + b^2 with 1 <= a <= topA, 1 <= b <= topB, a + b <= d, or -1.
func bestPair(topA, topB, d float64) float64 {
	if topA < shortest-eps || topB < shortest-eps || d < 2*shortest-eps {
		return -1
	}
	// a convex function is largest at a corner of the region
	corners := [][2]float64{{topA, topB}, {topA, shortest}, {shortest, topB},
		{topA, d - topA}, {d - topB, topB}, {d - shortest, shortest}, {shortest, d - shortest}}
	best := -1.0
	for _, c := range corners {
		a, b := c[0], c[1]
		if a >= shortest-eps && a <= topA+eps && b >= shortest-eps && b <= topB+eps && a+b <= d+eps {
			best = math.Max(best, a*a+b*b)
		}
	}
	return best
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	x, y, top := make([]float64, n), make([]float64, n), make([]float64, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(in, &x[i], &y[i])
		top[i] = longest
	}
	// the longest rope at each tree: up to the nearest other tree and 50 meters
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if j != i {
				top[i] = math.Min(top[i], math.Hypot(x[i]-x[j], y[i]-y[j]))
			}
		}
	}
	best := 0.0
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			best = math.Max(best, bestPair(top[i], top[j], math.Hypot(x[i]-x[j], y[i]-y[j])))
		}
	}
	fmt.Printf("%.4f\n", math.Pi*best)
}
