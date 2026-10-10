package main

import (
	"fmt"
	"math"
)

func main() {
	var s int64
	fmt.Scan(&s)
	// s = n*a + n(n-1)/2 with a >= 1 needs n(n+1)/2 <= s; try the longest first
	n := int64(math.Sqrt(2 * float64(s)))
	for n*(n+1)/2 > s {
		n--
	}
	for (s-n*(n-1)/2)%n != 0 {
		n--
	}
	fmt.Println((s-n*(n-1)/2)/n, n)
}
