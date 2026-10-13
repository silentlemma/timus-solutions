package main

import (
	"fmt"
	"math"
)

const quarters = 4

func isqrt(n int64) int64 {
	s := int64(math.Sqrt(float64(n)))
	for s*s > n {
		s--
	}
	for (s+1)*(s+1) <= n {
		s++
	}
	return s
}

func main() {
	var r int64
	fmt.Scan(&r)
	// a tile shares more than one point with the disc exactly when its
	// corner nearest to the centre lies strictly inside: in one quarter,
	// tiles (i, j) with i^2 + j^2 < r^2, that is j <= isqrt(r^2 - i^2 - 1)
	var total int64
	for i := int64(0); i < r; i++ {
		total += isqrt(r*r-i*i-1) + 1
	}
	fmt.Println(quarters * total)
}
