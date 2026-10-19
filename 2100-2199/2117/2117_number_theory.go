package main

import (
	"fmt"
	"math"
)

const bound = 1000000 // the cube root of the largest C

func isqrt(x uint64) uint64 {
	r := uint64(math.Sqrt(float64(x)))
	for r*r > x {
		r--
	}
	for (r+1)*(r+1) <= x {
		r++
	}
	return r
}

func main() {
	var c uint64
	fmt.Scan(&c)
	if c == 0 {
		fmt.Println(1) // only 0 + 0
		return
	}
	// sqrt A + sqrt B = sqrt C exactly when C = s^2 q with q square-free and
	// A = a^2 q, B = b^2 q, a + b = s; so the answer counts the pairs a <= b
	root := uint64(1)
	for d := uint64(2); d <= bound && d*d <= c; d++ {
		for c%(d*d) == 0 {
			c /= d * d
			root *= d
		}
		if c%d == 0 {
			c /= d
		}
	}
	// what is left has only prime factors above the bound, at most two of them,
	// so it holds a square factor only when it is a square itself
	if r := isqrt(c); c > 1 && r*r == c {
		root *= r
	}
	fmt.Println(root/2 + 1)
}
