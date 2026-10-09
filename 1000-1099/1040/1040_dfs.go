package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

type flight struct{ to, id int }

var (
	adj     [][]flight
	number  []int
	visited []bool
	counter int
)

// dfs numbers the flights in the order the search meets them; the first
// flight met at a new airport right after its entry flight k gets k + 1
func dfs(v int) {
	visited[v] = true
	for _, f := range adj[v] {
		if number[f.id] == 0 {
			counter++
			number[f.id] = counter
			if !visited[f.to] {
				dfs(f.to)
			}
		}
	}
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, m int
	fmt.Fscan(in, &n, &m)
	adj = make([][]flight, n+1)
	number = make([]int, m)
	visited = make([]bool, n+1)
	for e := 0; e < m; e++ {
		var a, b int
		fmt.Fscan(in, &a, &b)
		adj[a] = append(adj[a], flight{b, e})
		adj[b] = append(adj[b], flight{a, e})
	}
	dfs(1)
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	w.WriteString("YES\n")
	for e := 0; e < m; e++ {
		if e > 0 {
			w.WriteString(" ")
		}
		w.WriteString(strconv.Itoa(number[e]))
	}
	w.WriteString("\n")
}
