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
	half    = cells / 2
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
	// Split the commuting moves in half and match their XOR effects.
	// Duplicate left effects retain only the cheapest number of moves.
	left := make(map[int]int, 1<<half)
	effect := 0
	for step := 0; step < 1<<half; step++ {
		if step > 0 {
			effect ^= moves[bits.TrailingZeros(uint(step))]
		}
		count := bits.OnesCount(uint(step ^ (step >> 1)))
		if old, exists := left[effect]; !exists || count < old {
			left[effect] = count
		}
	}
	best := cells + 1
	effect = 0
	for step := 0; step < 1<<half; step++ {
		if step > 0 {
			effect ^= moves[half+bits.TrailingZeros(uint(step))]
		}
		count := bits.OnesCount(uint(step ^ (step >> 1)))
		for _, target := range []int{board ^ effect, board ^ all ^ effect} {
			if other, exists := left[target]; exists && count+other < best {
				best = count + other
			}
		}
	}
	if best > cells {
		fmt.Println("Impossible")
	} else {
		fmt.Println(best)
	}
}
