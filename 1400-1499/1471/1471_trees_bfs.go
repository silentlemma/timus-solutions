package main

import (
	"bufio"
	"fmt"
	"os"
)

const inputBuffer = 4096

// refills bound storage even when whitespace or tokens cross a buffer boundary.
type reader struct {
	buffer   [inputBuffer]byte
	at, size int
}

func (r *reader) read() byte {
	if r.at == r.size {
		r.size, _ = os.Stdin.Read(r.buffer[:])
		r.at = 0
		if r.size == 0 {
			return 0
		}
	}
	c := r.buffer[r.at]
	r.at++
	return c
}
func (r *reader) next() int {
	c := r.read()
	for c != 0 && c != '-' && (c < '0' || c > '9') {
		c = r.read()
	}
	sign := 1
	if c == '-' {
		sign = -1
		c = r.read()
	}
	value := 0
	for c >= '0' && c <= '9' {
		value = value*10 + int(c-'0')
		c = r.read()
	}
	return sign * value
}

func main() {
	input := reader{}
	n := input.next()
	type edge struct{ to, weight int }
	edges := make([][]edge, n)
	for i := 1; i < n; i++ {
		u, v, w := input.next(), input.next(), input.next()
		edges[u] = append(edges[u], edge{v, w})
		edges[v] = append(edges[v], edge{u, w})
	}
	parent, depth, distance := make([]int, n), make([]int, n), make([]int, n)
	size, heavy, top := make([]int, n), make([]int, n), make([]int, n)
	for i := range parent {
		parent[i] = -1
		size[i] = 1
		heavy[i] = -1
	}
	order := make([]int, 1, n)
	for i := 0; i < n; i++ {
		v := order[i]
		for _, e := range edges[v] {
			if e.to != parent[v] {
				u := e.to
				parent[u] = v
				depth[u] = depth[v] + 1
				distance[u] = distance[v] + e.weight
				order = append(order, u)
			}
		}
	}
	for i := n - 1; i > 0; i-- {
		v := order[i]
		p := parent[v]
		size[p] += size[v]
		if heavy[p] < 0 || size[v] > size[heavy[p]] {
			heavy[p] = v
		}
	}
	// a light-edge jump at least doubles the subtree size, so there are O(log n) jumps.
	for _, v := range order {
		if v != 0 {
			top[v] = v
			if heavy[parent[v]] == v {
				top[v] = top[parent[v]]
			}
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	m := input.next()
	for i := 0; i < m; i++ {
		a, b := input.next(), input.next()
		answer := distance[a] + distance[b]
		for top[a] != top[b] {
			if depth[top[a]] < depth[top[b]] {
				a, b = b, a
			}
			a = parent[top[a]]
		}
		if depth[a] > depth[b] {
			a = b
		}
		fmt.Fprintln(out, answer-2*distance[a])
	}
}
