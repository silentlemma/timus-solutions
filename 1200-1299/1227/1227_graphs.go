package main

import (
	"bufio"
	"fmt"
	"os"
)

type road struct {
	to  int
	len int64
}

var (
	m      int
	parent []int
	adj    [][]road
)

func find(v int) int {
	for parent[v] != v {
		parent[v] = parent[parent[v]]
		v = parent[v]
	}
	return v
}

// distances returns the distances from start within its tree, -1 elsewhere.
func distances(start int) []int64 {
	dist := make([]int64, m+1)
	for i := range dist {
		dist[i] = -1
	}
	dist[start] = 0
	stack := []int{start}
	for len(stack) > 0 {
		v := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		for _, e := range adj[v] {
			if dist[e.to] < 0 {
				dist[e.to] = dist[v] + e.len
				stack = append(stack, e.to)
			}
		}
	}
	return dist
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	var s int64
	fmt.Fscan(in, &m, &n, &s)
	parent = make([]int, m+1)
	adj = make([][]road, m+1)
	for v := range parent {
		parent[v] = v
	}
	for i := 0; i < n; i++ {
		var p, q int
		var r int64
		fmt.Fscan(in, &p, &q, &r)
		a, b := find(p), find(q)
		if a == b {
			// a cycle, a loop or a second road: drive round it as long as needed
			fmt.Println("YES")
			return
		}
		parent[a] = b
		adj[p] = append(adj[p], road{q, r})
		adj[q] = append(adj[q], road{p, r})
	}
	// a forest: the longest route is a diameter of one of its trees
	best := int64(0)
	seen := make([]bool, m+1)
	for v := 1; v <= m; v++ {
		if seen[v] {
			continue
		}
		d := distances(v)
		end := v
		for u := 1; u <= m; u++ {
			if d[u] >= 0 {
				seen[u] = true
				if d[u] > d[end] {
					end = u
				}
			}
		}
		for _, x := range distances(end) {
			if x > best {
				best = x
			}
		}
	}
	if best >= s {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}
}
