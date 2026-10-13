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
	board := make([][]int, size)
	for r := range board {
		board[r] = make([]int, size)
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
					board[r][c] = count
					stack = append(stack, square{r0, c0, half, r, c})
				}
			}
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for _, row := range board {
		for c, v := range row {
			out.WriteString(strconv.Itoa(v))
			if c+1 < size {
				out.WriteByte(' ')
			} else {
				out.WriteByte('\n')
			}
		}
	}
}
