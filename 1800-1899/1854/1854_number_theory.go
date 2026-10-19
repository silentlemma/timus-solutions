package main

import (
	"fmt"
	"math"
)

const firstOddPrime = 3 // n is odd

// isqrt gives the integer square root, corrected after the floating-point guess
func isqrt(n int64) int64 {
	r := int64(math.Sqrt(float64(n)))
	for r*r > n {
		r--
	}
	for (r+1)*(r+1) <= n {
		r++
	}
	return r
}

func main() {
	var n int64
	fmt.Scan(&n)
	// the gods number a square divisor of n: a number has an odd count of
	// divisors exactly when it is a square
	best := int64(1)
	for p := int64(firstOddPrime); p*p*p <= n; p += 2 {
		power := 0
		for n%p == 0 {
			n /= p
			power++
		}
		for k := 0; k < power/2; k++ {
			best *= p * p
		}
	}
	// what is left has no prime factor up to its cube root, so at most two
	// prime factors: it is a square only as the square of one prime
	if r := isqrt(n); r*r == n {
		best *= n
	}
	fmt.Println(best)
}
