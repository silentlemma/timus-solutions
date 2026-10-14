package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

const (
	golden = 0x9E3779B97F4A7C15
	mix1   = 0xBF58476D1CE4E5B9
	mix2   = 0x94D049BB133111EB
	shift1 = 30
	shift2 = 27
	shift3 = 31
)

// mix is a splitmix64 step: well-spread 64-bit labels from a counter
func mix(x uint64) uint64 {
	x += golden
	x = (x ^ (x >> shift1)) * mix1
	x = (x ^ (x >> shift2)) * mix2
	return x ^ (x >> shift3)
}

type arc struct{ to, edge int }

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, m int
	fmt.Fscan(in, &n, &m)
	from, to := make([]int, m), make([]int, m)
	adj := make([][]arc, n)
	for e := 0; e < m; e++ {
		fmt.Fscan(in, &from[e], &to[e])
		from[e]--
		to[e]--
		adj[from[e]] = append(adj[from[e]], arc{to[e], e})
		adj[to[e]] = append(adj[to[e]], arc{from[e], e})
	}
	// a spanning tree in breadth-first order
	parent, parentEdge := make([]int, n), make([]int, n)
	seen, inTree := make([]bool, n), make([]bool, m)
	order := []int{0}
	seen[0] = true
	for i := 0; i < len(order); i++ {
		for _, a := range adj[order[i]] {
			if !seen[a.to] {
				seen[a.to] = true
				parent[a.to], parentEdge[a.to], inTree[a.edge] = order[i], a.edge, true
				order = append(order, a.to)
			}
		}
	}
	// every other channel gets a random label; a tree channel gets the XOR
	// of the labels of the channels whose cycles pass through it, which is
	// the XOR over the subtree below it
	label, below := make([]uint64, m), make([]uint64, n)
	for e := 0; e < m; e++ {
		if !inTree[e] {
			label[e] = mix(uint64(e))
			below[from[e]] ^= label[e]
			below[to[e]] ^= label[e]
		}
	}
	for i := n - 1; i > 0; i-- {
		v := order[i]
		label[parentEdge[v]] = below[v]
		below[parent[v]] ^= below[v]
	}
	// a bridge (label 0) cuts with any other channel; two other channels cut
	// together exactly when no cycle passes through just one of them
	sort.Slice(label, func(a, b int) bool { return label[a] < label[b] })
	bridges := int64(sort.Search(m, func(e int) bool { return label[e] != 0 }))
	total, rest := int64(m)*int64(m-1)/2, int64(m)-bridges
	total -= rest * (rest - 1) / 2
	for i, j := int(bridges), int(bridges); i < m; i = j {
		for j < m && label[j] == label[i] {
			j++
		}
		total += int64(j-i) * int64(j-i-1) / 2
	}
	fmt.Println(total)
}
