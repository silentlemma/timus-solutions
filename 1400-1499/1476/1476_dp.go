package main

import (
	"fmt"
	"math/big"
)

func main() {
	var m, n, k int
	fmt.Scan(&m, &n, &k)
	binom := make([][]int64, m+1)
	for i := range binom {
		binom[i] = make([]int64, m+1)
		binom[i][0] = 1
		for j := 1; j <= i; j++ {
			binom[i][j] = binom[i-1][j-1] + binom[i-1][j]
		}
	}
	// step[c][d]: ways to follow a column with c ones by one with d ones,
	// turning at most k zeros into ones (at most 2^40 of them)
	step := make([][]int64, m+1)
	for c := range step {
		step[c] = make([]int64, m+1)
		for t := 0; t <= k && t <= m-c; t++ {
			for s := 0; s <= c; s++ {
				step[c][s+t] += binom[m-c][t] * binom[c][s]
			}
		}
	}
	// ways[c]: fillings of the columns so far whose last column has c ones
	ways := make([]*big.Int, m+1)
	for c := range ways {
		ways[c] = big.NewInt(binom[m][c])
	}
	term := new(big.Int)
	for col := 1; col < n; col++ {
		next := make([]*big.Int, m+1)
		for d := range next {
			next[d] = new(big.Int)
			for c := 0; c <= m; c++ {
				next[d].Add(next[d], term.Mul(ways[c], big.NewInt(step[c][d])))
			}
		}
		ways = next
	}
	total := new(big.Int)
	for _, w := range ways {
		total.Add(total, w)
	}
	fmt.Println(total.String())
}
