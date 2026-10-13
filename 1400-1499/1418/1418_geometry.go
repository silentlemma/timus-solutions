package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

type point struct{ x, y int64 }

func cross(o, a, b point) int64 {
	return (a.x-o.x)*(b.y-o.y) - (a.y-o.y)*(b.x-o.x)
}

// chain: marks the points of one monotone chain, keeping points that lie on its edges.
func chain(p []point, order []int, border []bool) {
	var stack []int
	for _, i := range order {
		for len(stack) > 1 && cross(p[stack[len(stack)-2]], p[stack[len(stack)-1]], p[i]) < 0 {
			stack = stack[:len(stack)-1]
		}
		stack = append(stack, i)
	}
	for _, i := range stack {
		border[i] = true
	}
}

func flat(p []point) bool {
	for _, q := range p {
		if cross(p[0], p[len(p)-1], q) != 0 {
			return false
		}
	}
	return true
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	points := make([]point, n)
	for i := range points {
		fmt.Fscan(in, &points[i].x, &points[i].y)
	}
	sort.Slice(points, func(a, b int) bool {
		if points[a].x != points[b].x {
			return points[a].x < points[b].x
		}
		return points[a].y < points[b].y
	})
	layers := 0
	// peel hulls with their whole border while the rest still has area
	for len(points) > 2 && !flat(points) {
		layers++
		size := len(points)
		order := make([]int, size)
		for i := range order {
			order[i] = i
		}
		border := make([]bool, size)
		chain(points, order, border)
		for i := range order {
			order[i] = size - 1 - i
		}
		chain(points, order, border)
		var rest []point
		for i, p := range points {
			if !border[i] {
				rest = append(rest, p)
			}
		}
		points = rest
	}
	fmt.Println(layers)
}
