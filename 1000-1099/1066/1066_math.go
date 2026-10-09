package main

import (
	"fmt"
	"math"
)

func main() {
	var n int
	var a float64
	fmt.Scan(&n, &a)
	// with the second height x, lamp i hangs at a + (i-1)(x - a) + (i-1)(i-2)
	// and the last height grows with x, so x is the smallest value keeping every
	// lamp at height 0 or above
	x := 0.0
	for k := 1; k < n; k++ {
		x = math.Max(x, a-a/float64(k)-float64(k-1))
	}
	m := float64(n - 1)
	fmt.Printf("%.2f\n", a+m*(x-a)+m*(m-1))
}
