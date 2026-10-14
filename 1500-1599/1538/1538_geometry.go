package main

import (
	"bufio"
	"fmt"
	"math/bits"
	"os"
	"sort"
)

const (
	enough = 9 // any 9 points, no three on a line, hold a convex pentagon
	sides  = 5
)

type point struct {
	x, y int64
	id   int
}

func cross(o, a, b point) int64 {
	return (a.x-o.x)*(b.y-o.y) - (a.y-o.y)*(b.x-o.x)
}

// hull returns the convex hull of the points, counterclockwise
func hull(points []point) []point {
	sort.Slice(points, func(i, j int) bool {
		return points[i].x < points[j].x || points[i].x == points[j].x && points[i].y < points[j].y
	})
	var h []point
	for pass := 0; pass < 2; pass++ {
		start := len(h)
		for _, p := range points {
			for len(h) >= start+2 && cross(h[len(h)-2], h[len(h)-1], p) <= 0 {
				h = h[:len(h)-1]
			}
			h = append(h, p)
		}
		h = h[:len(h)-1]
		for i, j := 0, len(points)-1; i < j; i, j = i+1, j-1 {
			points[i], points[j] = points[j], points[i]
		}
	}
	return h
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	// by the Erdos-Szekeres theorem the first nine points are enough
	m := n
	if m > enough {
		m = enough
	}
	points := make([]point, m)
	for i := range points {
		fmt.Fscan(in, &points[i].x, &points[i].y)
		points[i].id = i + 1
	}
	for mask := 0; mask < 1<<m; mask++ {
		if bits.OnesCount(uint(mask)) != sides {
			continue
		}
		var five []point
		for i := 0; i < m; i++ {
			if mask>>i&1 == 1 {
				five = append(five, points[i])
			}
		}
		if h := hull(five); len(h) == sides {
			fmt.Println("Yes")
			for i, p := range h {
				if i > 0 {
					fmt.Print(" ")
				}
				fmt.Print(p.id)
			}
			fmt.Println()
			return
		}
	}
	fmt.Println("No")
}
