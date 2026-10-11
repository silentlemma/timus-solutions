package main

import (
	"fmt"
	"math/big"
)

const percent = 100

func main() {
	var gold, limit, fee int64
	fmt.Scan(&gold, &limit, &fee)
	// after k years the gold is gold * ((100 - fee) / 100)^k exactly, so
	// compare gold * (100 - fee)^k with limit * 100^k in whole numbers
	left, right := big.NewInt(gold), big.NewInt(limit)
	keep, all := big.NewInt(percent-fee), big.NewInt(percent)
	years := 0
	for left.Cmp(right) > 0 {
		left.Mul(left, keep)
		right.Mul(right, all)
		years++
	}
	fmt.Println(years)
}
