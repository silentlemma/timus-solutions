package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	step  = 2   // columns two apart keep every pair of points farther than 1
	limit = 999 // the leftmost column, so that 1000 columns fit in [-999, 999]
)

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var n int
	fmt.Fscan(in, &n)
	adj := make([][]int, n+1)
	for i := 0; i < n-1; i++ {
		var a, b int
		fmt.Fscan(in, &a, &b)
		adj[a] = append(adj[a], b)
		adj[b] = append(adj[b], a)
	}
	// column = preorder index, row = depth: the subtrees of the vertices on
	// one row take disjoint ranges of columns, so no two wires cross
	x, y := make([]int, n+1), make([]int, n+1)
	seen := make([]bool, n+1)
	seen[1] = true
	stack, order := []int{1}, 0
	for len(stack) > 0 {
		v := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		x[v] = order*step - limit
		order++
		for k := len(adj[v]) - 1; k >= 0; k-- {
			u := adj[v][k]
			if !seen[u] {
				seen[u] = true
				y[u] = y[v] + 1
				stack = append(stack, u)
			}
		}
	}
	for v := 1; v <= n; v++ {
		fmt.Fprintln(out, x[v], y[v])
	}
}
