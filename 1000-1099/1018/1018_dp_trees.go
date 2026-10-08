package main

import "fmt"

type branch struct{ to, apples int }

var (
	adj [][]branch
	q   int
)

// solve: best[k] is the most apples on k branches kept in the subtree of v,
// all of them connected to v; the slice is only as long as k can go.
func solve(v, parent int) []int {
	best := []int{0}
	for _, e := range adj[v] {
		if e.to == parent {
			continue
		}
		sub := solve(e.to, v)
		size := len(best) + len(sub)
		if size > q+1 {
			size = q + 1
		}
		merged := make([]int, size)
		for i := range merged {
			merged[i] = -1
		}
		for i, a := range best {
			// taking j >= 1 branches on the child's side: its edge and j - 1 below
			for j := 0; j <= len(sub) && i+j < size; j++ {
				gain := 0
				if j > 0 {
					gain = e.apples + sub[j-1]
				}
				if a+gain > merged[i+j] {
					merged[i+j] = a + gain
				}
			}
		}
		best = merged
	}
	return best
}

func main() {
	var n int
	fmt.Scan(&n, &q)
	adj = make([][]branch, n+1)
	for i := 1; i < n; i++ {
		var a, b, apples int
		fmt.Scan(&a, &b, &apples)
		adj[a] = append(adj[a], branch{b, apples})
		adj[b] = append(adj[b], branch{a, apples})
	}
	fmt.Println(solve(1, 0)[q])
}
