package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	adj := make([][]int, n+1)
	for v := 1; v <= n; v++ {
		for {
			var u int
			fmt.Fscan(in, &u)
			if u == 0 {
				break
			}
			adj[v] = append(adj[v], u)
		}
	}
	// colour a BFS tree of every component by depth parity: each member has a
	// tree neighbour, its parent or a child, in the other team
	side := make([]int, n+1)
	for i := range side {
		side[i] = -1
	}
	for root := 1; root <= n; root++ {
		if side[root] >= 0 {
			continue
		}
		side[root] = 0
		queue := []int{root}
		for len(queue) > 0 {
			v := queue[0]
			queue = queue[1:]
			for _, u := range adj[v] {
				if side[u] < 0 {
					side[u] = 1 - side[v]
					queue = append(queue, u)
				}
			}
		}
	}
	var team []string
	for v := 1; v <= n; v++ {
		if side[v] == 0 {
			team = append(team, strconv.Itoa(v))
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	fmt.Fprintln(out, len(team))
	for i, s := range team {
		if i > 0 {
			out.WriteString(" ")
		}
		out.WriteString(s)
	}
	out.WriteString("\n")
}
