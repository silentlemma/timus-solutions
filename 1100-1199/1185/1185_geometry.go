package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
)

type pt struct{ x, y int64 }

func cross(o, a, b pt) int64 {
	return (a.x-o.x)*(b.y-o.y) - (a.y-o.y)*(b.x-o.x)
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	var gap float64
	fmt.Fscan(in, &n, &gap)
	pts := make([]pt, n)
	for i := range pts {
		fmt.Fscan(in, &pts[i].x, &pts[i].y)
	}
	sort.Slice(pts, func(i, j int) bool {
		if pts[i].x != pts[j].x {
			return pts[i].x < pts[j].x
		}
		return pts[i].y < pts[j].y
	})
	// the shortest wall is the convex hull pushed out by L: its straight
	// parts add up to the hull perimeter, and its arcs turn once around a
	// full circle of radius L in total
	var hull []pt
	for pass := 0; pass < 2; pass++ {
		var part []pt
		for _, p := range pts {
			for len(part) >= 2 && cross(part[len(part)-2], part[len(part)-1], p) <= 0 {
				part = part[:len(part)-1]
			}
			part = append(part, p)
		}
		hull = append(hull, part[:len(part)-1]...)
		for i, j := 0, len(pts)-1; i < j; i, j = i+1, j-1 {
			pts[i], pts[j] = pts[j], pts[i]
		}
	}
	length := 2 * math.Pi * gap
	for k := range hull {
		a, b := hull[k], hull[(k+1)%len(hull)]
		length += math.Hypot(float64(a.x-b.x), float64(a.y-b.y))
	}
	fmt.Println(int64(math.Round(length)))
}
