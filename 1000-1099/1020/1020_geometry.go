package main

import (
	"fmt"
	"math"
)

func main() {
	var n int
	var r float64
	fmt.Scan(&n, &r)
	x, y := make([]float64, n), make([]float64, n)
	for i := range x {
		fmt.Scan(&x[i], &y[i])
	}
	// the straight parts are the sides of the polygon, the arcs around the
	// nails turn by 2*pi in total: one full circle of radius r
	length := 2 * math.Pi * r
	for i := 0; n > 1 && i < n; i++ {
		length += math.Hypot(x[(i+1)%n]-x[i], y[(i+1)%n]-y[i])
	}
	fmt.Printf("%.2f\n", length)
}
