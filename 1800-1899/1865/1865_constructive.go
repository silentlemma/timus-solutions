package main

import (
	"bufio"
	"fmt"
	"os"
)

type point struct{ x, y int64 }

type cut struct{ rows, column int64 }

func min64(a, b int64) int64 {
	if a < b {
		return a
	}
	return b
}

// straighten drops repeated points and points in the middle of a straight run
func straighten(points []point) []point {
	out := []point{}
	for _, p := range points {
		if len(out) > 0 && out[len(out)-1] == p {
			continue
		}
		for len(out) >= 2 {
			a, b := out[len(out)-2], out[len(out)-1]
			if !(a.x == b.x && b.x == p.x) && !(a.y == b.y && b.y == p.y) {
				break
			}
			out = out[:len(out)-1]
		}
		out = append(out, p)
	}
	return out
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var w, h, x, y, d int64
	fmt.Fscan(reader, &w, &h, &x, &y, &d)
	half := w * h / 2
	// Finland always holds the column of cells along its coast, the
	// lighthouse, and a corridor of cells from the lighthouse to that column
	right := w - 1 - x - d
	if h+d*d+right > half {
		fmt.Println("Impossible")
		return
	}
	var points []point
	if h+d*(w-1-x) <= half {
		// every row of Finland runs from some column to the coast; the area
		// still missing pushes rows west from the top down
		extra := half - (h + d*(w-1-x))
		cuts := []cut{}
		bands := [][]int64{{h, y + d, w - 1}, {y + d, y, x}, {y, 0, w - 1}}
		for _, band := range bands {
			rows, column := band[0]-band[1], band[2]
			if rows == 0 {
				continue
			}
			full := int64(0)
			if column > 1 {
				full = min64(rows, extra/(column-1))
			}
			extra -= full * (column - 1)
			if full > 0 {
				cuts = append(cuts, cut{full, 1})
			}
			if full < rows {
				part := min64(extra, column-1)
				extra -= part
				cuts = append(cuts, cut{1, column - part})
				if full+1 < rows {
					cuts = append(cuts, cut{rows - full - 1, column})
				}
			}
		}
		level := h
		points = append(points, point{cuts[0].column, h})
		for _, c := range cuts {
			points = append(points, point{c.column, level}, point{c.column, level - c.rows})
			level -= c.rows
		}
	} else {
		// the border goes round the lighthouse: Finland takes full corridor
		// rows at the top of the lighthouse rows and part of one more row
		rest := half - (h + d*d + right)
		more, part := rest/right, rest%right
		level := y + d - 1 - more
		points = []point{{w - 1, h}, {w - 1, y + d}, {x, y + d}, {x, y}, {x + d, y}, {x + d, level},
			{w - 1 - part, level}, {w - 1 - part, level - 1}, {w - 1, level - 1}, {w - 1, 0}}
	}
	points = straighten(points)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	fmt.Fprintln(writer, len(points))
	for _, p := range points {
		fmt.Fprintln(writer, p.x, p.y)
	}
}
