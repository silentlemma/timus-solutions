package main

import (
	"fmt"
	"math"
)

const slack = 1e-9 // lets a chain that closes exactly keep its last circle

type circle struct{ x, y, r float64 }

// invert gives the image under inversion in the unit circle around the origin.
func invert(c circle) circle {
	den := c.x*c.x + c.y*c.y - c.r*c.r
	return circle{c.x / den, c.y / den, c.r / math.Abs(den)}
}

func main() {
	var big, small, d float64
	fmt.Scan(&big, &small, &d)
	// the limit point inside the small circle (the common centre if d = 0):
	// inverting there makes both circles concentric
	b := big*big + d*d - small*small
	twice := 2 * d * big
	p := twice * big / (b + math.Sqrt(math.Max(0, b*b-twice*twice)))
	outer := invert(circle{-p, 0, big})
	inner := invert(circle{d - p, 0, small})
	centre := (outer.x + inner.x) / 2
	mid := (outer.r + inner.r) / 2
	half := math.Abs(outer.r-inner.r) / 2
	// there every chain circle has radius half and turns by step around the
	// centre; the chain stops once one more would overlap the first
	step := 2 * math.Asin(half/mid)
	count := math.Floor(2*math.Pi/step + slack)
	span := (count - 1) * step
	gap := func(theta float64) float64 {
		a := invert(circle{centre + mid*math.Cos(theta), mid * math.Sin(theta), half})
		z := invert(circle{centre + mid*math.Cos(theta+span), mid * math.Sin(theta+span), half})
		return math.Hypot(a.x-z.x, a.y-z.y) - a.r - z.r
	}
	// the best chain is symmetric about the line through the centres
	best := math.Min(gap(-span/2), gap(math.Pi-span/2))
	fmt.Printf("%.10f\n", math.Max(0, best))
}
