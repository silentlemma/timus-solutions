package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var n int
	fmt.Fscan(in, &n)
	a := make([]int, n)
	for i := range a {
		fmt.Fscan(in, &a[i])
	}
	// n + 1 prefix sums modulo n take at most n values: two of them are
	// equal, and the numbers between them sum to a multiple of n
	first := make([]int, n)
	for i := range first {
		first[i] = -1
	}
	first[0] = 0
	sum := 0
	for i := 1; i <= n; i++ {
		sum = (sum + a[i-1]) % n
		if first[sum] >= 0 {
			fmt.Fprintln(out, i-first[sum])
			for _, x := range a[first[sum]:i] {
				fmt.Fprintln(out, x)
			}
			return
		}
		first[sum] = i
	}
}
