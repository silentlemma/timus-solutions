package main

import (
	"bufio"
	"os"
	"sort"
	"strconv"
)

type edge struct{ a, b, length int }

func readInt(in *bufio.Reader) int {
	c, _ := in.ReadByte()
	for c == ' ' || c == '\n' || c == '\r' {
		c, _ = in.ReadByte()
	}
	n := 0
	for ; c >= '0' && c <= '9'; c, _ = in.ReadByte() {
		n = n*10 + int(c-'0')
	}
	return n
}

func main() {
	in := bufio.NewReader(os.Stdin)
	n, m := readInt(in), readInt(in)
	edges := make([]edge, m)
	for k := range edges {
		edges[k] = edge{readInt(in), readInt(in), readInt(in)}
	}
	sort.SliceStable(edges, func(x, y int) bool { return edges[x].length < edges[y].length })
	parent := make([]int, n+1)
	for v := range parent {
		parent[v] = v
	}
	find := func(v int) int {
		for parent[v] != v {
			parent[v] = parent[parent[v]]
			v = parent[v]
		}
		return v
	}
	// Kruskal's tree: its longest cable is the smallest possible longest cable
	// of any plan that connects every hub
	var chosen []edge
	for _, e := range edges {
		if ra, rb := find(e.a), find(e.b); ra != rb {
			parent[ra] = rb
			chosen = append(chosen, e)
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	out.WriteString(strconv.Itoa(chosen[len(chosen)-1].length) + "\n")
	out.WriteString(strconv.Itoa(len(chosen)) + "\n")
	for _, e := range chosen {
		out.WriteString(strconv.Itoa(e.a) + " " + strconv.Itoa(e.b) + "\n")
	}
}
