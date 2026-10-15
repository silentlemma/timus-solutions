package main

import (
	"fmt"
	"math"
)

func main() {
	var a1, b1, a2, b2 int64
	if _, err := fmt.Scan(&a1, &b1, &a2, &b2); err != nil {
		return
	}
	// the largest singular value of [[a1, b1], [a2, b2]] without cancellation:
	// both sums of squares are exact integers
	p := (a1+b2)*(a1+b2) + (b1-a2)*(b1-a2)
	q := (a1-b2)*(a1-b2) + (b1+a2)*(b1+a2)
	fmt.Printf("%.10f\n", (math.Sqrt(float64(p))+math.Sqrt(float64(q)))/2)
}
