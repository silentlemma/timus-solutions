package main

import (
	"bufio"
	"fmt"
	"os"
)

type edge struct{ from, to, weight int }

func reach(links [][]int) []bool {
	seen := make([]bool, len(links))
	seen[0] = true
	stack := []int{0}
	for len(stack) > 0 {
		v := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		for _, u := range links[v] {
			if !seen[u] {
				seen[u] = true
				stack = append(stack, u)
			}
		}
	}
	return seen
}

// negativeCycle: Bellman-Ford from every node at once, is some cycle negative?
func negativeCycle(nodes int, edges []edge, sign int) bool {
	dist := make([]int, nodes)
	for round := 0; round < nodes; round++ {
		changed := false
		for _, e := range edges {
			if dist[e.from]+sign*e.weight < dist[e.to] {
				dist[e.to] = dist[e.from] + sign*e.weight
				changed = true
			}
		}
		if !changed {
			return false
		}
	}
	return true
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	s := n + 1
	// rule[j][i][k]: cockroaches next month in a flat with j, i below, k above
	rule := make([][][]int, s)
	for j := range rule {
		rule[j] = make([][]int, s)
		for i := range rule[j] {
			rule[j][i] = make([]int, s)
			for k := range rule[j][i] {
				fmt.Fscan(in, &rule[j][i][k])
			}
		}
	}
	// a finite floor plan read upwards is a closed walk through the pair (0, 0)
	// of the graph on pairs of neighbours; a step (a, b) -> (b, c) changes the
	// total by rule[b][a][c] - b, so the totals of a walk give the change
	outOf, into := make([][]int, s*s), make([][]int, s*s)
	var all []edge
	for a := 0; a < s; a++ {
		for b := 0; b < s; b++ {
			for c := 0; c < s; c++ {
				all = append(all, edge{a*s + b, b*s + c, rule[b][a][c] - b})
				outOf[a*s+b] = append(outOf[a*s+b], b*s+c)
				into[b*s+c] = append(into[b*s+c], a*s+b)
			}
		}
	}
	forward, backward := reach(outOf), reach(into)
	var edges []edge
	for _, e := range all {
		if forward[e.from] && backward[e.from] && forward[e.to] && backward[e.to] {
			edges = append(edges, e)
		}
	}
	fall, rise := negativeCycle(s*s, edges, 1), negativeCycle(s*s, edges, -1)
	switch {
	case fall && rise:
		fmt.Println("<>")
	case fall:
		fmt.Println("<")
	case rise:
		fmt.Println(">")
	default:
		fmt.Println("=")
	}
}
