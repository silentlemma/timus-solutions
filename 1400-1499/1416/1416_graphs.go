package main

import (
	"bufio"
	"fmt"
	"os"
)

const inf = 1 << 30

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, m int
	fmt.Fscan(in, &n, &m)
	w := make([][]int, n)
	for i := range w {
		w[i] = make([]int, n)
		for j := range w[i] {
			w[i][j] = inf
		}
	}
	ea, eb, ec := make([]int, m), make([]int, m), make([]int, m)
	for i := 0; i < m; i++ {
		fmt.Fscan(in, &ea[i], &eb[i], &ec[i])
		ea[i]--
		eb[i]--
		w[ea[i]][eb[i]], w[eb[i]][ea[i]] = ec[i], ec[i]
	}
	// Prim on the matrix; heaviest[u][v] is the heaviest tree edge between u and v
	heaviest := make([][]int, n)
	inTree := make([][]bool, n)
	for i := range heaviest {
		heaviest[i] = make([]int, n)
		inTree[i] = make([]bool, n)
	}
	dist := append([]int(nil), w[0]...)
	parent := make([]int, n)
	done := make([]bool, n)
	done[0] = true
	order := []int{0}
	total := 0
	for step := 1; step < n; step++ {
		v := -1
		for u := 0; u < n; u++ {
			if !done[u] && (v < 0 || dist[u] < dist[v]) {
				v = u
			}
		}
		p, c := parent[v], dist[v]
		total += c
		inTree[p][v], inTree[v][p] = true, true
		for _, u := range order {
			h := heaviest[p][u]
			if c > h {
				h = c
			}
			heaviest[u][v], heaviest[v][u] = h, h
		}
		done[v] = true
		order = append(order, v)
		for u := 0; u < n; u++ {
			if !done[u] && w[v][u] < dist[u] {
				dist[u], parent[u] = w[v][u], v
			}
		}
	}
	// the next tree swaps one outside edge for the heaviest edge on its tree path
	swap := inf
	for i := 0; i < m; i++ {
		if d := ec[i] - heaviest[ea[i]][eb[i]]; !inTree[ea[i]][eb[i]] && d < swap {
			swap = d
		}
	}
	fmt.Printf("Cost: %d\n", total)
	if swap == inf {
		fmt.Println("Cost: -1")
	} else {
		fmt.Printf("Cost: %d\n", total+swap)
	}
}
