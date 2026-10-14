package main

import (
	"fmt"
	"math/big"
)

func main() {
	var n, k int
	fmt.Scan(&n, &k)
	// count[i + 1]: lines of i words with no more than k lemons in a row,
	// with count[0] = 1 standing for length -1
	count := []*big.Int{big.NewInt(1), big.NewInt(1)}
	for i := 1; i <= n; i++ {
		// a valid line of i words is a valid line of i - 1 words plus a word,
		// except those ending in exactly k + 1 lemons after a banana
		next := new(big.Int).Lsh(count[i], 1)
		if i > k {
			next.Sub(next, count[i-k-1])
		}
		count = append(count, next)
	}
	fmt.Println(count[n+1].String())
}
