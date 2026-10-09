package main

import (
	"bufio"
	"fmt"
	"os"
)

const kinds = 3

func main() {
	in := bufio.NewReader(os.Stdin)
	var length, price [kinds]int64
	for k := range length {
		fmt.Fscan(in, &length[k])
	}
	for k := range price {
		fmt.Fscan(in, &price[k])
	}
	var n, a, b int
	fmt.Fscan(in, &n, &a, &b)
	x := make([]int64, n+1)
	for i := 2; i <= n; i++ {
		fmt.Fscan(in, &x[i])
	}
	if a > b {
		a, b = b, a
	}
	// cost[i]: the cheapest way from a to i; it never decreases along the
	// line, so for every kind of ticket the farthest start in reach is best
	cost := make([]int64, n+1)
	from := [kinds]int{a, a, a}
	for i := a + 1; i <= b; i++ {
		cost[i] = -1
		for k := 0; k < kinds; k++ {
			for x[i]-x[from[k]] > length[k] {
				from[k]++
			}
			if from[k] < i && (cost[i] < 0 || cost[from[k]]+price[k] < cost[i]) {
				cost[i] = cost[from[k]] + price[k]
			}
		}
	}
	fmt.Println(cost[b])
}
