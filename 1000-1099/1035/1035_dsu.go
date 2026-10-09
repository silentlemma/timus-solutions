package main

import (
	"bufio"
	"fmt"
	"os"
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
	var n, m int
	fmt.Fscan(in, &n, &m)
	// the vertices of the grid are (i, j) -> i*(m+1)+j; balance[v] is the number
	// of front stitches minus the number of back stitches that end at v
	width := m + 1
	vertices := (n + 1) * width
	parent = make([]int, vertices)
	for v := range parent {
		parent[v] = v
	}
	balance := make([]int, vertices)
	stitched := make([]bool, vertices)
	for side := 0; side < 2; side++ {
		sign := 1
		if side == 1 {
			sign = -1
		}
		for i := 0; i < n; i++ {
			var row string
			fmt.Fscan(in, &row)
			for j := 0; j < m; j++ {
				c := row[j]
				ends := [2][2]int{
					{i*width + j, (i+1)*width + j + 1},
					{(i+1)*width + j, i*width + j + 1},
				}
				present := [2]bool{c == '\\' || c == 'X', c == '/' || c == 'X'}
				for d := 0; d < 2; d++ {
					if !present[d] {
						continue
					}
					a, b := ends[d][0], ends[d][1]
					balance[a] += sign
					balance[b] += sign
					stitched[a], stitched[b] = true, true
					parent[find(a)] = find(b)
				}
			}
		}
	}
	// a group needs one thread per two unbalanced stitch ends, and at least one
	ends := make([]int, vertices)
	used := make([]bool, vertices)
	for v := 0; v < vertices; v++ {
		if stitched[v] {
			r := find(v)
			used[r] = true
			if balance[v] < 0 {
				ends[r] -= balance[v]
			} else {
				ends[r] += balance[v]
			}
		}
	}
	threads := 0
	for v := 0; v < vertices; v++ {
		if used[v] {
			if ends[v] > 0 {
				threads += ends[v] / 2
			} else {
				threads++
			}
		}
	}
	fmt.Println(threads)
}
