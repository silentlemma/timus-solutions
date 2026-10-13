package main

import (
	"bufio"
	"fmt"
	"os"
)

type pipe struct{ to, profit int }

func main() {
	reader := bufio.NewReader(os.Stdin)
	var n, m int
	fmt.Fscan(reader, &n, &m)
	out := make([][]pipe, n+1)
	indeg := make([]int, n+1)
	for i := 0; i < m; i++ {
		var a, b, c int
		fmt.Fscan(reader, &a, &b, &c)
		out[a] = append(out[a], pipe{b, c})
		indeg[b]++
	}
	var s, f int
	fmt.Fscan(reader, &s, &f)
	// the network has no cycles: take the stations in topological order and
	// keep the best profit of a route from S to each of them, -1 if unreachable
	best := make([]int, n+1)
	for i := range best {
		best[i] = -1
	}
	best[s] = 0
	var order []int
	for v := 1; v <= n; v++ {
		if indeg[v] == 0 {
			order = append(order, v)
		}
	}
	for k := 0; k < len(order); k++ {
		v := order[k]
		for _, p := range out[v] {
			if best[v] >= 0 && best[v]+p.profit > best[p.to] {
				best[p.to] = best[v] + p.profit
			}
			indeg[p.to]--
			if indeg[p.to] == 0 {
				order = append(order, p.to)
			}
		}
	}
	if best[f] < 0 {
		fmt.Println("No solution")
	} else {
		fmt.Println(best[f])
	}
}
