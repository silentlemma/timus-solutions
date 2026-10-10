package main

import (
	"fmt"
	"math/big"
)

const (
	first = 36
	other = 55
)

func main() {
	var k int64
	fmt.Scan(&k)
	// no position may carry: 36 pairs of leading digits with a sum of at
	// most 9, and 55 pairs of digits from 0 in every other position
	count := new(big.Int).Exp(big.NewInt(other), big.NewInt(k-1), nil)
	fmt.Println(count.Mul(count, big.NewInt(first)))
}
