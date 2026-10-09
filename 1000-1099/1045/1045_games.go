package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, k int
	fmt.Fscan(in, &n, &k)
	adj := make([][]int, n+1)
	for i := 0; i+1 < n; i++ {
		var a, b int
		fmt.Fscan(in, &a, &b)
		adj[a] = append(adj[a], b)
		adj[b] = append(adj[b], a)
	}
	// the destroyed airports are exactly the ones on the way back to k, so a
	// move always goes down the tree rooted at k; a breadth-first order lists
	// parents before children
	parent := make([]int, n+1)
	parent[k] = -1
	order := []int{k}
	for i := 0; i < len(order); i++ {
		v := order[i]
		for _, w := range adj[v] {
			if w != parent[v] {
				parent[w] = v
				order = append(order, w)
			}
		}
	}
	// win[v]: the player to move at v wins, that is, some child is a loss
	win := make([]bool, n+1)
	for i := len(order) - 1; i >= 1; i-- {
		if !win[order[i]] {
			win[parent[order[i]]] = true
		}
	}
	best := 0
	for _, w := range adj[k] {
		if !win[w] && (best == 0 || w < best) {
			best = w
		}
	}
	if best == 0 {
		fmt.Println("First player loses")
	} else {
		fmt.Printf("First player wins flying to airport %d\n", best)
	}
}
