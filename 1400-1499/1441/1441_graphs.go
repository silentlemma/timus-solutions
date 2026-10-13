package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	var n, m int
	fmt.Fscan(reader, &n, &m)
	ends := make([]int, 2*m)
	degree := make([]int, n+1)
	for i := range ends {
		fmt.Fscan(reader, &ends[i])
		degree[ends[i]]++
	}
	// vertex 0 is a helper joined to every room with an odd number of tunnels
	for v := 1; v <= n; v++ {
		if degree[v]%2 == 1 {
			ends = append(ends, 0, v)
		}
	}
	edges := len(ends) / 2
	adj := make([][]int, n+1)
	for e := 0; e < edges; e++ {
		adj[ends[2*e]] = append(adj[ends[2*e]], e)
		adj[ends[2*e+1]] = append(adj[ends[2*e+1]], e)
	}
	// an Euler circuit, found without recursion
	used := make([]bool, edges)
	pos := make([]int, n+1)
	start := 0
	if len(adj[0]) == 0 {
		start = 1
	}
	stack := []int{start}
	var circuit []int
	for len(stack) > 0 {
		v := stack[len(stack)-1]
		for pos[v] < len(adj[v]) && used[adj[v][pos[v]]] {
			pos[v]++
		}
		if pos[v] == len(adj[v]) {
			circuit = append(circuit, v)
			stack = stack[:len(stack)-1]
			continue
		}
		e := adj[v][pos[v]]
		used[e] = true
		stack = append(stack, ends[2*e]+ends[2*e+1]-v)
	}
	// the helper edges cut the circuit into trails of real tunnels
	var trails []string
	var current []string
	for _, v := range circuit {
		if v == 0 {
			if len(current) > 0 {
				trails = append(trails, strings.Join(current, " "))
			}
			current = nil
		} else {
			current = append(current, strconv.Itoa(v))
		}
	}
	if len(current) > 0 {
		trails = append(trails, strings.Join(current, " "))
	}
	fmt.Fprintln(writer, len(trails))
	for _, t := range trails {
		fmt.Fprintln(writer, t)
	}
}
