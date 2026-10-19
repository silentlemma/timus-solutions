package main

import (
	"bufio"
	"fmt"
	"math/rand"
	"os"
	"strconv"
)

const seed = 31337

func main() {
	in := bufio.NewScanner(os.Stdin)
	in.Split(bufio.ScanWords)
	next := func() int {
		in.Scan()
		v, _ := strconv.Atoi(in.Text())
		return v
	}
	n, m := next(), next()
	adj := make([][]int, n)
	for i := 0; i < n-1; i++ {
		u, v := next()-1, next()-1
		adj[u] = append(adj[u], v)
		adj[v] = append(adj[v], u)
	}
	// every technology gets a random weight; a path uses each one exactly once
	// when (with overwhelming probability) its weights add up to the sum of all
	rng := rand.New(rand.NewSource(seed))
	weight := make([]uint64, m+1)
	goal := uint64(0)
	for t := 1; t <= m; t++ {
		weight[t] = rng.Uint64()
		goal += weight[t]
	}
	own := make([]uint64, n)
	for v := 0; v < n; v++ {
		for a := next(); a > 0; a-- {
			own[v] += weight[next()]
		}
	}
	// depth[v]: the weights on the path from the root to v
	parent := make([]int, n)
	parent[0] = -1
	depth := make([]uint64, n)
	depth[0] = own[0]
	order := []int{0}
	for k := 0; k < len(order); k++ {
		v := order[k]
		for _, u := range adj[v] {
			if u != parent[v] {
				parent[u] = v
				depth[u] = depth[v] + own[u]
				order = append(order, u)
			}
		}
	}
	// small to large: below[v] maps depth -> a vertex of the subtree of v; two
	// vertices from different children of x (or x itself) join through x
	below := make([]map[uint64]int, n)
	for k := n - 1; k >= 0; k-- {
		x := order[k]
		if own[x] == goal {
			fmt.Println(x+1, x+1)
			return
		}
		mine := map[uint64]int{depth[x]: x}
		target := goal + 2*depth[x] - own[x]
		for _, y := range adj[x] {
			if y == parent[x] {
				continue
			}
			other := below[y]
			below[y] = nil
			if len(other) > len(mine) {
				mine, other = other, mine
			}
			for d, u := range other {
				if v, ok := mine[target-d]; ok {
					fmt.Println(u+1, v+1)
					return
				}
			}
			for d, u := range other {
				mine[d] = u
			}
		}
		below[x] = mine
	}
	fmt.Println("No solution")
}
