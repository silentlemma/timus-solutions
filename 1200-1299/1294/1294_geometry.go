package main

import (
	"fmt"
	"math"
)

const km = 1000 // input distances are in thousands of kilometres

func abs(x int64) int64 {
	if x < 0 {
		return -x
	}
	return x
}

func main() {
	// a = AD, b = AC, c = BD, d = BC; A and B see the chord CD at the same
	// inscribed angle t, so CD^2 = a^2 + b^2 - 2ab cos t = c^2 + d^2 - 2cd cos t
	var a, b, c, d int64
	fmt.Scan(&a, &b, &c, &d)
	den := a*b - c*d
	diff := a*a + b*b - c*c - d*d
	if den == 0 || abs(diff) >= 2*abs(den) || b*c <= a*d {
		fmt.Println("Impossible.")
		return
	}
	num := a*b*(c*c+d*d) - c*d*(a*a+b*b)
	if den < 0 {
		num = -num
		den = -den
	}
	distance := int64(km * math.Sqrt(float64(num)/float64(den)))
	// Compare the half-kilometre boundary exactly, dividing before scaling.
	scale := int64(4 * km * km)
	bound := scale*(num/den) + scale*(num%den)/den
	if (2*distance+1)*(2*distance+1) <= bound {
		distance++
	}
	fmt.Printf("Distance is %d km.\n", distance)
}
