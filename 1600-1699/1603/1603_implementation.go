package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	side    = 4
	cells   = side * side
	letters = 26
)

var (
	grid, word string
	nearCells  [cells][]int
	dead       map[int]bool // (visited cells, last cell) that cannot finish the word
)

// walk continues from cell, which holds word[i-1]; mask is every cell used so far.
func walk(cell, mask, i int) bool {
	if i == len(word) {
		return true
	}
	key := mask*cells + cell
	if dead[key] {
		return false
	}
	for _, next := range nearCells[cell] {
		if mask>>uint(next)&1 == 0 && grid[next] == word[i] && walk(next, mask|1<<uint(next), i+1) {
			return true
		}
	}
	dead[key] = true
	return false
}

func found() bool {
	var have, need [letters]int
	for i := 0; i < len(grid); i++ {
		have[grid[i]-'a']++
	}
	for i := 0; i < len(word); i++ {
		need[word[i]-'a']++
		if need[word[i]-'a'] > have[word[i]-'a'] {
			return false
		}
	}
	dead = make(map[int]bool)
	for c := 0; c < cells; c++ {
		if grid[c] == word[0] && walk(c, 1<<uint(c), 1) {
			return true
		}
	}
	return false
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for r := 0; r < side; r++ {
		var row string
		fmt.Fscan(in, &row)
		grid += row
	}
	for c := 0; c < cells; c++ {
		r, col := c/side, c%side
		if r > 0 {
			nearCells[c] = append(nearCells[c], c-side)
		}
		if r < side-1 {
			nearCells[c] = append(nearCells[c], c+side)
		}
		if col > 0 {
			nearCells[c] = append(nearCells[c], c-1)
		}
		if col < side-1 {
			nearCells[c] = append(nearCells[c], c+1)
		}
	}
	var n int
	fmt.Fscan(in, &n)
	for i := 0; i < n; i++ {
		fmt.Fscan(in, &word)
		answer := "NO"
		if found() {
			answer = "YES"
		}
		fmt.Fprintf(out, "%s: %s\n", word, answer)
	}
}
