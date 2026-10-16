package main

import (
	"fmt"
	"math"
)

func main() {
	var rim, book, shelf float64
	if _, err := fmt.Scan(&rim, &book, &shelf); err != nil {
		return
	}
	// with the foot at distance x from the rim and r = hypot(x, rim), the book
	// leans on the rim top and its middle lies x * (book / 2r - 1) to the left,
	// which is largest where r cubed is book * rim * rim / 2
	r := math.Cbrt(book * rim * rim / 2)
	shift := 0.0
	if r > rim {
		x := math.Sqrt(r*r - rim*rim)
		shift = x * (book/(2*r) - 1)
	}
	fmt.Printf("%.6f\n", shift)
}
