package main

import (
	"fmt"
	"math/big"
)

func main() {
	var n, k int64
	fmt.Scan(&n, &k)
	// numbers of valid prefixes ending with a zero and with another digit,
	// where the first digit is not zero
	digits := big.NewInt(k - 1)
	zero, other := big.NewInt(0), big.NewInt(k-1)
	for i := int64(1); i < n; i++ {
		next := new(big.Int).Add(zero, other)
		next.Mul(next, digits)
		zero, other = other, next
	}
	fmt.Println(new(big.Int).Add(zero, other))
}
