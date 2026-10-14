package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

const (
	dim    = 3 // x, y, z, then vx, vy, vz
	coords = 2 * dim
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	var d float64
	if _, err := fmt.Fscan(in, &n, &d); err != nil {
		return
	}
	obj := make([][coords]float64, n)
	for i := range obj {
		for k := range obj[i] {
			fmt.Fscan(in, &obj[i][k])
		}
	}
	best := math.Inf(1)
	bestA, bestB := -1, -1
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			p, q := obj[i], obj[j]
			// |p + v t| = d for the relative position p and velocity v:
			// (v.v) t^2 + 2 (p.v) t + (p.p - d^2) = 0
			a, b, c := 0.0, 0.0, -d*d
			for k := 0; k < dim; k++ {
				dp, dv := q[k]-p[k], q[dim+k]-p[dim+k]
				a += dv * dv
				b += dp * dv
				c += dp * dp
			}
			if a == 0 {
				continue
			}
			disc := b*b - a*c
			if disc < 0 {
				continue
			}
			// the earlier root; the pair starts apart, so a negative one
			// means they are moving away
			t := (-b - math.Sqrt(disc)) / a
			if t >= 0 && t < best {
				best, bestA, bestB = t, i+1, j+1
			}
		}
	}
	if bestA < 0 {
		fmt.Println("OK")
	} else {
		fmt.Printf("ALARM!\n%.3f %d %d\n", best, bestA, bestB)
	}
}
