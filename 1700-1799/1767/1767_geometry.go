package main

import "fmt"

func sign(v int64) int64 {
	switch {
	case v > 0:
		return 1
	case v < 0:
		return -1
	}
	return 0
}

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
	var ax, ay, bx, by, cx, cy, dx, dy int64
	if _, err := fmt.Scan(&ax, &ay, &bx, &by, &cx, &cy, &dx, &dy); err != nil {
		return
	}
	// both walks stay in the boxes of their ends, so the shared part lies in
	// the overlap of the two boxes
	width := min(max(ax, bx), max(cx, dx)) - max(min(ax, bx), min(cx, dx))
	height := min(max(ay, by), max(cy, dy)) - max(min(ay, by), min(cy, dy))
	if width < 0 || height < 0 {
		fmt.Println(0)
		return
	}
	// walks rising the same way can share a staircase across the overlap, while
	// one rising and one falling share only one straight piece
	first, second := sign(bx-ax)*sign(by-ay), sign(dx-cx)*sign(dy-cy)
	if first*second < 0 {
		fmt.Println(max(width, height))
	} else {
		fmt.Println(width + height)
	}
}
