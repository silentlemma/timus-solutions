package main

import "fmt"

const (
	size  = 4
	cells = size * size
)

func main() {
	// the board as 16 bits, bit r * 4 + c set for a black piece
	board := 0
	for r := 0; r < size; r++ {
		var row string
		fmt.Scan(&row)
		for c := 0; c < size; c++ {
			if row[c] == 'b' {
				board |= 1 << uint(r*size+c)
			}
		}
	}
	// the pieces turned by a move at each cell
	var move [cells]int
	dr := []int{0, 1, -1, 0, 0}
	dc := []int{0, 0, 0, 1, -1}
	for r := 0; r < size; r++ {
		for c := 0; c < size; c++ {
			m := 0
			for d := range dr {
				rr, cc := r+dr[d], c+dc[d]
				if rr >= 0 && rr < size && cc >= 0 && cc < size {
					m |= 1 << uint(rr*size+cc)
				}
			}
			move[r*size+c] = m
		}
	}
	// moves commute and a move made twice cancels, so a solution is a set of
	// cells: try all 2^16 sets
	all := 1<<cells - 1
	best := -1
	for set := 0; set <= all; set++ {
		b, count := board, 0
		for i := 0; i < cells; i++ {
			if set>>uint(i)&1 == 1 {
				b ^= move[i]
				count++
			}
		}
		if (b == 0 || b == all) && (best < 0 || count < best) {
			best = count
		}
	}
	if best < 0 {
		fmt.Println("Impossible")
	} else {
		fmt.Println(best)
	}
}
