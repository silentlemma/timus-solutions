package main

import (
	"bufio"
	"fmt"
	"math/big"
	"os"
)

const letters = 26

// word returns the k-th password from 1: by length, then alphabetically,
// which is k written in bijective base 26 with digits a to z
func word(k *big.Int) string {
	x := new(big.Int).Set(k)
	one, base := big.NewInt(1), big.NewInt(letters)
	d := new(big.Int)
	var out []byte
	for x.Sign() > 0 {
		x.Sub(x, one)
		x.QuoRem(x, base, d)
		out = append([]byte{byte('a' + d.Int64())}, out...)
	}
	return string(out)
}

func main() {
	var n, m int64
	fmt.Scan(&n, &m)
	total, power := new(big.Int), big.NewInt(1)
	for i := int64(0); i < n; i++ {
		power.Mul(power, big.NewInt(letters))
		total.Add(total, power)
	}
	share, rest := new(big.Int).QuoRem(total, big.NewInt(m), new(big.Int))
	extra := rest.Int64()
	min := func(a, b int64) int64 {
		if a < b {
			return a
		}
		return b
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	// the first extra processors take one password more
	for i := int64(0); i < m; i++ {
		start := new(big.Int).Mul(share, big.NewInt(i))
		start.Add(start, big.NewInt(min(i, extra)+1))
		end := new(big.Int).Mul(share, big.NewInt(i+1))
		end.Add(end, big.NewInt(min(i+1, extra)))
		fmt.Fprintf(out, "%s-%s\n", word(start), word(end))
	}
}
