package main

import (
	"bufio"
	"fmt"
	"os"
)

func gcd(a, b int) int {
	if a < 0 {
		a = -a
	}
	if b < 0 {
		b = -b
	}
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	x := make([]int, n)
	y := make([]int, n)
	for i := range x {
		fmt.Fscan(in, &x[i], &y[i])
	}
	best := 2
	if n < best {
		best = n
	}
	for i := 0; i < n; i++ {
		// the points on one line through point i have the same reduced direction
		count := map[[2]int]int{}
		for j := i + 1; j < n; j++ {
			dx, dy := x[j]-x[i], y[j]-y[i]
			g := gcd(dx, dy)
			dx, dy = dx/g, dy/g
			// opposite directions are the same line
			if dx < 0 || (dx == 0 && dy < 0) {
				dx, dy = -dx, -dy
			}
			key := [2]int{dx, dy}
			count[key]++
			if count[key]+1 > best {
				best = count[key] + 1
			}
		}
	}
	fmt.Println(best)
}
