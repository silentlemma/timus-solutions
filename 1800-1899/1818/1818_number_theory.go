package main

import (
	"bufio"
	"fmt"
	"math/big"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	if _, err := fmt.Fscan(in, &n); err != nil {
		return
	}
	thrown := make([]int64, n)
	for i := range thrown {
		fmt.Fscan(in, &thrown[i])
	}
	bn := big.NewInt(int64(n))
	bm := big.NewInt(int64(n - 1))
	// build the catch X digit by digit in base n. Adding s n^j to X keeps
	// the first j fishermen happy and adds s (n - 1)^j to what fisherman
	// j + 1 finds, which is s (-1)^j modulo n: that fixes s
	caught, found := new(big.Int), new(big.Int)
	powerN, powerM := big.NewInt(1), big.NewInt(1)
	rem, term := new(big.Int), new(big.Int)
	for j, a := range thrown {
		rem.Mod(found, bn)
		s := ((a-rem.Int64())%int64(n) + int64(n)) % int64(n)
		if j%2 == 1 {
			s = (int64(n) - s) % int64(n)
		}
		bs := big.NewInt(s)
		caught.Add(caught, term.Mul(powerN, bs))
		found.Add(found, term.Mul(powerM, bs))
		// the fisherman throws a fishes away and leaves (n - 1)/n of the rest
		found.Sub(found, big.NewInt(a))
		found.Quo(found, bn)
		found.Mul(found, bm)
		powerN.Mul(powerN, bn)
		powerM.Mul(powerM, bm)
	}
	// every catch of this residue modulo n^n works; at least one fish
	if caught.Sign() == 0 {
		caught = powerN
	}
	fmt.Println(caught.String())
}
