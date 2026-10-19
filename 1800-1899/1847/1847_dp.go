package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	xs, ys := make([]float64, n), make([]float64, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(in, &xs[i], &ys[i])
	}
	adjacent := make([][]int, n)
	for k := 0; k < n-1; k++ {
		var a, b int
		fmt.Fscan(in, &a, &b)
		adjacent[a-1] = append(adjacent[a-1], b-1)
		adjacent[b-1] = append(adjacent[b-1], a-1)
	}
	order, parent := []int{0}, make([]int, n)
	parent[0] = -1
	for i := 0; i < len(order); i++ {
		u := order[i]
		for _, v := range adjacent[u] {
			if v != parent[u] {
				parent[v] = u
				order = append(order, v)
			}
		}
	}
	far := func(a, b int) float64 { return math.Hypot(xs[a]-xs[b], ys[a]-ys[b]) }
	inf := math.Inf(1)
	// the walk through a subtree starts at its root and ends at one of its
	// leaves: ends[u] lists them, cost[u] the shortest walk ending at each
	ends, cost := make([][]int, n), make([][]float64, n)
	for i := n - 1; i >= 0; i-- {
		u := order[i]
		var children []int
		for _, v := range adjacent[u] {
			if v != parent[u] {
				children = append(children, v)
			}
		}
		if len(children) == 0 {
			ends[u], cost[u] = []int{u}, []float64{0}
			continue
		}
		k := len(children)
		// link[a][b]: leave child a at its best end and fly to child b
		link := make([][]float64, k)
		for a := range link {
			link[a] = make([]float64, k)
			e, c := ends[children[a]], cost[children[a]]
			for b := range link[a] {
				link[a][b] = inf
				for j := range e {
					link[a][b] = math.Min(link[a][b], c[j]+far(e[j], children[b]))
				}
			}
		}
		// enter[m][b]: the children in mask m are done and b, in m, came last
		enter := make([][]float64, 1<<k)
		for m := range enter {
			enter[m] = make([]float64, k)
			for b := range enter[m] {
				enter[m][b] = inf
			}
		}
		for b := 0; b < k; b++ {
			enter[1<<b][b] = far(u, children[b])
		}
		for m := 1; m < 1<<k; m++ {
			for a := 0; a < k; a++ {
				if enter[m][a] == inf {
					continue
				}
				for b := 0; b < k; b++ {
					if m>>b&1 == 0 {
						next := &enter[m|1<<b][b]
						*next = math.Min(*next, enter[m][a]+link[a][b])
					}
				}
			}
		}
		full := enter[1<<k-1]
		for b, v := range children {
			for j, e := range ends[v] {
				ends[u] = append(ends[u], e)
				cost[u] = append(cost[u], full[b]+cost[v][j])
			}
			ends[v], cost[v] = nil, nil
		}
	}
	best := inf
	for j, e := range ends[0] {
		best = math.Min(best, cost[0][j]+far(e, 0))
	}
	fmt.Printf("%.10f\n", best)
}
