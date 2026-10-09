package main

import (
	"fmt"
	"math"
)

const sides = 4

func main() {
	var a, r float64
	fmt.Scan(&a, &r)
	half := a / 2
	var area float64
	switch {
	case r <= half:
		area = math.Pi * r * r
	case r*r >= 2*half*half:
		area = a * a
	default:
		// the circle minus the four caps cut off by the sides
		cap := r*r*math.Acos(half/r) - half*math.Sqrt(r*r-half*half)
		area = math.Pi*r*r - sides*cap
	}
	fmt.Printf("%.3f\n", area)
}
