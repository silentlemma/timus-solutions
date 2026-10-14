package main

import (
	"bufio"
	"fmt"
	"os"
)

type edge struct{ a, b int }

var n int
var adj [][]int

// bfs returns the distances from the nearest source and the edges of a tree
// of shortest paths that grows from the sources
func bfs(sources []int) ([]int, []edge) {
	dist := make([]int, n)
	for i := range dist {
		dist[i] = -1
	}
	var tree []edge
	queue := append([]int{}, sources...)
	for _, s := range sources {
		dist[s] = 0
	}
	for head := 0; head < len(queue); head++ {
		v := queue[head]
		for _, u := range adj[v] {
			if dist[u] < 0 {
				dist[u] = dist[v] + 1
				tree = append(tree, edge{v, u})
				queue = append(queue, u)
			}
		}
	}
	return dist, tree
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var m int
	fmt.Fscan(in, &n, &m)
	adj = make([][]int, n)
	edges := make([]edge, m)
	for i := range edges {
		fmt.Fscan(in, &edges[i].a, &edges[i].b)
		edges[i].a--
		edges[i].b--
		adj[edges[i].a] = append(adj[edges[i].a], edges[i].b)
		adj[edges[i].b] = append(adj[edges[i].b], edges[i].a)
	}
	dist := make([][]int, n)
	for v := range dist {
		dist[v], _ = bfs([]int{v})
	}
	// the middle of a tree of least diameter is a node or the middle of an edge, and
	// a tree of shortest paths from there has diameter 2 r or 2 r + 1 for the
	// largest distance r from it, and no tree can do better
	best, centre := -1, []int{}
	for v := 0; v < n; v++ {
		far := 0
		for _, d := range dist[v] {
			if d > far {
				far = d
			}
		}
		if best < 0 || 2*far < best {
			best, centre = 2*far, []int{v}
		}
	}
	for _, e := range edges {
		far := 0
		for w := 0; w < n; w++ {
			d := dist[e.a][w]
			if dist[e.b][w] < d {
				d = dist[e.b][w]
			}
			if d > far {
				far = d
			}
		}
		if 2*far+1 < best {
			best, centre = 2*far+1, []int{e.a, e.b}
		}
	}
	_, tree := bfs(centre)
	if len(centre) > 1 {
		tree = append(tree, edge{centre[0], centre[1]})
	}
	for _, e := range tree {
		fmt.Fprintln(out, e.a+1, e.b+1)
	}
}
