package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	adj                   [][]int
	matchLeft, matchRight []int
	stamp                 []int
	round                 int
)

// Kuhn's augmenting search on the doubled graph: left copies and right
// copies of the canoeists, adj[u] the right neighbours of left u
func augment(u int) bool {
	for _, v := range adj[u] {
		if stamp[v] == round {
			continue
		}
		stamp[v] = round
		if matchRight[v] < 0 || augment(matchRight[v]) {
			matchLeft[u] = v
			matchRight[v] = u
			return true
		}
	}
	return false
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, k, m int
	if _, err := fmt.Fscan(in, &n, &k, &m); err != nil {
		return
	}
	adj = make([][]int, n)
	for i := 0; i < m; i++ {
		var a, b int
		fmt.Fscan(in, &a, &b)
		adj[a-1] = append(adj[a-1], b-1)
		adj[b-1] = append(adj[b-1], a-1)
	}
	// each crew must get at least k between its two members; this linear
	// program has a half-integral optimum, k/2 for each copy of a canoeist
	// in a minimum vertex cover of the doubled bipartite graph
	matchLeft, matchRight, stamp = make([]int, n), make([]int, n), make([]int, n)
	for i := 0; i < n; i++ {
		matchLeft[i], matchRight[i], stamp[i] = -1, -1, -1
	}
	for u := 0; u < n; u++ {
		augment(u)
		round++
	}
	// Konig: left copies unreachable from free left copies by alternating
	// paths, and right copies reachable, form a minimum cover
	seenLeft, seenRight := make([]bool, n), make([]bool, n)
	var queue []int
	for u := 0; u < n; u++ {
		if matchLeft[u] < 0 {
			seenLeft[u] = true
			queue = append(queue, u)
		}
	}
	for i := 0; i < len(queue); i++ {
		for _, v := range adj[queue[i]] {
			if seenRight[v] {
				continue
			}
			seenRight[v] = true
			if w := matchRight[v]; w >= 0 && !seenLeft[w] {
				seenLeft[w] = true
				queue = append(queue, w)
			}
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for v := 0; v < n; v++ {
		copies := 0
		if !seenLeft[v] {
			copies++
		}
		if seenRight[v] {
			copies++
		}
		fmt.Fprintf(out, "%.1f\n", float64(copies*k)/2)
	}
}
