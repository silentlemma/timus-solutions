package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, k, m int
	fmt.Fscan(in, &n, &k, &m) // the bridges themselves do not matter
	parent := make([]int, n+1)
	for i := range parent {
		parent[i] = i
	}
	find := func(x int) int {
		for parent[x] != x {
			parent[x] = parent[parent[x]]
			x = parent[x]
		}
		return x
	}
	// tunnels are free; every bridge joins two of the remaining groups
	groups := n
	for i := 0; i < k; i++ {
		var a, b int
		fmt.Fscan(in, &a, &b)
		if a, b = find(a), find(b); a != b {
			parent[a] = b
			groups--
		}
	}
	fmt.Println(groups - 1)
}
