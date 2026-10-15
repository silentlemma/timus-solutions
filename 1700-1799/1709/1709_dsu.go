package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	var n int
	var d, a int64
	fmt.Fscan(reader, &n, &d, &a)
	flights := make([]string, n)
	for i := range flights {
		fmt.Fscan(reader, &flights[i])
	}
	parent := make([]int, n)
	for i := range parent {
		parent[i] = i
	}
	find := func(x int) int {
		for parent[x] != x {
			parent[x] = parent[parent[x]]
			x = parent[x]
		}
		return x
	}
	// the result must be a spanning tree: keep a spanning forest of the
	// existing flights, cancel the rest, then join the trees with new flights
	plan := make([][]byte, n)
	for i := range plan {
		plan[i] = make([]byte, n)
		for j := range plan[i] {
			plan[i][j] = '0'
		}
	}
	var cost int64
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			if flights[i][j] == '1' {
				ri, rj := find(i), find(j)
				if ri != rj {
					parent[ri] = rj
				} else {
					plan[i][j], plan[j][i] = 'd', 'd'
					cost += d
				}
			}
		}
	}
	for j := 1; j < n; j++ {
		r0, rj := find(0), find(j)
		if r0 != rj {
			parent[rj] = r0
			plan[0][j], plan[j][0] = 'a', 'a'
			cost += a
		}
	}
	fmt.Fprintln(writer, cost)
	for _, row := range plan {
		writer.Write(row)
		writer.WriteString("\n")
	}
}
