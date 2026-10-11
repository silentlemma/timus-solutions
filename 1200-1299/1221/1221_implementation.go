package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	n     int
	grid  [][]int
	black [][]int // black[i][j]: black cells among the first j of row i
	in    = bufio.NewReader(os.Stdin)
)

// ones counts the black cells of row i in columns lo..hi.
func ones(i, lo, hi int) int { return black[i][hi+1] - black[i][lo] }

func abs(v int) int {
	if v < 0 {
		return -v
	}
	return v
}

func fits(ci, cj, r int) bool {
	// row ci + d: |d| black cells, a white run of 2(r - |d|) + 1, |d| black
	for d := -r; d <= r; d++ {
		i, side := ci+d, abs(d)
		inner := r - side
		if ones(i, cj-r, cj-inner-1) != side || ones(i, cj+inner+1, cj+r) != side {
			return false
		}
		if ones(i, cj-inner, cj+inner) != 0 {
			return false
		}
	}
	return true
}

func largest() int {
	// the white square needs a cell on every side of the centre, so r >= 1
	for r := (n - 1) / 2; r >= 1; r-- {
		for ci := r; ci < n-r; ci++ {
			for cj := r; cj < n-r; cj++ {
				// quick tests first: a white centre and tip, a black corner
				if grid[ci][cj] == 1 || grid[ci-r][cj] == 1 || grid[ci-r][cj-r] == 0 {
					continue
				}
				if fits(ci, cj, r) {
					return 2*r + 1
				}
			}
		}
	}
	return 0
}

// readCell returns the next 0 or 1; the cells may come with or without spaces.
func readCell() int {
	c, _ := in.ReadByte()
	for c != '0' && c != '1' {
		c, _ = in.ReadByte()
	}
	return int(c - '0')
}

func main() {
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for {
		if _, err := fmt.Fscan(in, &n); err != nil || n == 0 {
			break
		}
		grid = make([][]int, n)
		black = make([][]int, n)
		for i := 0; i < n; i++ {
			grid[i] = make([]int, n)
			black[i] = make([]int, n+1)
			for j := 0; j < n; j++ {
				grid[i][j] = readCell()
				black[i][j+1] = black[i][j] + grid[i][j]
			}
		}
		if best := largest(); best > 0 {
			fmt.Fprintln(out, best)
		} else {
			fmt.Fprintln(out, "No solution")
		}
	}
}
