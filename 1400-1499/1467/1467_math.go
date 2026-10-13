package main

import (
	"fmt"
	"math/big"
	"strings"
)

func main() {
	var k int
	fmt.Scan(&k)
	comb := func(m, j int) *big.Rat {
		return new(big.Rat).SetInt(new(big.Int).Binomial(int64(m), int64(j)))
	}
	// Bernoulli numbers with B1 = +1/2: the sum of C(m + 1, j) B_j over
	// j <= m equals m + 1, which gives B_m from the earlier ones
	var bern []*big.Rat
	for m := 0; m <= k; m++ {
		rest := new(big.Rat)
		for j := 0; j < m; j++ {
			rest.Add(rest, new(big.Rat).Mul(comb(m+1, j), bern[j]))
		}
		b := new(big.Rat).Sub(big.NewRat(int64(m+1), 1), rest)
		bern = append(bern, b.Quo(b, big.NewRat(int64(m+1), 1)))
	}
	// Faulhaber: the coefficient of N^(k + 1 - j) is C(k + 1, j) B_j / (k + 1)
	parts := make([]string, 0, k+2)
	for j := 0; j <= k; j++ {
		c := new(big.Rat).Mul(comb(k+1, j), bern[j])
		c.Quo(c, big.NewRat(int64(k+1), 1))
		parts = append(parts, c.Num().String()+"/"+c.Denom().String())
	}
	parts = append(parts, "0/1")
	fmt.Println(strings.Join(parts, " "))
}
