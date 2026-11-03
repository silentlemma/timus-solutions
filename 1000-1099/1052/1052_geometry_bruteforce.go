package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	x, y := make([]int, n), make([]int, n)
	for i := range x {
		fmt.Fscan(in, &x[i], &y[i])
	}
	best := 2
	// Every line through two input points is tried; cross products are exact.
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			dx, dy, count := x[j]-x[i], y[j]-y[i], 0
			for k := 0; k < n; k++ {
				if (x[k]-x[i])*dy == (y[k]-y[i])*dx {
					count++
				}
			}
			if count > best {
				best = count
			}
			if best == n {
				fmt.Println(best)
				return
			}
		}
	}
	fmt.Println(best)
}
