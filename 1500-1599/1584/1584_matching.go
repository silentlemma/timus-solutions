package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

const (
	corners = 4 // cells in a group of mirror positions
	inf     = 1 << 29
	letters = 26
)

// hungarian gives the least total cost of giving each row its own column of
// a square matrix, by the potentials method in O(n^3)
func hungarian(cost [][]int) int {
	n := len(cost)
	u, v := make([]int, n+1), make([]int, n+1)
	owner, prev := make([]int, n+1), make([]int, n+1)
	for row := 1; row <= n; row++ {
		owner[0] = row
		col0 := 0
		least := make([]int, n+1)
		for i := range least {
			least[i] = inf
		}
		used := make([]bool, n+1)
		for owner[col0] != 0 {
			used[col0] = true
			r, delta, col1 := owner[col0], inf, 0
			for c := 1; c <= n; c++ {
				if used[c] {
					continue
				}
				if reduced := cost[r-1][c-1] - u[r] - v[c]; reduced < least[c] {
					least[c], prev[c] = reduced, col0
				}
				if least[c] < delta {
					delta, col1 = least[c], c
				}
			}
			for c := 0; c <= n; c++ {
				if used[c] {
					u[owner[c]] += delta
					v[c] -= delta
				} else {
					least[c] -= delta
				}
			}
			col0 = col1
		}
		for col0 != 0 {
			col1 := prev[col0]
			owner[col0] = owner[col1]
			col0 = col1
		}
	}
	return -v[0]
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, m int
	fmt.Fscan(in, &n, &m)
	grid := make([]string, n)
	for i := range grid {
		fmt.Fscan(in, &grid[i])
	}
	// every row and column symmetric means the four mirror images of a cell
	// hold one kind of statue; each group then gets one kind
	var groups []string
	for i := 0; i < n/2; i++ {
		for j := 0; j < m/2; j++ {
			far, low := m-1-j, n-1-i
			groups = append(groups, string([]byte{grid[i][j], grid[i][far], grid[low][j], grid[low][far]}))
		}
	}
	// a kind with c statues fills c / 4 groups; one column per such place
	var count [letters]int
	for _, row := range grid {
		for _, c := range row {
			count[c-'a']++
		}
	}
	var slots []string
	for k := 0; k < letters; k++ {
		for t := 0; t < count[k]/corners; t++ {
			slots = append(slots, string(rune('a'+k)))
		}
	}
	// a statue not already in place is carried once, and a cycle of k statues
	// takes k carries, so the answer is the number of statues that change
	cost := make([][]int, len(groups))
	for g, group := range groups {
		cost[g] = make([]int, len(slots))
		for s, kind := range slots {
			cost[g][s] = corners - strings.Count(group, kind)
		}
	}
	fmt.Println(hungarian(cost))
}
