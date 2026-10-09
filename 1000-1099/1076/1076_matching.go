package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

// hungarian returns the smallest total cost of a perfect matching of rows to
// columns, with potentials u, v kept so that reduced costs stay non-negative
func hungarian(cost [][]int, n int) int {
	u := make([]int, n+1)
	v := make([]int, n+1)
	owner := make([]int, n+1)
	way := make([]int, n+1)
	for row := 1; row <= n; row++ {
		owner[0] = row
		col := 0
		low := make([]int, n+1)
		for j := range low {
			low[j] = math.MaxInt64
		}
		used := make([]bool, n+1)
		for {
			used[col] = true
			r, next, delta := owner[col], 0, math.MaxInt64
			for j := 1; j <= n; j++ {
				if !used[j] {
					cur := cost[r-1][j-1] - u[r] - v[j]
					if cur < low[j] {
						low[j], way[j] = cur, col
					}
					if low[j] < delta {
						delta, next = low[j], j
					}
				}
			}
			for j := 0; j <= n; j++ {
				if used[j] {
					u[owner[j]] += delta
					v[j] -= delta
				} else {
					low[j] -= delta
				}
			}
			col = next
			if owner[col] == 0 {
				break
			}
		}
		for col != 0 {
			prev := way[col]
			owner[col] = owner[prev]
			col = prev
		}
	}
	return -v[0]
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	cost := make([][]int, n)
	total := 0
	for i := range cost {
		cost[i] = make([]int, n)
		for j := range cost[i] {
			fmt.Fscan(in, &cost[i][j])
			total += cost[i][j]
			// type j stays in container i; everything else in its column moves
			cost[i][j] = -cost[i][j]
		}
	}
	fmt.Println(total + hungarian(cost, n))
}
