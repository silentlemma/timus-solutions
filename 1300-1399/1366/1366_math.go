package main

import (
	"fmt"
	"math/big"
)

func main() {
	var n int64
	fmt.Scan(&n)
	// derangements: d(1) = 0 and d(k) = k d(k - 1) + (-1)^k
	count, one := big.NewInt(0), big.NewInt(1)
	for k := int64(2); k <= n; k++ {
		count.Mul(count, big.NewInt(k))
		if k%2 == 0 {
			count.Add(count, one)
		} else {
			count.Sub(count, one)
		}
	}
	fmt.Println(count.String())
}
