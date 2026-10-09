package main

import (
	"bufio"
	"fmt"
	"os"
)

const bufSize = 1 << 16

// matching runs Hopcroft-Karp: BFS layers from the free left vertices, then
// vertex-disjoint shortest augmenting paths along the layers
type matching struct {
	adj                      [][]int
	matchL, matchR, dist, it []int
}

func (g *matching) layer() bool {
	var queue []int
	for v := range g.adj {
		g.dist[v] = -1
		if g.matchL[v] < 0 {
			g.dist[v] = 0
			queue = append(queue, v)
		}
	}
	found := false
	for len(queue) > 0 {
		v := queue[0]
		queue = queue[1:]
		for _, u := range g.adj[v] {
			w := g.matchR[u]
			if w < 0 {
				found = true
			} else if g.dist[w] < 0 {
				g.dist[w] = g.dist[v] + 1
				queue = append(queue, w)
			}
		}
	}
	return found
}

func (g *matching) augment(v int) bool {
	for ; g.it[v] < len(g.adj[v]); g.it[v]++ {
		u := g.adj[v][g.it[v]]
		w := g.matchR[u]
		if w < 0 || (g.dist[w] == g.dist[v]+1 && g.augment(w)) {
			g.matchL[v], g.matchR[u] = u, v
			return true
		}
	}
	g.dist[v] = -1
	return false
}

func main() {
	in := bufio.NewReaderSize(os.Stdin, bufSize)
	// readInt skips separators and reads one non-negative number
	readInt := func() int {
		c, _ := in.ReadByte()
		for c < '0' || c > '9' {
			c, _ = in.ReadByte()
		}
		v := 0
		for c >= '0' && c <= '9' {
			v = v*10 + int(c-'0')
			c, _ = in.ReadByte()
		}
		return v
	}
	m, n, k := readInt(), readInt(), readInt()
	g := &matching{
		adj:    make([][]int, m),
		matchL: make([]int, m),
		matchR: make([]int, n),
		dist:   make([]int, m),
		it:     make([]int, m),
	}
	for i := 0; i < k; i++ {
		a, b := readInt(), readInt()
		g.adj[a-1] = append(g.adj[a-1], b-1)
	}
	for v := range g.matchL {
		g.matchL[v] = -1
	}
	for u := range g.matchR {
		g.matchR[u] = -1
	}
	size := 0
	for g.layer() {
		for v := range g.it {
			g.it[v] = 0
		}
		for v := range g.adj {
			if g.matchL[v] < 0 && g.augment(v) {
				size++
			}
		}
	}
	// a minimum edge cover takes a maximum matching and one more edge for
	// every vertex the matching leaves uncovered
	fmt.Println(m + n - size)
}
