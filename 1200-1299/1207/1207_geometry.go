package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	x, y := make([]int64, n), make([]int64, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(in, &x[i], &y[i])
	}
	// the lowest point (the leftmost of the lowest) sees all others within
	// half a turn, so they can be sorted by angle with cross products
	pivot := 0
	for i := 1; i < n; i++ {
		if y[i] < y[pivot] || (y[i] == y[pivot] && x[i] < x[pivot]) {
			pivot = i
		}
	}
	others := make([]int, 0, n-1)
	for i := 0; i < n; i++ {
		if i != pivot {
			others = append(others, i)
		}
	}
	px, py := x[pivot], y[pivot]
	sort.Slice(others, func(a, b int) bool {
		i, j := others[a], others[b]
		return (x[i]-px)*(y[j]-py)-(y[i]-py)*(x[j]-px) > 0
	})
	// the middle one leaves (n - 2) / 2 points on each side of the line
	fmt.Println(pivot+1, others[(n-2)/2]+1)
}
