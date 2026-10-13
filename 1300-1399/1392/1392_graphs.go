package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

var parent []int

func find(v int) int {
	for parent[v] != v {
		parent[v] = parent[parent[v]]
		v = parent[v]
	}
	return v
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var k int
	fmt.Fscan(in, &k)
	x, y, z, r := make([]int64, k), make([]int64, k), make([]int64, k), make([]int64, k)
	for i := 0; i < k; i++ {
		fmt.Fscan(in, &x[i], &y[i], &z[i], &r[i])
	}
	parent = make([]int, k)
	for i := range parent {
		parent[i] = i
	}
	// two balls share more than one point when the centres are closer than r1 + r2
	for i := 0; i < k; i++ {
		for j := i + 1; j < k; j++ {
			dx, dy, dz := x[i]-x[j], y[i]-y[j], z[i]-z[j]
			if dx*dx+dy*dy+dz*dz < (r[i]+r[j])*(r[i]+r[j]) {
				parent[find(j)] = find(i)
			}
		}
	}
	// each group lists its planets in order, and groups come by their first planet
	groups := make([][]int, k)
	for v := 0; v < k; v++ {
		groups[find(v)] = append(groups[find(v)], v)
	}
	var lists [][]int
	for _, g := range groups {
		if len(g) > 0 {
			lists = append(lists, g)
		}
	}
	sort.Slice(lists, func(i, j int) bool { return lists[i][0] < lists[j][0] })
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for _, g := range lists {
		for i, v := range g {
			if i > 0 {
				out.WriteString(", ")
			}
			out.WriteString(strconv.Itoa(v))
		}
		out.WriteString("\n")
	}
}
