package main

import (
	"fmt"
	"math/big"
)

const (
	odd  = 3 // the factor of the power of two for odd n
	less = 4 // every count is that power times 1 or odd, minus less
)

func main() {
	var n int
	fmt.Scan(&n)
	if n == 1 {
		fmt.Println(1)
		return
	}
	// the counts of polygons grow by 4, 4, 8, 8, 16, 16, ... from zone 3 on:
	// 2^(n / 2 + 2) - 4 for even n and 3 * 2^(n / 2 + 1) - 4 for odd n
	count := big.NewInt(1)
	if n%2 == 1 {
		count.SetInt64(odd)
	}
	count.Lsh(count, uint(n/2+2-n%2))
	count.Sub(count, big.NewInt(less))
	fmt.Println(count.String())
}
