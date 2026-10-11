package main

import (
	"fmt"
	"math"
)

const (
	steps   = 70 // golden-section steps: the bracket shrinks by 0.618 each
	samples = 24 // first look along circle B, before refining
)

var gold = (math.Sqrt(5) - 1) / 2

// golden is the least value of a function with one minimum on [lo, hi]
func golden(f func(float64) float64, lo, hi float64) float64 {
	a, b := hi-gold*(hi-lo), lo+gold*(hi-lo)
	fa, fb := f(a), f(b)
	for i := 0; i < steps; i++ {
		if fa < fb {
			hi, b, fb = b, a, fa
			a = hi - gold*(hi-lo)
			fa = f(a)
		} else {
			lo, a, fa = a, b, fb
			b = lo + gold*(hi-lo)
			fb = f(b)
		}
	}
	return math.Min(fa, fb)
}

func main() {
	var r1, r2, r3, r float64
	fmt.Scan(&r1, &r2, &r3, &r)
	// a dog is fed from the house itself: then the tour goes to the other
	// dog's circle and back, and nothing shorter exists
	if math.Min(r1, r2) <= r {
		fmt.Printf("%.3f\n", 2*math.Max(math.Max(r1, r2)-r, 0))
		return
	}
	// posts at (0, 0) and (r3, 0), the house above them
	hx := r1
	if r3 > 0 {
		hx = (r1*r1 - r2*r2 + r3*r3) / (2 * r3)
	}
	hy := math.Sqrt(math.Max(r1*r1-hx*hx, 0))
	bx := r3
	// toB is the shortest way from P to the circle of dog B and on home
	toB := func(px, py float64) float64 {
		dx, dy := hx-px, hy-py
		length := math.Hypot(dx, dy)
		t := 0.0
		if length > 0 {
			t = math.Min(math.Max(((bx-px)*dx-py*dy)/(length*length), 0), 1)
		}
		if math.Hypot(px+t*dx-bx, py+t*dy) <= r {
			return length
		}
		via := func(phi float64) float64 {
			qx, qy := bx+r*math.Cos(phi), r*math.Sin(phi)
			return math.Hypot(qx-px, qy-py) + math.Hypot(hx-qx, hy-qy)
		}
		step := 2 * math.Pi / samples
		best := 0
		for k := 1; k < samples; k++ {
			if via(float64(k)*step) < via(float64(best)*step) {
				best = k
			}
		}
		return golden(via, float64(best-1)*step, float64(best+1)*step)
	}
	// the tour length is convex in P inside dog A's circle, so a golden
	// search over x of golden searches over y finds its least value
	column := func(px float64) float64 {
		half := math.Sqrt(math.Max(r*r-px*px, 0))
		return golden(func(py float64) float64 {
			return math.Hypot(hx-px, hy-py) + toB(px, py)
		}, -half, half)
	}
	fmt.Printf("%.3f\n", golden(column, -r, r))
}
