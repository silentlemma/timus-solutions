package main

import (
	"bufio"
	"fmt"
	"os"
)

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	knows := make([][]bool, n)
	for i := range knows {
		knows[i] = make([]bool, n)
		for {
			var j int
			fmt.Fscan(in, &j)
			if j == 0 {
				break
			}
			knows[i][j-1] = true
		}
	}
	// two people who do not both know each other must be in different
	// teams, so these pairs must form a bipartite graph; each component
	// gives two sides, and one side of each goes to the first team
	side := make([]int, n)
	for i := range side {
		side[i] = -1
	}
	var parts [][2][]int
	for s := 0; s < n; s++ {
		if side[s] >= 0 {
			continue
		}
		side[s] = 0
		var groups [2][]int
		queue := []int{s}
		for h := 0; h < len(queue); h++ {
			v := queue[h]
			groups[side[v]] = append(groups[side[v]], v)
			for u := 0; u < n; u++ {
				if u != v && !(knows[v][u] && knows[u][v]) {
					if side[u] < 0 {
						side[u] = 1 - side[v]
						queue = append(queue, u)
					} else if side[u] == side[v] {
						fmt.Println("No solution")
						return
					}
				}
			}
		}
		parts = append(parts, groups)
	}
	// reach[k][size]: which side of part k-1 gives the first team that size,
	// or -1 when it cannot be reached
	reach := make([][]int, len(parts)+1)
	for k := range reach {
		reach[k] = make([]int, n+1)
		for s := range reach[k] {
			reach[k][s] = -1
		}
	}
	reach[0][0] = 0
	for k, groups := range parts {
		for size := 0; size <= n; size++ {
			if reach[k][size] < 0 {
				continue
			}
			for pick := 0; pick < 2; pick++ {
				if next := size + len(groups[pick]); reach[k+1][next] < 0 {
					reach[k+1][next] = pick
				}
			}
		}
	}
	size := -1
	for s := 0; s <= n; s++ {
		if reach[len(parts)][s] >= 0 && (size < 0 || abs(2*s-n) < abs(2*size-n)) {
			size = s
		}
	}
	var team [2][]int
	for k := len(parts) - 1; k >= 0; k-- {
		pick := reach[k+1][size]
		team[0] = append(team[0], parts[k][pick]...)
		team[1] = append(team[1], parts[k][1-pick]...)
		size -= len(parts[k][pick])
	}
	for _, t := range team {
		fmt.Print(len(t))
		for _, v := range t {
			fmt.Print(" ", v+1)
		}
		fmt.Println()
	}
}
