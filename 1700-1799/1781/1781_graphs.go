package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	var n int
	if _, err := fmt.Fscan(reader, &n); err != nil {
		return
	}
	grid := make([][]int, n)
	for i := range grid {
		grid[i] = make([]int, n)
		for j := range grid[i] {
			fmt.Fscan(reader, &grid[i][j])
		}
	}
	// renumbering contests and rooms together, room j must be free of every
	// later contest, so a contest that uses room b must come no later than
	// contest b: an order of the graph with an edge a -> b for each such use
	waiting := make([]int, n)
	for a := 0; a < n; a++ {
		for b := 0; b < n; b++ {
			if a != b && grid[a][b] == 1 {
				waiting[b]++
			}
		}
	}
	var ready, order []int
	for v := 0; v < n; v++ {
		if waiting[v] == 0 {
			ready = append(ready, v)
		}
	}
	for len(ready) > 0 {
		a := ready[0]
		ready = ready[1:]
		order = append(order, a)
		for b := 0; b < n; b++ {
			if a != b && grid[a][b] == 1 {
				waiting[b]--
				if waiting[b] == 0 {
					ready = append(ready, b)
				}
			}
		}
	}
	if len(order) < n {
		fmt.Println(-1)
		return
	}
	// each swap puts the next contest of the order in its place, so at most
	// n - 1 swaps are needed
	where, here := make([]int, n), make([]int, n)
	for v := 0; v < n; v++ {
		where[v], here[v] = v, v
	}
	var swaps [][2]int
	for i := 0; i < n; i++ {
		j := where[order[i]]
		if j == i {
			continue
		}
		swaps = append(swaps, [2]int{i + 1, j + 1})
		here[i], here[j] = here[j], here[i]
		where[here[i]], where[here[j]] = i, j
	}
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	fmt.Fprintln(writer, len(swaps))
	for _, s := range swaps {
		fmt.Fprintln(writer, s[0], s[1])
	}
}
