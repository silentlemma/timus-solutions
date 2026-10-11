package main

import (
	"bufio"
	"os"
	"strconv"
)

const ids = 32768 // station indices go up to 32767

var adj [ids][]int

func bfs(start int) []int {
	dist := make([]int, ids)
	for i := range dist {
		dist[i] = -1
	}
	dist[start] = 0
	queue := []int{start}
	for head := 0; head < len(queue); head++ {
		u := queue[head]
		for _, v := range adj[u] {
			if dist[v] < 0 {
				dist[v] = dist[u] + 1
				queue = append(queue, v)
			}
		}
	}
	return dist
}

func adjacent(a, b int) bool {
	for _, v := range adj[a] {
		if v == b {
			return true
		}
	}
	return false
}

func main() {
	in := bufio.NewScanner(os.Stdin)
	in.Split(bufio.ScanWords)
	next := func() int {
		in.Scan()
		v, _ := strconv.Atoi(in.Text())
		return v
	}
	var present [ids]bool
	n := next()
	for i := 0; i < n; i++ {
		line := make([]int, next())
		for j := range line {
			line[j] = next()
			present[line[j]] = true
		}
		for j := 0; j+1 < len(line); j++ {
			adj[line[j]] = append(adj[line[j]], line[j+1])
			adj[line[j+1]] = append(adj[line[j+1]], line[j])
		}
	}
	seen := make([]int, next())
	for i := range seen {
		seen[i] = next()
	}
	// the stations seen must be a walk through the network ...
	for i, s := range seen {
		if s < 0 || s >= ids || !present[s] || (i > 0 && !adjacent(seen[i-1], s)) {
			return
		}
	}
	m := len(seen)
	first := bfs(seen[0])
	// ... and a shortest one, or no target fits it
	if first[seen[m-1]] != m-1 {
		return
	}
	last := bfs(seen[m-1])
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	// a target fits when the walk can go on to it along a shortest path
	for t := 0; t < ids; t++ {
		if first[t] >= 0 && last[t] >= 0 && first[t] == m-1+last[t] {
			out.WriteString(strconv.Itoa(t) + "\n")
		}
	}
}
