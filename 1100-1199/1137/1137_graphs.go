package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

// stops are numbered up to this
const stops = 1000

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	adj := make([][]int, stops+1)
	edges, start := 0, -1
	for r := 0; r < n; r++ {
		var m int
		fmt.Fscan(in, &m)
		route := make([]int, m+1)
		for k := range route {
			fmt.Fscan(in, &route[k])
		}
		if start < 0 {
			start = route[0]
		}
		for k := 0; k < m; k++ {
			adj[route[k]] = append(adj[route[k]], route[k+1])
		}
		edges += m
	}
	// every old route is a cycle, so each stop is left as often as it is
	// entered; Hierholzer's walk then uses every segment once
	ptr := make([]int, stops+1)
	stack, circuit := []int{start}, []int{}
	for len(stack) > 0 {
		v := stack[len(stack)-1]
		if ptr[v] < len(adj[v]) {
			stack = append(stack, adj[v][ptr[v]])
			ptr[v]++
		} else {
			circuit = append(circuit, v)
			stack = stack[:len(stack)-1]
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	if len(circuit) != edges+1 {
		out.WriteString("0\n")
		return
	}
	out.WriteString(strconv.Itoa(edges))
	for k := len(circuit) - 1; k >= 0; k-- {
		out.WriteString(" " + strconv.Itoa(circuit[k]))
	}
	out.WriteString("\n")
}
