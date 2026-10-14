package main

import (
	"fmt"
	"strings"
)

type cell struct{ x, y int }

const (
	corners       = 4  // a loop turns at least four times, by 90 degrees each
	firstStair    = 12 // all-turn loops have 4 or at least 12 turns
	notchedHeight = 3  // rows of the box when a corner is cut in
)

// letters gives F, L or R for every cell of a closed loop of cells
func letters(cells []cell) string {
	n := len(cells)
	var out strings.Builder
	for i := range cells {
		a, b, c := cells[(i+n-1)%n], cells[i], cells[(i+1)%n]
		dx1, dy1, dx2, dy2 := b.x-a.x, b.y-a.y, c.x-b.x, c.y-b.y
		switch {
		case dx1 == dx2 && dy1 == dy2:
			out.WriteByte('F')
		case dx1*dy2-dy1*dx2 > 0:
			out.WriteByte('L')
		default:
			out.WriteByte('R')
		}
	}
	return out.String()
}

// ring is the border of a width x height box, counterclockwise from the
// lower left corner, with bumps (2 cells wide, 1 high) on the top and bottom
// rows, and with the lower left corner cut in if notch is set
func ring(width, height, bumps int, notch bool) []cell {
	var freeTop, freeBottom []int // pairs (x, x - 1) on top, (x - 1, x) at the bottom
	for x := width - 2; x > 1; x -= 2 {
		freeTop = append(freeTop, x)
	}
	start := 2
	if notch {
		start++
	}
	for x := start; x < width-1; x += 2 {
		freeBottom = append(freeBottom, x)
	}
	up := bumps
	if up > len(freeTop) {
		up = len(freeTop)
	}
	upAt, downAt := map[int]bool{}, map[int]bool{}
	for _, x := range freeTop[:up] {
		upAt[x] = true
	}
	for _, x := range freeBottom[:bumps-up] {
		downAt[x] = true
	}
	cells := []cell{{0, 0}}
	if notch {
		cells = []cell{{1, 1}, {1, 0}}
	}
	for x := cells[len(cells)-1].x + 1; x < width; x++ { // the bottom row, going east
		if downAt[x] {
			cells = append(cells, cell{x - 1, -1}, cell{x, -1})
		}
		cells = append(cells, cell{x, 0})
	}
	for y := 1; y < height; y++ {
		cells = append(cells, cell{width - 1, y})
	}
	for x := width - 2; x >= 0; x-- { // the top row, going west
		cells = append(cells, cell{x, height - 1})
		if upAt[x] {
			cells = append(cells, cell{x, height}, cell{x - 1, height}, cell{x - 1, height - 1})
			x--
		}
	}
	// the left column, going south; with a notch its last cell (0, 1) leads
	// into (1, 1) instead of the corner
	for y := height - 2; y > 0; y-- {
		cells = append(cells, cell{0, y})
	}
	return cells
}

func build(straights, turns int) string {
	if straights == 0 && turns >= firstStair {
		// a staircase loop: four corners and steps LR on the sides
		steps := (turns - corners) / corners
		half := "L" + strings.Repeat("LR", steps-1) + "L" + "LR"
		return half + half
	}
	notch := turns%corners == 2
	bumps := (turns - corners) / corners // a notch takes the other 2 turns
	height := 2
	if notch {
		height = notchedHeight
	}
	return letters(ring(2+straights/2+bumps, height, bumps, notch))
}

func main() {
	var s, t int
	fmt.Scan(&s, &t)
	// both counts even, at least 4 turns, and without straights the turns
	// must be 4 or a multiple of 4 from 12
	straights, turns := s-s%2, t-t%2
	if turns < corners {
		fmt.Println("Atawazu")
		return
	}
	if straights == 0 {
		turns -= turns % corners
		if turns < firstStair {
			turns = corners
		}
	}
	path := build(straights, turns)
	fmt.Println(len(path))
	fmt.Println(path)
}
