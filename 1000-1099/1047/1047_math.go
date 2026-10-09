package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

const cents = 100

func main() {
	in := bufio.NewReader(os.Stdin)
	// the input numbers in hundredths
	readCents := func() int64 {
		var v float64
		fmt.Fscan(in, &v)
		return int64(math.Round(v * cents))
	}
	var n int64
	fmt.Fscan(in, &n)
	first, last := readCents(), readCents()
	// with d[i] = a[i] - a[i-1] the relation reads d[i+1] = d[i] + 2 c[i], so
	// a[N+1] - a[0] = (N + 1) d[1] + 2 sum (N + 1 - i) c[i]
	var weighted int64
	for i := int64(1); i <= n; i++ {
		weighted += (n + 1 - i) * readCents()
	}
	num, den := n*first+last-2*weighted, n+1
	// the answer has two decimals; rounding only guards against bad input
	abs := num
	if abs < 0 {
		abs = -abs
	}
	q := (2*abs + den) / (2 * den)
	sign := ""
	if num < 0 && q > 0 {
		sign = "-"
	}
	fmt.Printf("%s%d.%02d\n", sign, q/cents, q%cents)
}
