package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, m int
	fmt.Fscan(in, &n, &m)
	// g[a][b]: total conductance between two nodes
	g := make([][]float64, n)
	for i := range g {
		g[i] = make([]float64, n)
	}
	for i := 0; i < m; i++ {
		var a, b, r int
		fmt.Fscan(in, &a, &b, &r)
		g[a-1][b-1] += 1 / float64(r)
		g[b-1][a-1] += 1 / float64(r)
	}
	// nodes cut off from node 1 carry no current and would make the
	// system singular
	seen := make([]bool, n)
	seen[0] = true
	stack := []int{0}
	for len(stack) > 0 {
		u := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		for v := 0; v < n; v++ {
			if g[u][v] > 0 && !seen[v] {
				seen[v] = true
				stack = append(stack, v)
			}
		}
	}
	var inner []int
	for v := 1; v < n-1; v++ {
		if seen[v] {
			inner = append(inner, v)
		}
	}
	// Kirchhoff at each inner node with potential 1 at node 1, 0 at node N
	k := len(inner)
	a := make([][]float64, k)
	for i, u := range inner {
		a[i] = make([]float64, k+1)
		for v := 0; v < n; v++ {
			a[i][i] += g[u][v]
		}
		for j, v := range inner {
			a[i][j] -= g[u][v]
		}
		a[i][k] = g[u][0]
	}
	for c := 0; c < k; c++ {
		p := c
		for r := c + 1; r < k; r++ {
			if math.Abs(a[r][c]) > math.Abs(a[p][c]) {
				p = r
			}
		}
		a[c], a[p] = a[p], a[c]
		for r := 0; r < k; r++ {
			if r != c && a[r][c] != 0 {
				f := a[r][c] / a[c][c]
				for j := c; j <= k; j++ {
					a[r][j] -= f * a[c][j]
				}
			}
		}
	}
	volt := make([]float64, n)
	volt[0] = 1
	for i, u := range inner {
		volt[u] = a[i][k] / a[i][i]
	}
	current := 0.0
	for v := 1; v < n; v++ {
		current += g[0][v] * (1 - volt[v])
	}
	fmt.Printf("%.2f\n", 1/current)
}
