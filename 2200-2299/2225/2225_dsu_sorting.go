package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func findRoot(parent []int, vertex int) int {
	for parent[vertex] != vertex {
		parent[vertex] = parent[parent[vertex]]
		vertex = parent[vertex]
	}
	return vertex
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	height := make([]int, n)
	order := make([]int, n)
	parent := make([]int, n)
	size := make([]int, n)
	for i := range height {
		fmt.Fscan(in, &height[i])
		order[i] = i
		parent[i] = i
	}
	sort.Slice(order, func(i, j int) bool {
		return height[order[i]] > height[order[j]]
	})
	var answer int64
	for _, vertex := range order {
		size[vertex] = 1
		answer += int64(height[vertex])
		for _, neighbor := range [2]int{vertex - 1, vertex + 1} {
			if neighbor < 0 || neighbor >= n || size[neighbor] == 0 {
				continue
			}
			a := findRoot(parent, vertex)
			b := findRoot(parent, neighbor)
			// Joining two odd runs saves one strike at every remaining level.
			if size[a]%2 == 1 && size[b]%2 == 1 {
				answer -= int64(height[vertex])
			}
			if size[a] < size[b] {
				a, b = b, a
			}
			parent[b] = a
			size[a] += size[b]
		}
	}
	fmt.Println(answer)
}
