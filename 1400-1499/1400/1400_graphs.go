package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// distances: key presses from the start to every character, by breadth-first search.
func distances(n, m, start int) []int {
	dist := make([]int, n)
	for i := range dist {
		dist[i] = -1
	}
	dist[start] = 0
	queue := []int{start}
	for h := 0; h < len(queue); h++ {
		v := queue[h]
		// left and right run on through the rows; up and down stop at the edges
		up, down := v, v
		if v >= m {
			up = v - m
		}
		if v+m < n {
			down = v + m
		}
		for _, u := range []int{(v + n - 1) % n, (v + 1) % n, up, down} {
			if dist[u] < 0 {
				dist[u] = dist[v] + 1
				queue = append(queue, u)
			}
		}
	}
	return dist
}

func main() {
	var n, m int
	fmt.Scan(&n, &m)
	var best []int
	bestSum := -1
	for s := 0; s < n; s++ {
		d := distances(n, m, s)
		sum := 0
		for _, x := range d {
			sum += x
		}
		if bestSum < 0 || sum < bestSum {
			bestSum, best = sum, d
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	fmt.Fprintf(out, "Mean = %.2f\n", float64(bestSum)/float64(n))
	for r := 0; r < n; r += m {
		end := r + m
		if end > n {
			end = n
		}
		parts := make([]string, 0, m)
		for _, x := range best[r:end] {
			parts = append(parts, strconv.Itoa(x))
		}
		fmt.Fprintln(out, strings.Join(parts, " "))
	}
}
