package main

import (
	"bufio"
	"os"
	"strconv"
)

type road struct{ a, b int }
type link struct{ to, id int }

func main() {
	sc := bufio.NewScanner(os.Stdin)
	sc.Split(bufio.ScanWords)
	next := func() int {
		sc.Scan()
		v, _ := strconv.Atoi(sc.Text())
		return v
	}
	n, m := next(), next()
	ends := make([]road, m)
	adj := make([][]link, n+1)
	for i := range ends {
		ends[i] = road{next(), next()}
		adj[ends[i].a] = append(adj[ends[i].a], link{ends[i].b, i})
		adj[ends[i].b] = append(adj[ends[i].b], link{ends[i].a, i})
	}
	parent := make([]int, n+1)
	depth := make([]int, n+1)
	for i := range depth {
		depth[i] = -1
	}
	tree := make([]bool, m)
	// a breadth-first forest keeps the tree paths, and so the tours, short
	for root := 1; root <= n; root++ {
		if depth[root] >= 0 {
			continue
		}
		depth[root] = 0
		queue := []int{root}
		for len(queue) > 0 {
			u := queue[0]
			queue = queue[1:]
			for _, l := range adj[u] {
				if depth[l.to] < 0 {
					depth[l.to] = depth[u] + 1
					parent[l.to] = u
					tree[l.id] = true
					queue = append(queue, l.to)
				}
			}
		}
	}
	var tours [][]int
	// every road outside the forest closes its own tour with the tree path
	for i, e := range ends {
		if tree[i] {
			continue
		}
		a, b := e.a, e.b
		var left, right []int
		for depth[a] > depth[b] {
			left = append(left, a)
			a = parent[a]
		}
		for depth[b] > depth[a] {
			right = append(right, b)
			b = parent[b]
		}
		for a != b {
			left = append(left, a)
			right = append(right, b)
			a, b = parent[a], parent[b]
		}
		left = append(left, a)
		for j := len(right) - 1; j >= 0; j-- {
			left = append(left, right[j])
		}
		tours = append(tours, left)
	}
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	w.WriteString(strconv.Itoa(len(tours)))
	w.WriteString("\n")
	for _, cycle := range tours {
		w.WriteString(strconv.Itoa(len(cycle)))
		for _, c := range cycle {
			w.WriteString(" ")
			w.WriteString(strconv.Itoa(c))
		}
		w.WriteString("\n")
	}
}
