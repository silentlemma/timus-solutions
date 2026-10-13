package main

import (
	"bufio"
	"fmt"
	"os"
)

// bridgeless cubic maps with the whole border built, found by a search
var blocks = [][]string{
	{
		`O-O-O-O`,
		`|\|/ /|`,
		`O O O-O`,
		`|\   \|`,
		`O-O O O`,
		`|/ /|\|`,
		`O-O-O-O`,
	},
	{
		`O-O-O-O`,
		`|\ \|/|`,
		`O-O O O`,
		`| |  /|`,
		`O-O-O-O`,
		`|     |`,
		`O-O O-O`,
		`|/| |\|`,
		`O-O-O-O`,
	},
	{
		`O-O-O-O`,
		`|\|/ /|`,
		`O O O-O`,
		`|\   \|`,
		`O-O-O O`,
		`|   |\|`,
		`O-O O O`,
		`|/|/ \|`,
		`O O O O`,
		`|/ /|\|`,
		`O-O-O-O`,
	},
	{
		`O-O-O-O`,
		`|\ \|/|`,
		`O O O O`,
		`|\|\ /|`,
		`O O O-O`,
		`|\|   |`,
		`O-O O-O`,
		`|   |\|`,
		`O-O-O O`,
		`| |  \|`,
		`O-O O O`,
		`|/ /|\|`,
		`O-O-O-O`,
	},
	{
		`O-O-O-O-O-O`,
		`|\ \|  \|/|`,
		`O-O O-O O O`,
		`| |  /|  /|`,
		`O-O O O O-O`,
		`|/ /| |\ \|`,
		`O-O-O-O-O-O`,
	},
	{
		`O-O-O-O-O-O`,
		`|\ \ \ \|/|`,
		`O-O-O O O O`,
		`|    \|\ /|`,
		`O-O-O-O O O`,
		`| | |  / /|`,
		`O-O O O O-O`,
		`|/ /| |\ \|`,
		`O-O-O-O-O-O`,
	},
	{
		`O-O-O-O-O-O`,
		`|\|  \| |/|`,
		`O-O O O-O O`,
		`|  /|\   /|`,
		`O-O-O O O-O`,
		`|  / /|/  |`,
		`O O-O O O-O`,
		`|\ \ \|/ \|`,
		`O-O O O O O`,
		`|/ /|  /|\|`,
		`O-O-O-O-O-O`,
	},
	{
		`O-O-O-O-O-O`,
		`|\| |  \|/|`,
		`O-O O O O O`,
		`|  /|/|\ /|`,
		`O-O-O O-O O`,
		`|     |  /|`,
		`O-O-O O O-O`,
		`| | |\|\| |`,
		`O-O O O O-O`,
		`|  \|\ \  |`,
		`O-O O O O-O`,
		`|/| | |\ \|`,
		`O-O-O-O-O-O`,
	},
	{
		`O-O-O-O-O-O-O-O`,
		`|\ \ \| | |/ /|`,
		`O-O O O O O O-O`,
		`|/ /| | |\ \ \|`,
		`O-O-O-O-O-O-O-O`,
	},
	{
		`O-O-O-O-O-O-O-O-O-O`,
		`|\ \ \|  \| |/ / /|`,
		`O-O O O O-O O O O-O`,
		`|/ /| | |\  | |\ \|`,
		`O-O-O-O-O-O-O-O-O-O`,
	},
	{
		`O-O-O-O-O-O-O-O-O-O-O-O`,
		`|\ \ \ \|/ /  | | |/ /|`,
		`O-O O O O O-O O-O O O-O`,
		`|/ /| |\  | |\ \ \ \ \|`,
		`O-O-O-O-O-O-O-O-O-O-O-O`,
	},
	{
		`O-O-O-O-O-O-O-O-O-O-O-O-O-O`,
		`|\ \| |/   \ \|/ /  |/ / /|`,
		`O-O O O O-O-O O O O-O O O-O`,
		`|/ / / /| | |  /| |\  |\ \|`,
		`O-O-O-O-O-O-O-O-O-O-O-O-O-O`,
	},
}

const minSide = 3
const flat = 3 // a strip this high needs at least flatStep columns
const flatStep = 8
const flatTop = 14
const step = 4
const wideTop = 6
const tallTop = 7
const noWorld = "Imaginary world"

func split(n, step, top int) []int {
	var parts []int
	for n > top {
		parts = append(parts, step)
		n -= step
	}
	return append(parts, n)
}

func shape(w, h int) []string {
	for _, b := range blocks {
		if len(b[0])/2+1 == w && len(b)/2+1 == h {
			return b
		}
	}
	return blocks[0]
}

func main() {
	var w, h int
	fmt.Scan(&w, &h)
	if w*h%2 == 1 || w < minSide || h < minSide {
		fmt.Println(noWorld)
		return
	}
	turned := w%2 == 1 // then h is even: build the turned map
	if turned {
		w, h = h, w
	}
	var widths, heights []int
	if h == flat {
		if w < flatStep {
			fmt.Println(noWorld)
			return
		}
		widths, heights = split(w, flatStep, flatTop), []int{flat}
	} else {
		widths, heights = split(w, step, wideTop), split(h, step, tallTop)
	}
	grid := make([][]byte, 2*h-1)
	for r := range grid {
		grid[r] = make([]byte, 2*w-1)
		for c := range grid[r] {
			grid[r][c] = ' '
		}
	}
	top := 0
	for j, bh := range heights {
		left := 0
		for i, bw := range widths {
			y, x := 2*top, 2*left
			for r, row := range shape(bw, bh) {
				copy(grid[y+r][x:], row)
			}
			if i > 0 {
				// two vertical bridges at the seam, in the lowest two rows,
				// give way to two horizontal ones
				z := 2 * (top + bh - 2)
				grid[z+1][x-2], grid[z+1][x] = ' ', ' '
				grid[z][x-1], grid[z+2][x-1] = '-', '-'
			}
			left += bw
		}
		if j > 0 {
			// the same exchange across a horizontal seam, in the last two columns
			y, x := 2*top, 2*(w-2)
			grid[y-2][x+1], grid[y][x+1] = ' ', ' '
			grid[y-1][x], grid[y-1][x+2] = '|', '|'
		}
		top += bh
	}
	if turned {
		flipped := make([][]byte, len(grid[0]))
		for c := range flipped {
			flipped[c] = make([]byte, len(grid))
			for r := range grid {
				ch := grid[r][c]
				if ch == '-' {
					ch = '|'
				} else if ch == '|' {
					ch = '-'
				}
				flipped[c][r] = ch
			}
		}
		grid = flipped
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for _, row := range grid {
		out.Write(row)
		out.WriteByte('\n')
	}
}
