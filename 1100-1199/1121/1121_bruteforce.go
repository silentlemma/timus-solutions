package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const reach = 5

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var h, w int
	fmt.Fscan(in, &h, &w)
	grid := make([][]int, h)
	for r := range grid {
		grid[r] = make([]int, w)
		for c := range grid[r] {
			fmt.Fscan(in, &grid[r][c])
		}
	}
	// the cells at each distance 1..5, as offsets around a crossing
	rings := make([][][2]int, reach+1)
	for dr := -reach; dr <= reach; dr++ {
		for dc := -reach; dc <= reach; dc++ {
			if d := abs(dr) + abs(dc); d >= 1 && d <= reach {
				rings[d] = append(rings[d], [2]int{dr, dc})
			}
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for r := 0; r < h; r++ {
		for c := 0; c < w; c++ {
			found := -1
			if grid[r][c] == 0 {
				found = 0
				for d := 1; d <= reach && found == 0; d++ {
					for _, o := range rings[d] {
						rr, cc := r+o[0], c+o[1]
						// each type counts once however many branches share it
						if rr >= 0 && rr < h && cc >= 0 && cc < w {
							found |= grid[rr][cc]
						}
					}
				}
			}
			out.WriteString(strconv.Itoa(found))
			if c+1 < w {
				out.WriteByte(' ')
			} else {
				out.WriteByte('\n')
			}
		}
	}
}
