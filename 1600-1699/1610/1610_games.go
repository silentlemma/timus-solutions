package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	sc := bufio.NewScanner(os.Stdin)
	sc.Split(bufio.ScanWords)
	next := func() int {
		sc.Scan()
		v, _ := strconv.Atoi(sc.Text())
		return v
	}
	n, m, root := next(), next(), next()
	adj := make([][]int, n+1)
	for i := 0; i < m; i++ {
		k, prev := next(), next()
		for j := 1; j < k; j++ {
			v := next()
			adj[prev] = append(adj[prev], v)
			adj[v] = append(adj[v], prev)
			prev = v
		}
	}
	// depth-first search without recursion, so every other edge joins a
	// vertex to one of its ancestors
	parent := make([]int, n+1)
	depth := make([]int, n+1)
	pos := make([]int, n+1)
	for i := range depth {
		depth[i] = -1
	}
	order := []int{root}
	depth[root] = 0
	stack := []int{root}
	for len(stack) > 0 {
		v := stack[len(stack)-1]
		if pos[v] == len(adj[v]) {
			stack = stack[:len(stack)-1]
			continue
		}
		u := adj[v][pos[v]]
		pos[v]++
		if depth[u] < 0 {
			depth[u] = depth[v] + 1
			parent[u] = v
			order = append(order, u)
			stack = append(stack, u)
		}
	}
	// every non-tree edge closes a cycle with the tree path between its ends
	onCycle := make([]bool, n+1)   // the edge from v to its parent lies on a cycle
	cycles := make([][][]int, n+1) // cycles listed at their top vertex
	for v := 1; v <= n; v++ {
		for _, u := range adj[v] {
			if depth[u] < depth[v] && u != parent[v] {
				var members []int
				for x := v; x != u; x = parent[x] {
					onCycle[x] = true
					members = append(members, x)
				}
				cycles[u] = append(cycles[u], members)
			}
		}
	}
	// a tree edge to a child of value g is worth g + 1; a cycle fuses into
	// loops on its top vertex: one loop (worth 1) per edge, so its length
	// parity, together with everything hanging from its other vertices
	value := make([]int, n+1)
	for i := n - 1; i >= 0; i-- {
		v, g := order[i], 0
		for _, u := range adj[v] {
			if parent[u] == v && !onCycle[u] {
				g ^= value[u] + 1
			}
		}
		for _, members := range cycles[v] {
			g ^= (len(members) + 1) % 2 // a cycle has as many edges as vertices
			for _, x := range members {
				g ^= value[x]
			}
		}
		value[v] = g
	}
	if value[root] != 0 {
		fmt.Println("First")
	} else {
		fmt.Println("Second")
	}
}
