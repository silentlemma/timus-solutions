package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, m int
	fmt.Fscan(in, &n, &m)
	protocol := make([]string, n)
	for i := range protocol {
		fmt.Fscan(in, &protocol[i])
	}
	adj := make([][]int, n)
	for i := 0; i < m; i++ {
		var a, b int
		fmt.Fscan(in, &a, &b)
		adj[a-1] = append(adj[a-1], b-1)
		adj[b-1] = append(adj[b-1], a-1)
	}
	// glue neighbours with the same protocol into regions
	region := make([]int, n)
	for i := range region {
		region[i] = -1
	}
	regions := 0
	for s := 0; s < n; s++ {
		if region[s] >= 0 {
			continue
		}
		region[s] = regions
		stack := []int{s}
		for len(stack) > 0 {
			v := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			for _, u := range adj[v] {
				if region[u] < 0 && protocol[u] == protocol[v] {
					region[u] = regions
					stack = append(stack, u)
				}
			}
		}
		regions++
	}
	near := make([]map[int]bool, regions)
	for r := range near {
		near[r] = map[int]bool{}
	}
	for v := 0; v < n; v++ {
		for _, u := range adj[v] {
			if region[u] != region[v] {
				near[region[v]][region[u]] = true
			}
		}
	}
	// switching a region merges it with all its neighbours, so switching the
	// same region again and again takes its eccentricity in steps, and no
	// plan does better than the radius of the region graph
	best, centre := regions, 0
	for start := 0; start < regions; start++ {
		dist := make([]int, regions)
		for i := range dist {
			dist[i] = -1
		}
		dist[start] = 0
		queue := []int{start}
		far := 0
		for len(queue) > 0 {
			r := queue[0]
			queue = queue[1:]
			if dist[r] > far {
				far = dist[r]
			}
			for x := range near[r] {
				if dist[x] < 0 {
					dist[x] = dist[r] + 1
					queue = append(queue, x)
				}
			}
		}
		if far < best {
			best, centre = far, start
		}
	}
	computer := 0
	for region[computer] != centre {
		computer++
	}
	current := protocol[computer]
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	fmt.Fprintln(out, best)
	for i := 0; i < best; i++ {
		if current == "J" {
			current = "E"
		} else {
			current = "J"
		}
		fmt.Fprintln(out, computer+1, current)
	}
}
