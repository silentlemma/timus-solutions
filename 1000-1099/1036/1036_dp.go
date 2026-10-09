package main

import (
	"fmt"
	"math/big"
)

const digits = 10

func main() {
	var n, s int
	fmt.Scan(&n, &s)
	half := s / 2
	if s%2 != 0 || half > (digits-1)*n {
		fmt.Println(0)
		return
	}
	// ways[t]: the number of strings of the digits seen so far with digit sum t
	ways := make([]*big.Int, half+1)
	for t := range ways {
		ways[t] = new(big.Int)
	}
	ways[0].SetInt64(1)
	for k := 0; k < n; k++ {
		next := make([]*big.Int, half+1)
		for t := 0; t <= half; t++ {
			next[t] = new(big.Int)
			for d := 0; d < digits && d <= t; d++ {
				next[t].Add(next[t], ways[t-d])
			}
		}
		ways = next
	}
	// the two halves are chosen independently
	fmt.Println(new(big.Int).Mul(ways[half], ways[half]))
}
