package main

import (
	"bufio"
	"fmt"
	"math/big"
	"os"
)

func main() {
	var n int
	if _, err := fmt.Scan(&n); err != nil {
		return
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	// The Catalan numbers: every leading square of their Hankel matrix has
	// determinant 1. C(k + 1) = C(k) * 2 (2k + 1) / (k + 2), always exact.
	c := big.NewInt(1)
	for k := 0; k < 2*n-1; k++ {
		fmt.Fprintln(out, c.String())
		c.Mul(c, big.NewInt(int64(2*(2*k+1))))
		c.Quo(c, big.NewInt(int64(k+2)))
	}
}
