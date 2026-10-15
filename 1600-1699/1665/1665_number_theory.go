package main

import (
	"bufio"
	"fmt"
	"os"
)

const firstOdd = 3 // the smallest divisor worth trying

// paid tells whether n is a product of an odd number of factors, each 2 or
// an odd number above 1: n = 2^twos * rest with rest odd.
func paid(n int64) bool {
	twos := 0
	for n%2 == 0 {
		n /= 2
		twos++
	}
	if n == 1 {
		return twos%2 == 1
	}
	if twos%2 == 0 {
		return true // rest as a single factor
	}
	// an odd count needs rest split into two factors, so not a prime
	for d := int64(firstOdd); d*d <= n; d += 2 {
		if n%d == 0 {
			return true
		}
	}
	return false
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var t int
	fmt.Fscan(in, &t)
	for ; t > 0; t-- {
		var n int64
		fmt.Fscan(in, &n)
		if paid(n) {
			fmt.Fprintln(out, "YES")
		} else {
			fmt.Fprintln(out, "NO")
		}
	}
}
