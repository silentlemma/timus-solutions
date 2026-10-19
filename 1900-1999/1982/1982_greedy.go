package main

import (
	"bufio"
	"fmt"
	"os"
)

const infinity int64 = 1 << 60

func solve(cost [][]int64, plants []int) int64 {
	n := len(cost)
	best := make([]int64, n)
	used := make([]bool, n)
	for i := range best {
		best[i] = infinity
	}
	for _, v := range plants {
		best[v] = 0
	}
	var answer int64
	for step := 0; step < n; step++ {
		vertex := -1
		for v := 0; v < n; v++ {
			if !used[v] && (vertex < 0 || best[v] < best[vertex]) {
				vertex = v
			}
		}
		answer += best[vertex]
		used[vertex] = true
		for v, price := range cost[vertex] {
			if !used[v] && price < best[v] {
				best[v] = price
			}
		}
	}
	return answer
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, k int
	if _, err := fmt.Fscan(in, &n, &k); err != nil {
		return
	}
	plants := make([]int, k)
	for i := range plants {
		fmt.Fscan(in, &plants[i])
		plants[i]--
	}
	cost := make([][]int64, n)
	for i := range cost {
		cost[i] = make([]int64, n)
		for j := range cost[i] {
			fmt.Fscan(in, &cost[i][j])
		}
	}
	out := bufio.NewWriter(os.Stdout)
	fmt.Fprintln(out, solve(cost, plants))
	out.Flush()
}
