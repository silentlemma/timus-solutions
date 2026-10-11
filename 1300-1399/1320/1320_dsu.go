package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const vertices = 1000

func main() {
	sc := bufio.NewScanner(bufio.NewReader(os.Stdin))
	sc.Split(bufio.ScanWords)
	var ends []int
	for sc.Scan() {
		v, _ := strconv.Atoi(sc.Text())
		ends = append(ends, v)
	}
	parent := make([]int, vertices+1)
	edges := make([]int, vertices+1) // edges of each component, kept at its root
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
	for i := 0; i+1 < len(ends); i += 2 {
		ra, rb := find(ends[i]), find(ends[i+1])
		if ra != rb {
			parent[ra] = rb
			edges[rb] += edges[ra]
		}
		edges[rb]++
	}
	answer := 1
	for v := 1; v <= vertices; v++ {
		if parent[v] == v && edges[v]%2 != 0 {
			answer = 0
		}
	}
	fmt.Println(answer)
}
