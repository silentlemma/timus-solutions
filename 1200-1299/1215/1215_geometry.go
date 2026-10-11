package main

import (
	"fmt"
	"math"
)

func segmentDistance(px, py, ax, ay, bx, by float64) float64 {
	dx, dy := bx-ax, by-ay
	t, length2 := (px-ax)*dx+(py-ay)*dy, dx*dx+dy*dy
	if t <= 0 {
		return math.Hypot(px-ax, py-ay)
	}
	if t >= length2 {
		return math.Hypot(px-bx, py-by)
	}
	return math.Abs((px-ax)*dy-(py-ay)*dx) / math.Sqrt(length2)
}

func main() {
	var px, py int64
	var n int
	fmt.Scan(&px, &py, &n)
	x, y := make([]int64, n), make([]int64, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&x[i], &y[i])
	}
	inside, best := true, math.Inf(1)
	for i := 0; i < n; i++ {
		j := (i + 1) % n
		// inside a counterclockwise polygon the point is left of every edge
		if (x[j]-x[i])*(py-y[i])-(y[j]-y[i])*(px-x[i]) < 0 {
			inside = false
		}
		d := segmentDistance(float64(px), float64(py), float64(x[i]), float64(y[i]),
			float64(x[j]), float64(y[j]))
		best = math.Min(best, d)
	}
	if inside {
		best = 0
	}
	fmt.Printf("%.3f\n", 2*best)
}
