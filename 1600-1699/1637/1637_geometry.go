package main

import "fmt"

const (
	corners = 3
	glide   = 3 // a glide reflection takes three reflections
	none    = -1
)

type point [2]int64

type line struct{ a, b, c int64 } // a x + b y = c

func cross(o, a, b point) int64 {
	return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])
}

func dist2(p, q point) int64 {
	dx, dy := p[0]-q[0], p[1]-q[1]
	return dx*dx + dy*dy
}

// bisector is the line of points as far from p as from q
func bisector(p, q point) line {
	return line{2 * (q[0] - p[0]), 2 * (q[1] - p[1]), dist2(q, point{}) - dist2(p, point{})}
}

func sameLine(u, v line) bool {
	return u.a*v.b == u.b*v.a && u.a*v.c == u.c*v.a && u.b*v.c == u.c*v.b
}

// moves counts reflections taking cur[i] to to[i], or none when no isometry does
func moves(cur, to [corners]point) int {
	for i := 0; i < corners; i++ {
		for j := i + 1; j < corners; j++ {
			if dist2(cur[i], cur[j]) != dist2(to[i], to[j]) {
				return none
			}
		}
	}
	if cur == to {
		return 0
	}
	if (cross(cur[0], cur[1], cur[2]) > 0) == (cross(to[0], to[1], to[2]) > 0) {
		return 2 // a rotation or a translation: two reflections
	}
	// orientation reversed: one reflection if a single mirror fits all three
	var lines []line
	var fixed []point
	for i := 0; i < corners; i++ {
		if cur[i] == to[i] {
			fixed = append(fixed, cur[i])
		} else {
			lines = append(lines, bisector(cur[i], to[i]))
		}
	}
	mirror := lines[0]
	for _, l := range lines {
		if !sameLine(mirror, l) {
			return glide
		}
	}
	for _, p := range fixed {
		if mirror.a*p[0]+mirror.b*p[1] != mirror.c {
			return glide
		}
	}
	return 1
}

func main() {
	var target, cur [corners]point
	for i := range target {
		if _, err := fmt.Scan(&target[i][0], &target[i][1]); err != nil {
			return
		}
	}
	for i := range cur {
		fmt.Scan(&cur[i][0], &cur[i][1])
	}
	orders := [][corners]int{{0, 1, 2}, {0, 2, 1}, {1, 0, 2}, {1, 2, 0}, {2, 0, 1}, {2, 1, 0}}
	best := none
	for _, order := range orders {
		var to [corners]point
		for i, k := range order {
			to[i] = target[k]
		}
		if m := moves(cur, to); m != none && (best == none || m < best) {
			best = m
		}
	}
	if best == none {
		fmt.Println("IMPOSSIBLE")
	} else {
		fmt.Println(best)
	}
}
