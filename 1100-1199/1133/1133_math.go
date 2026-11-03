package main

import (
	"bufio"
	"fmt"
	"math/big"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var i, j, n int
	var first, later int64
	fmt.Fscan(in, &i, &first, &j, &later, &n)
	if i > j {
		i, first, j, later = j, later, i, first
	}
	previous, coefficient := big.NewInt(0), big.NewInt(1)
	for step := 0; step < j-i; step++ {
		previous, coefficient = coefficient, new(big.Int).Add(previous, coefficient)
	}
	// F(j) = F(j-i-1)*F(i) + F(j-i)*F(i+1); division is exact.
	current := big.NewInt(first)
	factor := new(big.Int).Sub(coefficient, previous)
	following := new(big.Int).Sub(big.NewInt(later), new(big.Int).Mul(factor, current))
	following.Quo(following, previous)
	for i < n {
		current, following = following, new(big.Int).Add(current, following)
		i++
	}
	for i > n {
		current, following = new(big.Int).Sub(following, current), current
		i--
	}
	fmt.Println(current.String())
}
