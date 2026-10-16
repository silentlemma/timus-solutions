package main

import (
	"bufio"
	"fmt"
	"os"
)

const side = 8

func main() {
	reader := bufio.NewReader(os.Stdin)
	var grid, score [side][side]int64
	for r := 0; r < side; r++ {
		for c := 0; c < side; c++ {
			if _, err := fmt.Fscan(reader, &grid[r][c]); err != nil {
				return
			}
		}
	}
	// moving from u to a neighbour v with weight w(v) / W(u), where W(u) sums
	// the weights around u, the walk is balanced by w(u) W(u) in every cell,
	// and after so many steps it has settled into that distribution
	var total int64
	for r := 0; r < side; r++ {
		for c := 0; c < side; c++ {
			var around int64
			for y := r - 1; y <= r+1; y++ {
				for x := c - 1; x <= c+1; x++ {
					if y >= 0 && y < side && x >= 0 && x < side && (y != r || x != c) {
						around += grid[y][x]
					}
				}
			}
			score[r][c] = grid[r][c] * around
			total += score[r][c]
		}
	}
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	for r := 0; r < side; r++ {
		for c := 0; c < side; c++ {
			if c > 0 {
				writer.WriteByte(' ')
			}
			fmt.Fprintf(writer, "%.15f", float64(score[r][c])/float64(total))
		}
		writer.WriteByte('\n')
	}
}
