package main

import (
	"bufio"
	"fmt"
	"os"
)

// largest is the largest input
const largest = 10

func main() {
	// a(n) counts weak orders of n objects: the k objects tied for the
	// smallest place are any k of them, followed by a weak order of the rest
	var binom [largest + 1][largest + 1]int64
	var a [largest + 1]int64
	a[0] = 1
	for n := 0; n <= largest; n++ {
		binom[n][0], binom[n][n] = 1, 1
		for k := 1; k < n; k++ {
			binom[n][k] = binom[n-1][k-1] + binom[n-1][k]
		}
	}
	for n := 1; n <= largest; n++ {
		for k := 1; k <= n; k++ {
			a[n] += binom[n][k] * a[n-k]
		}
	}
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for {
		var n int
		if _, err := fmt.Fscan(in, &n); err != nil || n < 0 {
			break
		}
		fmt.Fprintln(out, a[n])
	}
}
