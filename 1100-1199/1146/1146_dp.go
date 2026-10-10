package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	grid := make([][]int, n)
	for r := range grid {
		grid[r] = make([]int, n)
		for c := range grid[r] {
			fmt.Fscan(in, &grid[r][c])
		}
	}
	best := grid[0][0]
	for top := 0; top < n; top++ {
		// column sums of the rows from top to bottom, then the best run of
		// neighbouring columns by Kadane's scan
		cols := make([]int, n)
		for bottom := top; bottom < n; bottom++ {
			run := 0
			for c := 0; c < n; c++ {
				cols[c] += grid[bottom][c]
				if run < 0 {
					run = cols[c]
				} else {
					run += cols[c]
				}
				if run > best {
					best = run
				}
			}
		}
	}
	fmt.Println(best)
}
