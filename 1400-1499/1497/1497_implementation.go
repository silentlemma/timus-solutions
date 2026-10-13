package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	n    int
	grid []string
)

// slides tells whether the black piece moves by (di, dj): no white cell
// may lie on that side of a black one in the same column or row
func slides(di, dj int) bool {
	for k := 0; k < n; k++ {
		seenWhite := false
		for t := 0; t < n; t++ {
			// walk the line from the side the piece moves towards
			step := t
			if di+dj > 0 {
				step = n - 1 - t
			}
			i, j := k, step
			if di != 0 {
				i, j = step, k
			}
			if grid[i][j] == '0' {
				seenWhite = true
			} else if seenWhite {
				return false
			}
		}
	}
	return true
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Fscan(reader, &n)
	grid = make([]string, n)
	for i := range grid {
		fmt.Fscan(reader, &grid[i])
	}
	// a sliding direction for either piece is the opposite one for the
	// other; a diagonal slide works only if both of its axis slides do, so
	// trying the four axis directions for the black piece is enough
	if slides(-1, 0) || slides(1, 0) || slides(0, -1) || slides(0, 1) {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
