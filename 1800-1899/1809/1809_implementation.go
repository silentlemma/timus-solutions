package main

import "fmt"

const (
	side  = 20
	count = 4
)

type cell struct{ x, y int }

var steps = []cell{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}

func lo(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func hi(a, b int) int {
	if a > b {
		return a
	}
	return b
}

// sees tells whether potatoes a and b share a line with nobody between
func sees(p []cell, a, b int) bool {
	if p[a].x != p[b].x && p[a].y != p[b].y {
		return false
	}
	for k := range p {
		if k == a || k == b {
			continue
		}
		x, y := p[k].x, p[k].y
		if lo(p[a].x, p[b].x) <= x && x <= hi(p[a].x, p[b].x) &&
			lo(p[a].y, p[b].y) <= y && y <= hi(p[a].y, p[b].y) {
			return false
		}
	}
	return true
}

func good(p []cell) bool {
	for a := range p {
		if p[a].x < 1 || p[a].x > side || p[a].y < 1 || p[a].y > side {
			return false
		}
		for b := 0; b < a; b++ {
			if p[a] == p[b] {
				return false
			}
		}
	}
	for a := range p {
		seen := 0
		for b := range p {
			if b != a && sees(p, a, b) {
				seen++
			}
		}
		if seen != 1 {
			return false
		}
	}
	return true
}

func solve(start []cell) []cell {
	if good(start) {
		return start
	}
	p := make([]cell, count)
	for k := 0; k < count; k++ {
		for x := 1; x <= side; x++ {
			for y := 1; y <= side; y++ {
				copy(p, start)
				p[k] = cell{x, y}
				if good(p) {
					return p
				}
			}
		}
	}
	// two moves always do: next to the two kept potatoes, or as a pair of
	// their own in rows and columns nobody else uses
	for k := 0; k < count; k++ {
		for l := k + 1; l < count; l++ {
			var kept, near []cell
			for i := 0; i < count; i++ {
				if i != k && i != l {
					kept = append(kept, start[i])
				}
			}
			for _, c := range kept {
				for _, d := range steps {
					near = append(near, cell{c.x + d.x, c.y + d.y})
				}
			}
			var options [][2]cell
			for _, a := range near {
				for _, b := range near {
					options = append(options, [2]cell{a, b})
				}
			}
			usedX := func(x int) bool { return x == kept[0].x || x == kept[1].x }
			usedY := func(y int) bool { return y == kept[0].y || y == kept[1].y }
			fx, fy := 1, 1
			for usedX(fx) {
				fx++
			}
			for usedY(fy) || usedY(fy+1) {
				fy++
			}
			options = append(options, [2]cell{{fx, fy}, {fx, fy + 1}})
			for _, o := range options {
				copy(p, start)
				p[k], p[l] = o[0], o[1]
				if good(p) {
					return p
				}
			}
		}
	}
	return start
}

func main() {
	start := make([]cell, count)
	for i := range start {
		if _, err := fmt.Scan(&start[i].x, &start[i].y); err != nil {
			return
		}
	}
	for _, c := range solve(start) {
		fmt.Println(c.x, c.y)
	}
}
