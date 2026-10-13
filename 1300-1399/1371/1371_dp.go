package main

import (
	"bufio"
	"fmt"
	"os"
)

type edge struct{ to, cost int }

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	adj := make([][]edge, n+1)
	for i := 0; i < n-1; i++ {
		var a, b, c int
		fmt.Fscan(in, &a, &b, &c)
		adj[a] = append(adj[a], edge{b, c})
		adj[b] = append(adj[b], edge{a, c})
	}
	// an edge with s branches on one side carries the s (n - s) pairs that
	// it separates; sizes come from a parents-first order read backwards
	parent, cost := make([]int, n+1), make([]int64, n+1)
	parent[1] = -1
	order := []int{1}
	for i := 0; i < len(order); i++ {
		v := order[i]
		for _, e := range adj[v] {
			if e.to != parent[v] {
				parent[e.to], cost[e.to] = v, int64(e.cost)
				order = append(order, e.to)
			}
		}
	}
	size := make([]int64, n+1)
	for i := range size {
		size[i] = 1
	}
	total := int64(0)
	for i := len(order) - 1; i > 0; i-- {
		v := order[i]
		size[parent[v]] += size[v]
		total += cost[v] * size[v] * (int64(n) - size[v])
	}
	// every pair is counted in both directions
	fmt.Printf("%.4f\n", 2*float64(total)/(float64(n)*float64(n-1)))
}
