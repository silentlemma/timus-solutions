package main

import (
	"fmt"
	"math/big"
)

func main() {
	var n int
	fmt.Scan(&n)
	// numbers of length k without two zeros in a row: Fibonacci F(k + 2), so
	// F(2N) bars go into F(N) safes, and F(2N) = F(N) L(N) with Lucas L(N)
	a, b := big.NewInt(2), big.NewInt(1) // L(0), L(1)
	for i := 0; i < n; i++ {
		a.Add(a, b)
		a, b = b, a
	}
	fmt.Println(a.String())
}
