package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const inf = 1000000000

var (
	n, k, size int
	road       [][]int
)

func door(s string) (int, int) {
	parts := strings.SplitN(s, ".", 2)
	h, _ := strconv.Atoi(parts[0])
	d, _ := strconv.Atoi(parts[1])
	return h, d
}

func equal(a, b [][]int) bool {
	for i := range a {
		for j := range a[i] {
			if a[i][j] != b[i][j] {
				return false
			}
		}
	}
	return true
}

// outerDistances gives the distances between the doors of the outer house
// when walking through an inner house from door i to door j costs inside[i][j].
func outerDistances(inside [][]int) [][]int {
	weight := make([][]int, size)
	for i := range weight {
		weight[i] = append([]int(nil), road[i]...)
	}
	for h := 1; h <= k; h++ {
		for i := 0; i < n; i++ {
			for j := 0; j < n; j++ {
				if inside[i][j] < weight[h*n+i][h*n+j] {
					weight[h*n+i][h*n+j] = inside[i][j]
				}
			}
		}
	}
	result := make([][]int, n)
	dist := make([]int, size)
	done := make([]bool, size)
	for s := 0; s < n; s++ {
		// Dijkstra on the dense graph, O(size^2)
		for v := range dist {
			dist[v], done[v] = inf, false
		}
		dist[s] = 0
		for step := 0; step < size; step++ {
			u := -1
			for v := 0; v < size; v++ {
				if !done[v] && dist[v] < inf && (u < 0 || dist[v] < dist[u]) {
					u = v
				}
			}
			if u < 0 {
				break
			}
			done[u] = true
			for v := 0; v < size; v++ {
				if weight[u][v] < inf && dist[u]+weight[u][v] < dist[v] {
					dist[v] = dist[u] + weight[u][v]
				}
			}
		}
		result[s] = append([]int(nil), dist[:n]...)
	}
	return result
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var m int
	if _, err := fmt.Fscan(in, &n, &k, &m); err != nil {
		return
	}
	size = (k + 1) * n // door d of house h is h * n + d
	road = make([][]int, size)
	for i := range road {
		road[i] = make([]int, size)
		for j := range road[i] {
			road[i][j] = inf
		}
	}
	for i := 0; i < m; i++ {
		var left, dash, right string
		fmt.Fscan(in, &left, &dash, &right)
		h1, d1 := door(left)
		h2, d2 := door(right)
		u, v := h1*n+d1, h2*n+d2
		road[u][v], road[v][u] = 1, 1
	}
	var source, sink int
	fmt.Fscan(in, &source, &sink)
	// Round t allows paths nested t houses deep; the distances only shrink,
	// and once a round changes nothing, no later round will.
	opaque := make([][]int, n)
	for i := range opaque {
		opaque[i] = make([]int, n)
		for j := range opaque[i] {
			opaque[i][j] = inf
		}
	}
	inside := outerDistances(opaque)
	for {
		next := outerDistances(inside)
		if equal(next, inside) {
			break
		}
		inside = next
	}
	if inside[source][sink] >= inf {
		fmt.Println("no solution")
	} else {
		fmt.Println(inside[source][sink])
	}
}
