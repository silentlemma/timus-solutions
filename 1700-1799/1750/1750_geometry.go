package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
)

type point struct{ x, y int64 }

func cross(o, a, b point) int64 { return (a.x-o.x)*(b.y-o.y) - (a.y-o.y)*(b.x-o.x) }
func vec(a, b point) point      { return point{b.x - a.x, b.y - a.y} }
func turn(u, w point) int64     { return u.x*w.y - u.y*w.x }
func dot(u, w point) int64      { return u.x*w.x + u.y*w.y }

// whether the ray w lies in the closed sector turning left from u to v
func within(u, v, w point) bool {
	c := turn(u, v)
	if c > 0 {
		return turn(u, w) >= 0 && turn(w, v) >= 0
	}
	if c < 0 {
		return !(turn(v, w) > 0 && turn(w, u) > 0)
	}
	return turn(u, w) >= 0
}

// rays from the bend b towards x and y stay on one side of the ravine
func sameSideAtBend(a, b, c, x, y point) bool {
	u, v, p, q := vec(b, a), vec(b, c), vec(b, x), vec(b, y)
	if turn(u, v) == 0 && dot(u, v) > 0 {
		return true // b is a free tip
	}
	return (within(u, v, p) && within(u, v, q)) || (within(v, u, p) && within(v, u, q))
}

func strictlyInside(p, a, b point) bool {
	return cross(a, b, p) == 0 && dot(vec(p, a), vec(p, b)) < 0
}

func crosses(p, q, a, b point) bool {
	return cross(p, q, a)*cross(p, q, b) < 0 && cross(a, b, p)*cross(a, b, q) < 0
}

func allowed(path []point, a, b, c point) bool {
	for i := 0; i+1 < len(path); i++ {
		p, q := path[i], path[i+1]
		if crosses(p, q, a, b) || crosses(p, q, b, c) {
			return false
		}
		// going straight through the bend must not change sides there
		if strictlyInside(b, p, q) && !sameSideAtBend(a, b, c, p, q) {
			return false
		}
	}
	for i := 1; i+1 < len(path); i++ {
		x, v, y := path[i-1], path[i], path[i+1]
		if v == b && !sameSideAtBend(a, b, c, x, y) {
			return false
		}
		// an end of the ravine lying inside the other piece is no corner
		if v == a && strictlyInside(a, b, c) && cross(b, c, x)*cross(b, c, y) < 0 {
			return false
		}
		if v == c && strictlyInside(c, a, b) && cross(a, b, x)*cross(a, b, y) < 0 {
			return false
		}
	}
	return true
}

type candidate struct {
	size float64
	path []point
}

// every order of every subset of the corners
func orders(left []int, chosen []int, out *[][]int) {
	*out = append(*out, append([]int{}, chosen...))
	for i, k := range left {
		rest := append(append([]int{}, left[:i]...), left[i+1:]...)
		orders(rest, append(chosen, k), out)
	}
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var routes [][]int
	orders([]int{0, 1, 2}, nil, &routes)
	var tests int
	fmt.Fscan(in, &tests)
	for ; tests > 0; tests-- {
		var s, e, a, b, c point
		fmt.Fscan(in, &s.x, &s.y, &e.x, &e.y, &a.x, &a.y, &b.x, &b.y, &c.x, &c.y)
		corner := []point{a, b, c}
		// a shortest way bends only at points of the ravine, at most once at
		// each of A, B and C; the shortest allowed candidate is the answer
		var candidates []candidate
		for _, route := range routes {
			path := []point{s}
			for _, k := range route {
				path = append(path, corner[k])
			}
			path = append(path, e)
			size := 0.0
			for i := 0; i+1 < len(path); i++ {
				size += math.Hypot(float64(path[i+1].x-path[i].x), float64(path[i+1].y-path[i].y))
			}
			candidates = append(candidates, candidate{size, path})
		}
		sort.Slice(candidates, func(i, j int) bool { return candidates[i].size < candidates[j].size })
		for _, cand := range candidates {
			if allowed(cand.path, a, b, c) {
				fmt.Fprintf(out, "%.6f\n", cand.size)
				break
			}
		}
	}
}
