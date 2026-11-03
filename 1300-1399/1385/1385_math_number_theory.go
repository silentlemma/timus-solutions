package main

import (
	"bufio"
	"fmt"
	"math/big"
	"os"
)

const decimalBase = 10

func main() {
	var n int
	fmt.Fscan(bufio.NewReader(os.Stdin), &n)
	unit := new(big.Int).Exp(big.NewInt(decimalBase), big.NewInt(int64(n)), nil)
	first := new(big.Int).Quo(unit, big.NewInt(decimalBase))
	answer, remainder, term := new(big.Int), new(big.Int), new(big.Int)
	// Keep unit/first immutable; only scratch values and the answer mutate.
	for k := int64(1); k < decimalBase; k++ {
		divisor := big.NewInt(k)
		if remainder.Mod(unit, divisor).Sign() == 0 {
			term.Quo(unit, divisor).Sub(term, first)
			answer.Add(answer, term)
		}
	}
	fmt.Println(answer)
}
