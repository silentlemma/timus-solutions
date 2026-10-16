package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

const shaves = 2

type edge struct{ to, cap int }

var (
	edges     []edge
	out       [][]int
	level, at []int
)

func add(a, b, cap int) int {
	out[a] = append(out[a], len(edges))
	edges = append(edges, edge{b, cap})
	out[b] = append(out[b], len(edges))
	edges = append(edges, edge{a, 0})
	return len(edges) - 2
}

func push(v, sink, limit int) int {
	if v == sink {
		return limit
	}
	for ; at[v] < len(out[v]); at[v]++ {
		e := out[v][at[v]]
		if edges[e].cap > 0 && level[edges[e].to] == level[v]+1 {
			c := limit
			if edges[e].cap < c {
				c = edges[e].cap
			}
			if got := push(edges[e].to, sink, c); got > 0 {
				edges[e].cap -= got
				edges[e^1].cap += got
				return got
			}
		}
	}
	return 0
}

func maxFlow(source, sink int) int {
	total := 0
	for {
		level = make([]int, len(out))
		for i := range level {
			level[i] = -1
		}
		level[source] = 0
		queue := []int{source}
		for len(queue) > 0 {
			v := queue[0]
			queue = queue[1:]
			for _, e := range out[v] {
				if edges[e].cap > 0 && level[edges[e].to] < 0 {
					level[edges[e].to] = level[v] + 1
					queue = append(queue, edges[e].to)
				}
			}
		}
		if level[sink] < 0 {
			return total
		}
		at = make([]int, len(out))
		for {
			got := push(source, sink, shaves)
			if got == 0 {
				break
			}
			total += got
		}
	}
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var n, k int
	if _, err := fmt.Fscan(reader, &n, &k); err != nil {
		return
	}
	come, stay := make([]int, n), make([]int, n)
	seen := map[int]bool{}
	var cuts []int
	for i := 0; i < n; i++ {
		fmt.Fscan(reader, &come[i], &stay[i])
		for _, c := range []int{come[i], come[i] + stay[i]} {
			if !seen[c] {
				seen[c] = true
				cuts = append(cuts, c)
			}
		}
	}
	// minutes between consecutive arrivals and departures see the same
	// mages, so they form blocks: a block of L minutes shaves k L times, at
	// most min(L, 2) of them on one mage
	sort.Ints(cuts)
	blocks := len(cuts) - 1
	source, sink := n+blocks, n+blocks+1
	out = make([][]int, sink+1)
	type link struct{ block, edge int }
	links := make([][]link, n)
	for i := 0; i < n; i++ {
		add(source, i, shaves)
		for j := 0; j < blocks; j++ {
			if come[i] <= cuts[j] && cuts[j+1] <= come[i]+stay[i] {
				c := cuts[j+1] - cuts[j]
				if c > shaves {
					c = shaves
				}
				links[i] = append(links[i], link{j, add(i, n+j, c)})
			}
		}
	}
	for j := 0; j < blocks; j++ {
		add(n+j, sink, k*(cuts[j+1]-cuts[j]))
	}
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	if maxFlow(source, sink) < shaves*n {
		fmt.Fprintln(writer, "No")
		return
	}
	// inside a block the shaves are dealt out round the minutes, so the two
	// shaves of one mage fall on different minutes and no minute gets more
	// than k of them
	dealt := make([]int, blocks)
	fmt.Fprintln(writer, "Yes")
	for i := 0; i < n; i++ {
		var times []int
		for _, l := range links[i] {
			for u := 0; u < edges[l.edge^1].cap; u++ {
				j := l.block
				times = append(times, cuts[j]+dealt[j]%(cuts[j+1]-cuts[j]))
				dealt[j]++
			}
		}
		sort.Ints(times)
		fmt.Fprintln(writer, times[0], times[1])
	}
}
