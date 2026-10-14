package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	if a < 0 {
		return -a
	}
	return a
}

const half = 0.5 // rounds to the nearest mile

type dir struct{ dx, dy int }

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	if _, err := fmt.Fscan(in, &n); err != nil {
		return
	}
	xs := make([]int, n)
	ys := make([]int, n)
	for i := range xs {
		fmt.Fscan(in, &xs[i], &ys[i])
	}
	total := 0.0
	for i := 0; i < n; i++ {
		// the farthest city in each reduced direction from city i, in steps
		far := make(map[dir]int)
		for j := 0; j < n; j++ {
			if j == i {
				continue
			}
			dx, dy := xs[j]-xs[i], ys[j]-ys[i]
			g := gcd(dx, dy)
			d := dir{dx / g, dy / g}
			if g > far[d] {
				far[d] = g
			}
		}
		for d, steps := range far {
			// city i ends the road in this direction when nothing lies behind it
			if _, ok := far[dir{-d.dx, -d.dy}]; !ok {
				total += float64(steps) * math.Hypot(float64(d.dx), float64(d.dy))
			}
		}
	}
	// every road is found from both of its ends
	fmt.Println(int64(math.Floor(total/2 + half)))
}
