package main

import (
	"fmt"
	"math"
)

const bosses = 4

// the three ways to split the four bosses into two shots
var splits = [3][2][2]int{{{0, 1}, {2, 3}}, {{0, 2}, {1, 3}}, {{0, 3}, {1, 2}}}

var x, y [bosses]float64

// walk goes from the origin to a point P on the line a1 b1, shoots, then
// walks straight to the line a2 b2; along the first line P = a1 + t u and
// the length is sqrt((t - t0)^2 + h^2) + |k t + m|, convex in t
func walk(a1, b1, a2, b2 int) float64 {
	length := math.Hypot(x[b1]-x[a1], y[b1]-y[a1])
	ux, uy := (x[b1]-x[a1])/length, (y[b1]-y[a1])/length
	t0 := -(x[a1]*ux + y[a1]*uy)
	h := math.Abs(x[a1]*uy - y[a1]*ux)
	norm := math.Hypot(x[b2]-x[a2], y[b2]-y[a2])
	nx, ny := -(y[b2]-y[a2])/norm, (x[b2]-x[a2])/norm
	k := nx*ux + ny*uy
	m := nx*(x[a1]-x[a2]) + ny*(y[a1]-y[a2])
	// the minimum is at the foot of the origin, where the lines cross, or
	// where the slope of the first term cancels the slope k of the second
	candidates := []float64{t0}
	if k != 0 {
		candidates = append(candidates, -m/k)
	}
	if math.Abs(k) < 1 {
		shift := k * h / math.Sqrt(1-k*k)
		candidates = append(candidates, t0+shift, t0-shift)
	}
	best := math.Inf(1)
	for _, t := range candidates {
		best = math.Min(best, math.Hypot(t-t0, h)+math.Abs(k*t+m))
	}
	return best
}

func main() {
	for i := 0; i < bosses; i++ {
		fmt.Scan(&x[i], &y[i])
	}
	best := math.Inf(1)
	for _, s := range splits {
		p, q := s[0], s[1]
		best = math.Min(best, math.Min(walk(p[0], p[1], q[0], q[1]), walk(q[0], q[1], p[0], p[1])))
	}
	fmt.Printf("%.10f\n", best)
}
