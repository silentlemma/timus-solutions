package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const (
	inf        = 1 << 30
	endOfInput = -1
)

// path returns the vertices of the shortest path u..v using next hops.
func path(u, v int, next [][]int) []int {
	res := []int{u}
	for u != v {
		u = next[u][v]
		res = append(res, u)
	}
	return res
}

func solve(n, m int, in *bufio.Reader, out *bufio.Writer) {
	edge := make([][]int, n) // the lightest direct road between two vertices
	dist := make([][]int, n)
	next := make([][]int, n)
	for i := range edge {
		edge[i], dist[i], next[i] = make([]int, n), make([]int, n), make([]int, n)
		for j := range edge[i] {
			if i != j {
				edge[i][j], dist[i][j] = inf, inf
			}
			next[i][j] = j
		}
	}
	for e := 0; e < m; e++ {
		var a, b, l int
		fmt.Fscan(in, &a, &b, &l)
		a, b = a-1, b-1
		if l < edge[a][b] {
			edge[a][b], edge[b][a] = l, l
			dist[a][b], dist[b][a] = l, l
		}
	}

	// Floyd-Warshall; before vertex k becomes an intermediate, dist[i][j] uses
	// only vertices below k, so i..j plus j-k-i is a simple cycle through k.
	best := inf
	var cycle []int
	for k := 0; k < n; k++ {
		for i := 0; i < k; i++ {
			if edge[i][k] == inf {
				continue
			}
			for j := i + 1; j < k; j++ {
				if edge[k][j] == inf || dist[i][j] == inf {
					continue
				}
				if c := dist[i][j] + edge[i][k] + edge[k][j]; c < best {
					best, cycle = c, append(path(i, j, next), k)
				}
			}
		}
		for i := 0; i < n; i++ {
			if dist[i][k] == inf {
				continue
			}
			for j := 0; j < n; j++ {
				if d := dist[i][k] + dist[k][j]; d < dist[i][j] {
					dist[i][j], next[i][j] = d, next[i][k]
				}
			}
		}
	}

	if best == inf {
		out.WriteString("No solution.\n")
		return
	}
	for i, v := range cycle {
		if i > 0 {
			out.WriteByte(' ')
		}
		out.WriteString(strconv.Itoa(v + 1))
	}
	out.WriteByte('\n')
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for {
		var n, m int
		if _, err := fmt.Fscan(in, &n); err != nil || n == endOfInput {
			return
		}
		fmt.Fscan(in, &m)
		solve(n, m, in, out)
	}
}
