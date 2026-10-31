package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

type square struct{ top, left, side, holeRow, holeCol int }

func main() {
	var n, x, y int
	fmt.Scan(&n, &x, &y)
	size, count := 1<<uint(n), 0
	// n <= 9 gives at most 87381 labels, which fit in int32.
	board := make([][]int32, size)
	for r := range board {
		board[r] = make([]int32, size)
	}
	// each square has one cell that is already taken: the hole or a piece of
	// the tromino in the middle of the square above it
	stack := []square{{0, 0, size, x - 1, y - 1}}
	for len(stack) > 0 {
		s := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		if s.side == 1 {
			continue
		}
		half := s.side / 2
		count++
		for dr := 0; dr < 2; dr++ {
			for dc := 0; dc < 2; dc++ {
				r0, c0 := s.top+dr*half, s.left+dc*half
				if r0 <= s.holeRow && s.holeRow < r0+half && c0 <= s.holeCol && s.holeCol < c0+half {
					stack = append(stack, square{r0, c0, half, s.holeRow, s.holeCol})
				} else {
					// the cell of this quarter next to the middle of the square
					r, c := s.top+half-1+dr, s.left+half-1+dc
					board[r][c] = int32(count)
					stack = append(stack, square{r0, c0, half, r, c})
				}
			}
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	// reuse decimal storage rather than allocate a string for every cell.
	const decimalBuffer = 10
	digits := make([]byte, 0, decimalBuffer)
	for _, row := range board {
		for c, v := range row {
			digits = strconv.AppendInt(digits[:0], int64(v), 10)
			out.Write(digits)
			if c+1 < size {
				out.WriteByte(' ')
			} else {
				out.WriteByte('\n')
			}
		}
	}
}
