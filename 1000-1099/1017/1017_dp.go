package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	// ways[s]: sets of distinct step sizes, each used at most once, summing
	// to s; sizes are added one by one, going over s downwards
	ways := make([]int64, n+1)
	ways[0] = 1
	for size := 1; size <= n; size++ {
		for s := n; s >= size; s-- {
			ways[s] += ways[s-size]
		}
	}
	// a staircase needs at least two steps: drop the single step of n cubes
	fmt.Println(ways[n] - 1)
}
