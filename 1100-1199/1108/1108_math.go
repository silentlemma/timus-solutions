package main

import (
	"bufio"
	"fmt"
	"math/big"
	"os"
)

func main() {
	var n int
	fmt.Scan(&n)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	one := big.NewInt(1)
	a := big.NewInt(2)
	for i := 0; i < n; i++ {
		out.WriteString(a.String() + "\n")
		// after the shares 1/a(1) .. 1/a(k) the remainder is 1/(a(k+1) - 1), and the
		// largest share that still leaves something is 1/a(k+1)
		less := new(big.Int).Sub(a, one)
		a.Mul(a, less).Add(a, one)
	}
}
