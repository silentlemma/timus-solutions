package main

import (
	"fmt"
	"math"
)

func main() {
	var a, b float64
	fmt.Scan(&a, &b)
	// the right triangle on the birch and the ground holds at most a quarter
	// of the squared diagonal; with the triangle of the sticks added, the
	// total is largest when the sticks meet at 135 degrees
	x, y := a/2, b/2
	fmt.Printf("%.9f\n", x*x+y*y+2*math.Sqrt(2)*x*y)
}
