package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var n int
	if _, err := fmt.Fscan(in, &n); err != nil {
		return
	}
	heights := make([]int, n*n)
	for i := range heights {
		fmt.Fscan(in, &heights[i])
	}
	sort.Sort(sort.Reverse(sort.IntSlice(heights)))
	mid := n / 2
	// cells by (nearer, farther) distance from the centre row and column:
	// along any row or column this grows outwards on each side
	type cell struct{ near, far, r, c int }
	var cells []cell
	for r := 0; r < n; r++ {
		for c := 0; c < n; c++ {
			a, b := abs(r-mid), abs(c-mid)
			if a > b {
				a, b = b, a
			}
			cells = append(cells, cell{a, b, r, c})
		}
	}
	sort.SliceStable(cells, func(x, y int) bool {
		if cells[x].near != cells[y].near {
			return cells[x].near < cells[y].near
		}
		return cells[x].far < cells[y].far
	})
	grid := make([][]int, n)
	for r := range grid {
		grid[r] = make([]int, n)
	}
	for k, p := range cells {
		grid[p.r][p.c] = heights[k]
	}
	for _, row := range grid {
		for c, h := range row {
			if c > 0 {
				fmt.Fprint(out, " ")
			}
			fmt.Fprint(out, h)
		}
		fmt.Fprintln(out)
	}
}
