package main

import (
	"bufio"
	"fmt"
	"os"
)

// two people can team up only if their ranks differ by exactly 2, so half
// the rank changes parity along every pair: the graph is bipartite
const (
	gap   = 2
	sides = 2
)

type person struct {
	name          string
	writes, tests bool
	rank          int
}

var (
	adj                       [][]int
	mateLeft, mateRight, dist []int
)

func layers() bool {
	queue := []int{}
	for u := range adj {
		dist[u] = -1
		if mateLeft[u] < 0 {
			dist[u] = 0
			queue = append(queue, u)
		}
	}
	found := false
	for h := 0; h < len(queue); h++ {
		u := queue[h]
		for _, v := range adj[u] {
			w := mateRight[v]
			if w < 0 {
				found = true
			} else if dist[w] < 0 {
				dist[w] = dist[u] + 1
				queue = append(queue, w)
			}
		}
	}
	return found
}

func augment(u int) bool {
	for _, v := range adj[u] {
		w := mateRight[v]
		if w < 0 || (dist[w] == dist[u]+1 && augment(w)) {
			mateLeft[u] = v
			mateRight[v] = u
			return true
		}
	}
	dist[u] = -1
	return false
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var n int
	fmt.Fscan(in, &n)
	people := make([]person, n)
	var side [sides][]int
	for i := range people {
		var kind string
		fmt.Fscan(in, &people[i].name, &kind, &people[i].rank)
		people[i].writes = kind != "testdata"
		people[i].tests = kind != "statements"
		s := people[i].rank / gap % sides
		side[s] = append(side[s], i)
	}
	left, right := side[0], side[1]
	adj = make([][]int, len(left))
	for i, x := range left {
		a := people[x]
		for j, y := range right {
			b := people[y]
			close := a.rank-b.rank == gap || b.rank-a.rank == gap
			if close && ((a.writes && b.tests) || (b.writes && a.tests)) {
				adj[i] = append(adj[i], j)
			}
		}
	}
	mateLeft = make([]int, len(left))
	mateRight = make([]int, len(right))
	dist = make([]int, len(left))
	for i := range mateLeft {
		mateLeft[i] = -1
	}
	for i := range mateRight {
		mateRight[i] = -1
	}
	total := 0
	for layers() {
		for u := range left {
			if mateLeft[u] < 0 && augment(u) {
				total++
			}
		}
	}
	fmt.Fprintln(out, total)
	for u, v := range mateLeft {
		if v < 0 {
			continue
		}
		a, b := people[left[u]], people[right[v]]
		if a.writes && b.tests {
			fmt.Fprintln(out, a.name, b.name)
		} else {
			fmt.Fprintln(out, b.name, a.name)
		}
	}
}
