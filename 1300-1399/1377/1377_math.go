package main

import "fmt"

func index(n, m, r, c int) int {
	layer := r
	for _, value := range []int{c, n - 1 - r, m - 1 - c} {
		if value < layer {
			layer = value
		}
	}
	height, width := n-2*layer, m-2*layer
	r, c = r-layer, c-layer
	// Outer layers contain the cells outside this remaining rectangle.
	before, offset := n*m-height*width, 0
	switch {
	case height == 1:
		offset = c
	case width == 1:
		offset = r
	case r == 0:
		offset = c
	case c == width-1:
		offset = width - 1 + r
	case r == height-1:
		offset = width - 1 + height - 1 + width - 1 - c
	default:
		offset = 2*(height+width-2) - r
	}
	return before + offset
}

func main() {
	var n, m, r1, c1, r2, c2 int
	fmt.Scan(&n, &m, &r1, &c1, &r2, &c2)
	difference := index(n, m, r1-1, c1-1) - index(n, m, r2-1, c2-1)
	if difference < 0 {
		difference = -difference
	}
	fmt.Println(difference)
}
