package main

import (
	"fmt"
	"math/bits"
)

const (
	size    = 4
	pattern = 3
	cells   = size * size
	all     = 1<<cells - 1
)

func main() {
	rows := make([]string, size)
	pat := make([]string, pattern)
	for i := range rows {
		fmt.Scan(&rows[i])
	}
	for i := range pat {
		fmt.Scan(&pat[i])
	}
	board := 0
	for r := 0; r < size; r++ {
		for c := 0; c < size; c++ {
			if rows[r][c] == 'B' {
				board |= 1 << (r*size + c)
			}
		}
	}
	// the flips of a move in each cell, the pattern clipped at the edges
	var moves [cells]int
	for r := 0; r < size; r++ {
		for c := 0; c < size; c++ {
			for dr := 0; dr < pattern; dr++ {
				for dc := 0; dc < pattern; dc++ {
					rr, cc := r+dr-1, c+dc-1
					if pat[dr][dc] == '1' && rr >= 0 && rr < size && cc >= 0 && cc < size {
						moves[r*size+c] |= 1 << (rr*size + cc)
					}
				}
			}
		}
	}
	// moves commute and a second move in a cell undoes the first, so a
	// solution is a set of cells; flips[s] is the effect of the set s
	flips := make([]int, 1<<cells)
	best := -1
	for s := 0; s < 1<<cells; s++ {
		if s > 0 {
			flips[s] = flips[s&(s-1)] ^ moves[bits.TrailingZeros(uint(s))]
		}
		if flips[s] == board || flips[s] == board^all {
			if count := bits.OnesCount(uint(s)); best < 0 || count < best {
				best = count
			}
		}
	}
	if best < 0 {
		fmt.Println("Impossible")
	} else {
		fmt.Println(best)
	}
}
