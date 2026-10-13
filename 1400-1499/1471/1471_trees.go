package main

import (
	"bufio"
	"math/bits"
	"os"
	"strconv"
)

const buffer = 1 << 20

func main() {
	reader := bufio.NewReaderSize(os.Stdin, buffer)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	readInt := func() int {
		x := 0
		c, _ := reader.ReadByte()
		for c < '0' || c > '9' {
			c, _ = reader.ReadByte()
		}
		for c >= '0' && c <= '9' {
			x = x*10 + int(c-'0')
			var err error
			if c, err = reader.ReadByte(); err != nil {
				break
			}
		}
		return x
	}

	n := readInt()
	us, vs, ws := make([]int, n-1), make([]int, n-1), make([]int, n-1)
	start := make([]int, n+1)
	for i := 0; i+1 < n; i++ {
		us[i], vs[i], ws[i] = readInt(), readInt(), readInt()
		start[us[i]+1]++
		start[vs[i]+1]++
	}
	// adjacency lists packed into one array (both directions of each edge)
	for i := 0; i < n; i++ {
		start[i+1] += start[i]
	}
	fill := append([]int(nil), start[:n]...)
	adj, weight := make([]int, 2*(n-1)), make([]int, 2*(n-1))
	for i := 0; i+1 < n; i++ {
		adj[fill[us[i]]], weight[fill[us[i]]] = vs[i], ws[i]
		fill[us[i]]++
		adj[fill[vs[i]]], weight[fill[vs[i]]] = us[i], ws[i]
		fill[vs[i]]++
	}

	// Euler tour from vertex 0: a vertex is written on entry and after each child
	parent := make([]int, n)
	for i := range parent {
		parent[i] = -1
	}
	depth, dist, first := make([]int, n), make([]int, n), make([]int, n)
	tour := []int{0}
	pointer := append([]int(nil), start[:n]...)
	stack := []int{0}
	for len(stack) > 0 {
		v := stack[len(stack)-1]
		p := pointer[v]
		if p < start[v+1] {
			pointer[v]++
			u := adj[p]
			if u == parent[v] {
				continue
			}
			parent[u] = v
			depth[u] = depth[v] + 1
			dist[u] = dist[v] + weight[p]
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
