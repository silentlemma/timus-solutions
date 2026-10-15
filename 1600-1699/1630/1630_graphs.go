package main

import (
	"bufio"
	"fmt"
	"os"
)

const maxClique = 4 // four points pairwise 1 apart fit in space, five do not

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, m int
	if _, err := fmt.Fscan(in, &n, &m); err != nil {
		return
	}
	parent := make([]int, n)
	for v := range parent {
		parent[v] = v
	}
	find := func(v int) int {
		for parent[v] != v {
			parent[v] = parent[parent[v]]
			v = parent[v]
		}
		return v
	}
	degree, ends := make([]int, n), make([]int, m)
	for i := 0; i < m; i++ {
		var u, v int
		fmt.Fscan(in, &u, &v)
		u--
		v--
		degree[u]++
		degree[v]++
		ends[i] = u
		parent[find(u)] = find(v)
	}
	size, edges, widest := make([]int, n), make([]int, n), make([]int, n)
	for v := 0; v < n; v++ {
		root := find(v)
		size[root]++
		if degree[v] > widest[root] {
			widest[root] = degree[v]
		}
	}
	for _, u := range ends {
		edges[find(u)]++
	}
	// every component must be a path or a clique of at most four vertices
	for root := 0; root < n; root++ {
		k := size[root]
		if k == 0 {
			continue
		}
		path := edges[root] == k-1 && widest[root] <= 2
		clique := edges[root] == k*(k-1)/2 && k <= maxClique
		if !path && !clique {
			fmt.Println("Unlucky Petr")
			return
		}
	}
	fmt.Println("Luck is possible")
}
