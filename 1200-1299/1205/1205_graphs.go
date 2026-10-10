package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var walk, metro float64
	var n int
	fmt.Fscan(in, &walk, &metro, &n)
	total, start, goal := n+2, n, n+1
	x, y := make([]float64, total), make([]float64, total)
	for i := 0; i < n; i++ {
		fmt.Fscan(in, &x[i], &y[i])
	}
	linked := make([][]bool, total)
	for i := range linked {
		linked[i] = make([]bool, total)
	}
	for {
		var a, b int
		fmt.Fscan(in, &a, &b)
		if a == 0 && b == 0 {
			break
		}
		linked[a-1][b-1], linked[b-1][a-1] = true, true
	}
	fmt.Fscan(in, &x[start], &y[start], &x[goal], &y[goal])
	// nodes: the stations, then A and B; the subway is never slower than
	// walking, so a linked pair always goes by train
	dist := make([]float64, total)
	prev := make([]int, total)
	done := make([]bool, total)
	for i := range dist {
		dist[i] = math.Inf(1)
	}
	dist[start] = 0
	for step := 0; step < total; step++ {
		u := -1
		for v := 0; v < total; v++ {
			if !done[v] && (u < 0 || dist[v] < dist[u]) {
				u = v
			}
		}
		done[u] = true
		for v := 0; v < total; v++ {
			if done[v] {
				continue
			}
			speed := walk
			if linked[u][v] {
				speed = metro
			}
			d := math.Hypot(x[v]-x[u], y[v]-y[u]) / speed
			if dist[u]+d < dist[v] {
				dist[v], prev[v] = dist[u]+d, u
			}
		}
	}
	var path []int
	for v := prev[goal]; v != start; v = prev[v] {
		path = append(path, v+1)
	}
	fmt.Printf("%.10f\n%d", dist[goal], len(path))
	for i := len(path) - 1; i >= 0; i-- {
		fmt.Printf(" %d", path[i])
	}
	fmt.Println()
}
