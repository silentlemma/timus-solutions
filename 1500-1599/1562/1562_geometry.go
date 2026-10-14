package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

const (
	quarter = 0.25
	third   = 1.0 / 3
)

func main() {
	var a, b float64
	var n int
	fmt.Scan(&a, &b, &n)
	half := b / 2
	// below is the volume of the pineapple between its middle and height z:
	// the cross-section at z is a disc of area pi (a / 2)^2 (1 - (z / half)^2)
	below := func(z float64) float64 {
		return math.Pi * a * a * quarter * (z - z*z*z*third/(half*half))
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for i := 0; i < n; i++ {
		lo := -half + b*float64(i)/float64(n)
		hi := -half + b*float64(i+1)/float64(n)
		fmt.Fprintf(out, "%.6f\n", below(hi)-below(lo))
	}
}
