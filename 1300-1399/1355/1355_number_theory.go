package main

import (
	"bufio"
	"fmt"
	"os"
)

// primeFactors: how many primes multiply to n, counted with repetition.
func primeFactors(n int64) int {
	count := 0
	for d := int64(2); d*d <= n; d++ {
		for n%d == 0 {
			n /= d
			count++
		}
	}
	if n > 1 {
		count++
	}
	return count
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var t int
	fmt.Fscan(in, &t)
	for ; t > 0; t-- {
		var a, b int64
		fmt.Fscan(in, &a, &b)
		// every step multiplies the number by at least one prime
		if b%a == 0 {
			fmt.Fprintln(out, 1+primeFactors(b/a))
		} else {
			fmt.Fprintln(out, 0)
		}
	}
}
