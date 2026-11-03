package main

import (
	"bufio"
	"fmt"
	"os"
)

const maxSide = 50
const maxSquared = 2 * maxSide * maxSide
const colourXor = byte('W' ^ 'B')

type offset struct{ dr, dc int }

func main() {
	in := bufio.NewReader(os.Stdin)
	var m, n int
	fmt.Fscan(in, &m, &n)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	if m == 0 || n == 0 {
		for r := 0; r < m; r++ {
			fmt.Fprintln(out)
		}
		return
	}
	board := make([][]byte, m)
	for r := range board {
		var row string
		fmt.Fscan(in, &row)
		board[r] = []byte(row)
	}
	square := make([]bool, maxSquared)
	for k := 0; k*k < maxSquared; k++ {
		square[k*k] = true
	}
	var offsets []offset
	for dr := 1 - m; dr < m; dr++ {
		for dc := 1 - n; dc < n; dc++ {
			if square[dr*dr+dc*dc] {
				offsets = append(offsets, offset{dr, dc})
			}
		}
	}
	// Only odd visits remain after cancelling pairs of identical flips.
	for r := 0; r < m; r++ {
		for c := 0; c < n; c++ {
			var visits int
			fmt.Fscan(in, &visits)
			if visits&1 != 0 {
				for _, delta := range offsets {
					a, b := r+delta.dr, c+delta.dc
					if a >= 0 && a < m && b >= 0 && b < n {
						board[a][b] ^= colourXor
					}
				}
			}
		}
	}
	for _, row := range board {
		fmt.Fprintln(out, string(row))
	}
}
