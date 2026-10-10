package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, m int
	fmt.Fscan(in, &n, &m)
	total := 2 * n
	near := make([][]int, total+1)
	for k := 0; k < m; k++ {
		var a, b int
		fmt.Fscan(in, &a, &b)
		near[a] = append(near[a], b)
		near[b] = append(near[b], a)
	}
	// similar problems must go to different rounds: colour every component of
	// the conflict graph in two colours, or give up on an odd cycle
	colour := make([]int, total+1)
	for v := range colour {
		colour[v] = -1
	}
	var comps [][]int
	for start := 1; start <= total; start++ {
		if colour[start] >= 0 {
			continue
		}
		colour[start] = 0
		members, stack := []int{start}, []int{start}
		for len(stack) > 0 {
			v := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			for _, w := range near[v] {
				if colour[w] < 0 {
					colour[w] = 1 - colour[v]
					members = append(members, w)
					stack = append(stack, w)
				} else if colour[w] == colour[v] {
					fmt.Println("IMPOSSIBLE")
					return
				}
			}
		}
		comps = append(comps, members)
	}
	// each component sends one of its colours to the first round; reach[k][s]
	// tells whether the first k components can give it s problems
	c := len(comps)
	sizes := make([][2]int, c)
	for k, members := range comps {
		for _, v := range members {
			sizes[k][colour[v]]++
		}
	}
	reach := make([][]bool, c+1)
	for k := range reach {
		reach[k] = make([]bool, n+1)
	}
	reach[0][0] = true
	for k := 0; k < c; k++ {
		for s := 0; s <= n; s++ {
			if reach[k][s] {
				for _, size := range sizes[k] {
					if s+size <= n {
						reach[k+1][s+size] = true
					}
				}
			}
		}
	}
	if !reach[c][n] {
		fmt.Println("IMPOSSIBLE")
		return
	}
	first := make([]bool, total+1)
	for k, s := c-1, n; k >= 0; k-- {
		side := 1
		if s >= sizes[k][0] && reach[k][s-sizes[k][0]] {
			side = 0
		}
		for _, v := range comps[k] {
			if colour[v] == side {
				first[v] = true
			}
		}
		s -= sizes[k][side]
	}
	for round := 0; round < 2; round++ {
		var parts []string
		for v := 1; v <= total; v++ {
			if first[v] == (round == 0) {
				parts = append(parts, strconv.Itoa(v))
			}
		}
		fmt.Println(strings.Join(parts, " "))
	}
}
