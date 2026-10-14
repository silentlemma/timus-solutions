package main

import (
	"fmt"
	"math"
)

const (
	four  = 4
	seven = 7
	eight = 8

	residue  = 3 // the primes 4k + 3
	firstOdd = 3 // the first odd divisor to try

	threeSquares = 3
	fourSquares  = 4
)

func isSquare(n int64) bool {
	r := int64(math.Sqrt(float64(n)))
	for r*r > n {
		r--
	}
	for (r+1)*(r+1) <= n {
		r++
	}
	return r*r == n
}

// twoSquares: by Fermat, every prime 4k + 3 must appear an even number of times.
func twoSquares(n int64) bool {
	for n%2 == 0 {
		n /= 2
	}
	for d := int64(firstOdd); d*d <= n; d += 2 {
		count := 0
		for n%d == 0 {
			n /= d
			count++
		}
		if d%four == residue && count%2 == 1 {
			return false
		}
	}
	// what is left is 1 or a prime
	return n%four != residue
}

func main() {
	var n int64
	if _, err := fmt.Scan(&n); err != nil {
		return
	}
	m := n
	for m%four == 0 {
		m /= four
	}
	switch {
	case isSquare(n):
		fmt.Println(1)
	case twoSquares(n):
		fmt.Println(2)
	case m%eight == seven:
		fmt.Println(fourSquares) // Legendre: exactly the numbers 4^a (8b + 7) need four
	default:
		fmt.Println(threeSquares)
	}
}
