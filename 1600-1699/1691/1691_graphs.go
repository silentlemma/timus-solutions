package main

import (
	"bufio"
	"fmt"
	"os"
)

func reach(start int, adj [][]int) []bool {
	seen := make([]bool, len(adj))
	seen[start] = true
	stack := []int{start}
	for len(stack) > 0 {
		v := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		for _, u := range adj[v] {
			if !seen[u] {
				seen[u] = true
				stack = append(stack, u)
			}
		}
	}
	return seen
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, m, s, t int
	fmt.Fscan(in, &n, &m, &s, &t)
	s--
	t--
	from, to := make([]int, m), make([]int, m)
	adj, radj := make([][]int, n), make([][]int, n)
	for i := 0; i < m; i++ {
		fmt.Fscan(in, &from[i], &to[i])
		from[i]--
		to[i]--
		adj[from[i]] = append(adj[from[i]], to[i])
		radj[to[i]] = append(radj[to[i]], from[i])
	}
	// only vertices on some path from s to t matter; they form whole
	// strongly connected components
	fromS := reach(s, adj)
	if !fromS[t] {
		fmt.Println(0)
		return
	}
	toT := reach(t, radj)
	alive := make([]bool, n)
	for v := range alive {
		alive[v] = fromS[v] && toT[v]
	}
	// Kosaraju: finishing order on the graph, then the reversed graph in
	// reverse finishing order numbers the components in topological order
	var order []int
	done := make([]bool, n)
	type frame struct{ v, i int }
	for root := 0; root < n; root++ {
		if !alive[root] || done[root] {
			continue
		}
		done[root] = true
		stack := []frame{{root, 0}}
		for len(stack) > 0 {
			top := &stack[len(stack)-1]
			if top.i < len(adj[top.v]) {
				u := adj[top.v][top.i]
				top.i++
				if alive[u] && !done[u] {
					done[u] = true
					stack = append(stack, frame{u, 0})
				}
			} else {
				order = append(order, top.v)
				stack = stack[:len(stack)-1]
			}
		}
	}
	comp := make([]int, n)
	for v := range comp {
		comp[v] = -1
	}
	count := 0
	for k := len(order) - 1; k >= 0; k-- {
		root := order[k]
		if comp[root] >= 0 {
			continue
		}
		comp[root] = count
		stack := []int{root}
		for len(stack) > 0 {
			v := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			for _, u := range radj[v] {
				if alive[u] && comp[u] < 0 {
					comp[u] = count
					stack = append(stack, u)
				}
			}
		}
		count++
	}
	size, inside := make([]int, count), make([]int, count)
	out := make([][]int, count)
	for v := 0; v < n; v++ {
		if alive[v] {
			size[comp[v]]++
		}
	}
	for i := 0; i < m; i++ {
		a, b := from[i], to[i]
		if alive[a] && alive[b] {
			if comp[a] == comp[b] {
				inside[comp[a]]++
			} else {
				out[comp[a]] = append(out[comp[a]], comp[b])
			}
		}
	}
	// a component with more arcs than vertices holds two cycles, and paths grow
	// exponentially; otherwise each cyclic component is one simple cycle, and
	// paths through c of them number about N^(c - 1)
	for c := 0; c < count; c++ {
		if inside[c] > size[c] {
			fmt.Println(-1)
			return
		}
	}
	// best[c]: the most cycles on a path from s into component c; arcs go
	// from lower to higher numbers, so one pass in order settles it
	best := make([]int, count)
	for c := 0; c < count; c++ {
		if inside[c] == size[c] {
			best[c]++
		}
		for _, d := range out[c] {
			if best[c] > best[d] {
				best[d] = best[c]
			}
		}
	}
	answer := best[comp[t]] - 1
	if answer < 0 {
		answer = 0
	}
	fmt.Println(answer)
}
