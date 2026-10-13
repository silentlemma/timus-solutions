package main

import (
	"fmt"
	"math/big"
)

func main() {
	var n int
	fmt.Scan(&n)
	// a[k]: rooted trees with k vertices; s[k]: the sum of d a[d] over divisors d of k
	a := make([]*big.Int, n+1)
	s := make([]*big.Int, n+1)
	a[1], s[1] = big.NewInt(1), big.NewInt(1)
	for m := 1; m < n; m++ {
		// a(m + 1) = (s(1) a(m) + s(2) a(m - 1) + ... + s(m) a(1)) / m
		total := new(big.Int)
		for k := 1; k <= m; k++ {
			total.Add(total, new(big.Int).Mul(s[k], a[m-k+1]))
		}
		a[m+1] = total.Div(total, big.NewInt(int64(m)))
		s[m+1] = new(big.Int)
		for d := 1; d <= m+1; d++ {
			if (m+1)%d == 0 {
				s[m+1].Add(s[m+1], new(big.Int).Mul(big.NewInt(int64(d)), a[d]))
			}
		}
	}
	fmt.Println(a[n])
}
