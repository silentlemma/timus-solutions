package main

import (
	"fmt"
	"math/big"
)

const (
	three = 3
	four  = 4
)

func main() {
	var n int64
	fmt.Scan(&n)
	// threes are best: a 4 or more splits into parts with a larger product, and
	// three 2s lose to two 3s; a leftover 1 joins a 3 to make 2 + 2
	if n < four {
		fmt.Println(n)
		return
	}
	threes, rest := n/three, n%three
	if rest == 1 {
		threes, rest = threes-1, four
	}
	if rest == 0 {
		rest = 1
	}
	product := new(big.Int).Exp(big.NewInt(three), big.NewInt(threes), nil)
	fmt.Println(product.Mul(product, big.NewInt(rest)))
}
