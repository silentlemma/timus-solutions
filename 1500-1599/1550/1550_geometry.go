package main

import (
	"fmt"
	"math"
)

const third = 1.0 / 3 // a pyramid is a third of its prism

func main() {
	var h, w, x, y, r float64
	fmt.Scan(&h, &w, &x, &y, &r)
	// the hole meets no edge, so it lies over a single face, where the height
	// is linear: the cut-out volume is the hole's area times the height at
	// its centre, and that height falls from H to 0 with max(|x|, |y|)
	centre := h * (1 - math.Max(math.Abs(x), math.Abs(y))/(w/2))
	fmt.Printf("%.5f\n", h*w*w*third-math.Pi*r*r*centre)
}
