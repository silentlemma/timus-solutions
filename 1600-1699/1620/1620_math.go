package main

import (
	"fmt"
	"math/big"
)

func main() {
	var n, m, k int64
	if _, err := fmt.Scan(&n, &m, &k); err != nil {
		return
	}
	// each flip moves the expectation to E (1 - 2/n) + 1, so after k flips
	// E = n/2 + (m - n/2) ((n - 2)/n)^k = (n^(k+1) + (2m - n)(n - 2)^k) / (2 n^k)
	bn := big.NewInt(n)
	num := new(big.Int).Exp(bn, big.NewInt(k+1), nil)
	tail := new(big.Int).Exp(big.NewInt(n-2), big.NewInt(k), nil)
	tail.Mul(tail, big.NewInt(2*m-n))
	num.Add(num, tail)
	den := new(big.Int).Exp(bn, big.NewInt(k), nil)
	den.Lsh(den, 1)
	g := new(big.Int).GCD(nil, nil, num, den)
	num.Quo(num, g)
	den.Quo(den, g)
	fmt.Printf("%s/%s\n", num.String(), den.String())
}
