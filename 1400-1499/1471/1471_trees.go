package main

import (
	"bufio"
	"fmt"
	"math/bits"
	"os"
	"strconv"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	readInt := func() int { var value int; fmt.Fscan(reader, &value); return value }
	n := readInt()
	type edge struct{ to, weight int }
	adjacency := make([][]edge, n)
	for i := 1; i < n; i++ {
		u, v, w := readInt(), readInt(), readInt()
		adjacency[u] = append(adjacency[u], edge{v, w})
		adjacency[v] = append(adjacency[v], edge{u, w})
	}

	// euler tour from vertex 0: a vertex is written on entry and after each child
	parent := make([]int, n)
	for i := range parent {
		parent[i] = -1
	}
	depth, dist, first := make([]int, n), make([]int, n), make([]int, n)
	tour := []int{0}
	pointer := make([]int, n)
	stack := []int{0}
	for len(stack) > 0 {
		v := stack[len(stack)-1]
		p := pointer[v]
		if p < len(adjacency[v]) {
			pointer[v]++
			u := adjacency[v][p].to
			if u == parent[v] {
				continue
			}
			parent[u] = v
			depth[u] = depth[v] + 1
			dist[u] = dist[v] + adjacency[v][p].weight
			first[u] = len(tour)
			tour = append(tour, u)
			stack = append(stack, u)
		} else {
			stack = stack[:len(stack)-1]
			if len(stack) > 0 {
				tour = append(tour, stack[len(stack)-1])
			}
		}
	}

	// sparse table: the shallowest vertex of each run of 2^k tour entries
	shallower := func(a, b int) int {
		if depth[a] <= depth[b] {
			return a
		}
		return b
	}
	table := [][]int{tour}
	for span := 1; 2*span <= len(tour); span *= 2 {
		prev := table[len(table)-1]
		level := make([]int, len(tour)-2*span+1)
		for i := range level {
			level[i] = shallower(prev[i], prev[i+span])
		}
		table = append(table, level)
	}

	m := readInt()
	for ; m > 0; m-- {
		a, b := readInt(), readInt()
		lo, hi := first[a], first[b]
		if lo > hi {
			lo, hi = hi, lo
		}
		k := bits.Len(uint(hi-lo+1)) - 1
		lca := shallower(table[k][lo], table[k][hi-(1<<k)+1])
		writer.WriteString(strconv.Itoa(dist[a]+dist[b]-2*dist[lca]) + "\n")
	}
}
