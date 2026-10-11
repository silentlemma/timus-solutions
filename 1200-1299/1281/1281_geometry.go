package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
)

type point struct{ x, y float64 }

func cross(o, a, b point) float64 {
	return (a.x-o.x)*(b.y-o.y) - (a.y-o.y)*(b.x-o.x)
}

// hullArea is the area of the convex hull, by the monotone chain and the
// shoelace
func hullArea(pts []point) float64 {
	sort.Slice(pts, func(i, j int) bool {
		return pts[i].x < pts[j].x || pts[i].x == pts[j].x && pts[i].y < pts[j].y
	})
	h := make([]point, 0, 2*len(pts))
	for _, p := range pts {
		for len(h) >= 2 && cross(h[len(h)-2], h[len(h)-1], p) <= 0 {
			h = h[:len(h)-1]
		}
		h = append(h, p)
	}
	for i, t := len(pts)-2, len(h)+1; i >= 0; i-- {
		for len(h) >= t && cross(h[len(h)-2], h[len(h)-1], pts[i]) <= 0 {
			h = h[:len(h)-1]
		}
		h = append(h, pts[i])
	}
	area := 0.0
	for i := 0; i+1 < len(h); i++ {
		area += h[i].x*h[i+1].y - h[i].y*h[i+1].x
	}
	return math.Abs(area) / 2
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	rivers := make([][]point, n)
	for i := range rivers {
		var k int
		fmt.Fscan(in, &k)
		rivers[i] = make([]point, k)
		for j := range rivers[i] {
			fmt.Fscan(in, &rivers[i][j].x, &rivers[i][j].y)
		}
	}
	// a river is a tributary of the one whose inner vertex is its mouth
	owner := map[point]int{}
	for i, r := range rivers {
		for j := 1; j+1 < len(r); j++ {
			owner[r[j]] = i
		}
	}
	tributaries := make([][]int, n)
	for i, r := range rivers {
		if o, ok := owner[r[len(r)-1]]; ok && o != i {
			tributaries[o] = append(tributaries[o], i)
		}
	}
	var basin func(i int) []point
	basin = func(i int) []point {
		pts := append([]point(nil), rivers[i]...)
		for _, t := range tributaries[i] {
			pts = append(pts, basin(t)...)
		}
		return pts
	}
	best := 0.0
	for i := range rivers {
		best = math.Max(best, hullArea(basin(i)))
	}
	fmt.Printf("%.2f\n", best)
}
