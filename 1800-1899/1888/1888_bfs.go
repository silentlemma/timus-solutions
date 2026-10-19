package main

import (
	"bufio"
	"fmt"
	"os"
)

const longest = 50 // experience is from 1 to 50 years

var (
	p   int
	adj [][]int
)

// distances from start, -1 outside its component
func distances(start int) []int {
	dist := make([]int, p+1)
	for i := range dist {
		dist[i] = -1
	}
	dist[start] = 0
	queue := []int{start}
	for head := 0; head < len(queue); head++ {
		u := queue[head]
		for _, v := range adj[u] {
			if dist[v] < 0 {
				dist[v] = dist[u] + 1
				queue = append(queue, v)
			}
		}
	}
	return dist
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(reader, &n, &p)
	adj = make([][]int, p+1)
	for k := 0; k < n; k++ {
		var a, b int
		fmt.Fscan(reader, &a, &b)
		adj[a] = append(adj[a], b)
		adj[b] = append(adj[b], a)
	}
	// the two pilots of a flight differ by exactly one year, so a component
	// must be bipartite; within it no two pilots differ by more than their
	// distance, and BFS layers from one end of a diameter reach it
	seen := make([]bool, p+1)
	roots := []int{}
	for s := 1; s <= p; s++ {
		if seen[s] {
			continue
		}
		dist := distances(s)
		for u := 1; u <= p; u++ {
			if dist[u] < 0 {
				continue
			}
			seen[u] = true
			for _, v := range adj[u] {
				if (dist[u]-dist[v])%2 == 0 {
					fmt.Println(-1)
					return
				}
			}
		}
		roots = append(roots, s)
	}
	years := make([]int, p+1)
	if len(roots) == 1 {
		spread := -1
		for s := 1; s <= p; s++ {
			dist := distances(s)
			far := 0
			for u := 1; u <= p; u++ {
				if dist[u] > far {
					far = dist[u]
				}
			}
			if far > spread {
				spread = far
				for u := 1; u <= p; u++ {
					years[u] = 1 + dist[u]
				}
			}
		}
		fmt.Println(spread)
	} else {
		// separate groups: one alternates 1 and 2, the others 49 and 50
		for k, root := range roots {
			dist := distances(root)
			for u := 1; u <= p; u++ {
				if dist[u] < 0 {
					continue
				}
				if k == 0 {
					years[u] = 1 + dist[u]%2
				} else {
					years[u] = longest - dist[u]%2
				}
			}
		}
		fmt.Println(longest - 1)
	}
	for u := 1; u <= p; u++ {
		if u > 1 {
			fmt.Print(" ")
		}
		fmt.Print(years[u])
	}
	fmt.Println()
}
