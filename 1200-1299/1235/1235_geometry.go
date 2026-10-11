package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, w, h int
	fmt.Fscan(in, &n, &w, &h)
	x, y := make([]int, n), make([]int, n)
	for i := range x {
		fmt.Fscan(in, &x[i], &y[i])
	}
	// a largest square slides left and down until its sides meet a tree or
	// the park border, so its corner has x = 0 or a tree x and y = 0 or a tree y
	xs, ys := append([]int{0}, x...), append([]int{0}, y...)
	bestP, bestQ, bestL := 0, 0, 0
	for _, p := range xs {
		for _, q := range ys {
			side := min(w-p, h-q)
			// a tree up and to the right of the corner is inside unless the
			// side stops at its larger distance
			for i := range x {
				if x[i] > p && y[i] > q {
					side = min(side, max(x[i]-p, y[i]-q))
				}
			}
			if side > bestL {
				bestP, bestQ, bestL = p, q, side
			}
		}
	}
	fmt.Println(bestP, bestQ, bestL)
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
