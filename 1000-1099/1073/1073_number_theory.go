package main

import (
	"fmt"
	"math"
)

// Lagrange: every number is a sum of four squares, and Legendre: exactly the
// numbers 4^a (8b + 7) need all four
const (
	most    = 4
	power   = 4
	modulus = 8
	rest    = 7
)

func isSquare(v int) bool {
	r := int(math.Round(math.Sqrt(float64(v))))
	return r*r == v
}

func count(n int) int {
	if isSquare(n) {
		return 1
	}
	for a := 1; a*a < n; a++ {
		if isSquare(n - a*a) {
			return 2
		}
	}
	for n%power == 0 {
		n /= power
	}
	if n%modulus == rest {
		return most
	}
	return most - 1
}

func main() {
	var n int
	fmt.Scan(&n)
	fmt.Println(count(n))
}
