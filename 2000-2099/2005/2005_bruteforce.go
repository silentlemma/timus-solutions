package main

import (
	"bufio"
	"fmt"
	"os"
)

const points = 5

// point k has index k - 1: start 0, middle points firstMiddle..lastMiddle, finish end
const (
	firstMiddle = 1
	point3      = 2
	lastMiddle  = 3
	end         = 4
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var d [points][points]int
	for i := range d {
		for j := range d[i] {
			fmt.Fscan(in, &d[i][j])
		}
	}
	// points 2, 3 and 4 (indices 1, 2, 3) come in any order, except that 3
	// may not be the last of them
	best := -1
	var route [points]int
	for a := firstMiddle; a <= lastMiddle; a++ {
		for b := firstMiddle; b <= lastMiddle; b++ {
			for c := firstMiddle; c <= lastMiddle; c++ {
				if a == b || a == c || b == c || c == point3 {
					continue
				}
				cost := d[0][a] + d[a][b] + d[b][c] + d[c][end]
				if best < 0 || cost < best {
					best = cost
					route = [points]int{0, a, b, c, end}
				}
			}
		}
	}
	fmt.Println(best)
	for i, point := range route {
		if i > 0 {
			fmt.Print(" ")
		}
		fmt.Print(point + 1)
	}
	fmt.Println()
}
