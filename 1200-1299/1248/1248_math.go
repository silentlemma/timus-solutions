package main

import (
	"bufio"
	"fmt"
	"math/big"
	"os"
	"strconv"
	"strings"
)

const (
	digits = 19
	half   = 5
)

// every input number is a whole multiple of 10^-shift, and every sum has
// more than 19 digits once scaled
const shift = 300

func pow10(k int) *big.Int {
	return new(big.Int).Exp(big.NewInt(10), big.NewInt(int64(k)), nil)
}

// scaled is the number times 10^shift, as an exact integer
func scaled(text string) *big.Int {
	mantissa, exp := text, 0
	if e := strings.IndexAny(text, "eE"); e >= 0 {
		mantissa = text[:e]
		exp, _ = strconv.Atoi(text[e+1:])
	}
	frac := 0
	if dot := strings.IndexByte(mantissa, '.'); dot >= 0 {
		frac = len(mantissa) - dot - 1
		mantissa = mantissa[:dot] + mantissa[dot+1:]
	}
	v, _ := new(big.Int).SetString(mantissa, 10)
	return v.Mul(v, pow10(shift+exp-frac))
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	total := new(big.Int)
	for i := 0; i < n; i++ {
		var word string
		fmt.Fscan(in, &word)
		total.Add(total, scaled(word))
	}
	if total.Sign() == 0 {
		fmt.Printf("0.%se0\n", strings.Repeat("0", digits-1))
		return
	}
	sign := ""
	if total.Sign() < 0 {
		sign = "-"
		total.Neg(total)
	}
	// keep 19 significant digits, rounding half up on the rest
	extra := len(total.String()) - digits
	bump := new(big.Int).Mul(big.NewInt(half), pow10(extra-1))
	kept := new(big.Int).Quo(total.Add(total, bump), pow10(extra))
	if kept.Cmp(pow10(digits)) == 0 {
		kept.Quo(kept, big.NewInt(10))
		extra++
	}
	text := kept.String()
	fmt.Printf("%s%s.%se%d\n", sign, text[:1], text[1:], extra+digits-1-shift)
}
