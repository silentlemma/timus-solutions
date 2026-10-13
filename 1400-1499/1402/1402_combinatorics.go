package main

import (
	"fmt"
	"math/big"
)

func main() {
	var n int64
	fmt.Scan(&n)
	// ordered choices of k different drinks: n (n - 1) ... (n - k + 1), for k from 2,
	// the sum for n = 21 needs more than 64 bits
	total, ways := new(big.Int), big.NewInt(n)
	for k := int64(2); k <= n; k++ {
		ways.Mul(ways, big.NewInt(n-k+1))
		total.Add(total, ways)
	}
	fmt.Println(total)
}
