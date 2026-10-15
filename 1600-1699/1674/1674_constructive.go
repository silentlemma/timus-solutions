package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	block    = 4            // rows or columns added at a time
	smallest = 4            // boards with a shorter side have no tour, apart from 2 x 2
	bottom   = smallest - 1 // the last row of a strip
)

type cell struct{ r, c int }

var (
	noTour  = cell{5, 5} // the one board with both sides at least 4 and no tour
	oddBase = cell{5, 9} // the base when both sides are of the form 4k + 1
)

// bases holds closed tours of small boards, as flat (row, column) lists
// ending at the start.
var bases = map[cell][]int{
	{5, 6}: {0, 0, 0, 1, 1, 2, 0, 2, 0, 3, 1, 3, 0, 4, 0, 5, 1, 5, 1, 4, 2, 5, 2, 4, 3, 5, 4, 5,
		4, 4, 3, 4, 2, 3, 2, 2, 3, 3, 3, 2, 4, 3, 4, 2, 3, 1, 4, 1, 4, 0, 3, 0, 2, 1, 2, 0,
		1, 1, 1, 0, 0, 0},
	{5, 7}: {0, 0, 0, 1, 1, 1, 0, 2, 0, 3, 1, 2, 2, 2, 2, 3, 3, 3, 2, 4, 1, 3, 0, 4, 1, 4, 0, 5,
		0, 6, 1, 6, 1, 5, 2, 6, 2, 5, 3, 6, 4, 6, 3, 5, 4, 5, 4, 4, 3, 4, 4, 3, 4, 2, 3, 2,
		4, 1, 4, 0, 3, 0, 3, 1, 2, 0, 2, 1, 1, 0, 0, 0},
	{6, 6}: {0, 0, 1, 0, 2, 1, 1, 2, 2, 2, 3, 1, 2, 0, 3, 0, 4, 1, 4, 0, 5, 0, 5, 1, 4, 2, 5, 2,
		5, 3, 4, 3, 5, 4, 5, 5, 4, 5, 4, 4, 3, 3, 3, 2, 2, 3, 3, 4, 3, 5, 2, 5, 2, 4, 1, 5,
		0, 5, 1, 4, 0, 4, 0, 3, 1, 3, 0, 2, 0, 1, 1, 1, 0, 0},
	{6, 7}: {0, 0, 0, 1, 1, 1, 0, 2, 0, 3, 1, 2, 2, 2, 1, 3, 1, 4, 0, 4, 1, 5, 0, 5, 0, 6, 1, 6,
		2, 5, 2, 6, 3, 6, 3, 5, 2, 4, 3, 3, 2, 3, 3, 2, 4, 3, 3, 4, 4, 5, 4, 6, 5, 6, 5, 5,
		4, 4, 5, 4, 5, 3, 4, 2, 5, 2, 4, 1, 5, 1, 5, 0, 4, 0, 3, 1, 3, 0, 2, 0, 2, 1, 1, 0,
		0, 0},
	{7, 7}: {0, 0, 0, 1, 1, 2, 0, 2, 0, 3, 1, 3, 2, 2, 3, 2, 3, 1, 4, 2, 3, 3, 3, 4, 2, 4, 2, 3,
		1, 4, 0, 4, 1, 5, 0, 5, 0, 6, 1, 6, 2, 5, 2, 6, 3, 6, 3, 5, 4, 6, 4, 5, 5, 6, 6, 6,
		6, 5, 5, 5, 4, 4, 4, 3, 5, 4, 6, 4, 5, 3, 6, 3, 6, 2, 5, 2, 5, 1, 6, 1, 6, 0, 5, 0,
		4, 1, 4, 0, 3, 0, 2, 1, 2, 0, 1, 0, 1, 1, 0, 0},
	{5, 9}: {0, 0, 0, 1, 1, 2, 0, 2, 0, 3, 1, 3, 0, 4, 1, 4, 2, 3, 2, 2, 3, 2, 3, 3, 2, 4, 2, 5,
		1, 5, 2, 6, 1, 6, 0, 5, 0, 6, 1, 7, 0, 7, 0, 8, 1, 8, 2, 7, 2, 8, 3, 8, 3, 7, 4, 8,
		4, 7, 3, 6, 4, 6, 3, 5, 4, 5, 4, 4, 3, 4, 4, 3, 4, 2, 3, 1, 4, 1, 4, 0, 3, 0, 2, 1,
		2, 0, 1, 0, 1, 1, 0, 0},
}

// strip is a closed tour of the 4 x m board: along the top two rows in a
// zigzag, down the right end, back along the bottom two rows, up the left.
func strip(m int) []cell {
	path := []cell{{0, 0}, {0, 1}, {1, 1}}
	for c := 2; c < m-1; c++ {
		path = append(path, cell{0, c})
		if c < m-2 {
			path = append(path, cell{1, c})
		}
	}
	path = append(path, cell{0, m - 1}, cell{1, m - 1}, cell{1, m - 2})
	path = append(path, cell{2, m - 1}, cell{bottom, m - 1})
	for c := m - 2; c > 1; c-- {
		path = append(path, cell{bottom, c}, cell{2, c})
	}
	path = append(path, cell{bottom, 1}, cell{bottom, 0}, cell{2, 0})
	return append(path, cell{2, 1}, cell{1, 0}, cell{0, 0})
}

func flip(path []cell) []cell {
	out := make([]cell, len(path))
	for i, p := range path {
		out[i] = cell{p.c, p.r}
	}
	return out
}

func base(n, m int) []cell {
	if n == smallest {
		return strip(m)
	}
	if m == smallest {
		return flip(strip(n))
	}
	flat, ok := bases[cell{n, m}]
	if !ok {
		flat = bases[cell{m, n}]
	}
	var path []cell
	for i := 0; i < len(flat); i += 2 {
		path = append(path, cell{flat[i], flat[i+1]})
	}
	if !ok {
		return flip(path)
	}
	return path
}

var grid [][]byte

// mark draws the move between cells a and b, or with ch = ' ' erases it.
func mark(a, b cell, ch byte) {
	if ch == 0 {
		switch {
		case a.r == b.r:
			ch = '-'
		case a.c == b.c:
			ch = '|'
		case b.r-a.r == b.c-a.c:
			ch = '\\'
		default:
			ch = '/'
		}
	}
	grid[a.r+b.r][a.c+b.c] = ch
}

func draw(path []cell, dr, dc int, swap bool) {
	for i := 0; i+1 < len(path); i++ {
		a, b := path[i], path[i+1]
		if swap {
			a, b = cell{a.c, a.r}, cell{b.c, b.r}
		}
		mark(cell{a.r + dr, a.c + dc}, cell{b.r + dr, b.c + dc}, 0)
	}
}

func main() {
	var n, m int
	fmt.Scan(&n, &m)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	grid = make([][]byte, 2*n-1)
	for y := range grid {
		grid[y] = make([]byte, 2*m-1)
		for x := range grid[y] {
			grid[y][x] = ' '
			if y%2 == 0 && x%2 == 0 {
				grid[y][x] = 'o'
			}
		}
	}
	switch {
	case n == 2 && m == 2:
		draw([]cell{{0, 0}, {0, 1}, {1, 1}, {1, 0}, {0, 0}}, 0, 0, false)
	case n < smallest || m < smallest || (cell{n, m}) == noTour:
		fmt.Fprintln(out, "No")
		return
	default:
		// a base board whose sides leave multiples of 4; two sides of the
		// form 4k + 1 start from 5 x 9 instead, as 5 x 5 has no tour
		bn, bm := smallest+(n-smallest)%block, smallest+(m-smallest)%block
		if n%block == 1 && m%block == 1 {
			bn, bm = oddBase.r, oddBase.c
			if m < oddBase.c {
				bn, bm = oddBase.c, oddBase.r
			}
		}
		draw(base(bn, bm), 0, 0, false)
		// each new 4-wide block has its own strip tour; three edges at the
		// seam are swapped for three others, which joins the two cycles
		for cur := bm; cur < m; cur += block {
			draw(strip(bn), 0, cur, true)
			mark(cell{0, cur - 1}, cell{1, cur - 1}, ' ')
			mark(cell{0, cur}, cell{1, cur}, ' ')
			mark(cell{2, cur}, cell{1, cur + 1}, ' ')
			mark(cell{0, cur - 1}, cell{1, cur}, 0)
			mark(cell{1, cur - 1}, cell{2, cur}, 0)
			mark(cell{0, cur}, cell{1, cur + 1}, 0)
		}
		for cur := bn; cur < n; cur += block {
			draw(strip(m), cur, 0, false)
			mark(cell{cur - 1, 0}, cell{cur - 1, 1}, ' ')
			mark(cell{cur, 0}, cell{cur, 1}, ' ')
			mark(cell{cur, 2}, cell{cur + 1, 1}, ' ')
			mark(cell{cur - 1, 0}, cell{cur, 1}, 0)
			mark(cell{cur - 1, 1}, cell{cur, 2}, 0)
			mark(cell{cur, 0}, cell{cur + 1, 1}, 0)
		}
	}
	fmt.Fprintln(out, "Yes")
	for _, row := range grid {
		out.Write(row)
		out.WriteByte('\n')
	}
}
