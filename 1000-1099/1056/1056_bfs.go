package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

var adj [][]int

// bfs returns the distances from s and the predecessors on the shortest paths
func bfs(s int) ([]int, []int) {
	dist := make([]int, len(adj))
	prev := make([]int, len(adj))
	for i := range dist {
		dist[i] = -1
	}
	dist[s] = 0
	queue := []int{s}
	for i := 0; i < len(queue); i++ {
		for _, w := range adj[queue[i]] {
			if dist[w] < 0 {
				dist[w] = dist[queue[i]] + 1
				prev[w] = queue[i]
				queue = append(queue, w)
			}
		}
	}
	return dist, prev
}

func farthest(dist []int) int {
	best := 1
	for v := 1; v < len(dist); v++ {
		if dist[v] > dist[best] {
			best = v
		}
	}
	return best
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	adj = make([][]int, n+1)
	for i := 2; i <= n; i++ {
		var p int
		fmt.Fscan(in, &p)
		adj[i] = append(adj[i], p)
		adj[p] = append(adj[p], i)
	}
	// the farthest computer from any start is an end of a longest path; the
	// farthest one from it is the other end
	dist, _ := bfs(1)
	u := farthest(dist)
	dist, prev := bfs(u)
	v := farthest(dist)
	// the centers are the middle one or two computers of that path
	length := dist[v]
	set := map[int]bool{}
	for k, x := 0, v; k <= length; k, x = k+1, prev[x] {
		if k == length/2 || k == (length+1)/2 {
			set[x] = true
		}
	}
	var centers []int
	for c := range set {
		centers = append(centers, c)
	}
	sort.Ints(centers)
	parts := make([]string, len(centers))
	for i, c := range centers {
		parts[i] = strconv.Itoa(c)
	}
	fmt.Println(strings.Join(parts, " "))
}
