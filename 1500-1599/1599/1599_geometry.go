package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func min(a, b int64) int64 {
	if a < b {
		return a
	}
	return b
}

func max(a, b int64) int64 {
	if a > b {
		return a
	}
	return b
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var n int
	if _, err := fmt.Fscan(in, &n); err != nil {
		return
	}
	xs := make([]int64, n)
	ys := make([]int64, n)
	for i := range xs {
		fmt.Fscan(in, &xs[i], &ys[i])
	}
	var m int
	fmt.Fscan(in, &m)
	for j := 0; j < m; j++ {
		var px, py int64
		fmt.Fscan(in, &px, &py)
		turns := 0
		onEdge := false
		for i := 0; i < n && !onEdge; i++ {
			ax, ay := xs[i], ys[i]
			bx, by := xs[(i+1)%n], ys[(i+1)%n]
			// each product is below 4 10^18, so the difference fits in 64 bits
			cross := (bx-ax)*(py-ay) - (by-ay)*(px-ax)
			switch {
			case cross == 0 && min(ax, bx) <= px && px <= max(ax, bx) &&
				min(ay, by) <= py && py <= max(ay, by):
				onEdge = true
			case ay <= py && py < by:
				// upwards past the point on its left: one more turn
				if cross > 0 {
					turns++
				}
			case by <= py && py < ay:
				// downwards past the point on its right: one turn less
				if cross < 0 {
					turns--
				}
			}
		}
		if onEdge {
			out.WriteString("EDGE\n")
		} else {
			out.WriteString(strconv.Itoa(turns) + "\n")
		}
	}
}
