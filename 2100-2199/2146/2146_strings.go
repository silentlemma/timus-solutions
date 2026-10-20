package main

import (
	"bufio"
	"fmt"
	"os"
)

const letters = 26

func main() {
	reader := bufio.NewReader(os.Stdin)
	var n, k int
	var s string
	fmt.Fscan(reader, &n, &k, &s)
	// On a circle every period can be replaced by its gcd with n, so only the
	// divisors of n are tried, from the smallest.
	for d := 1; d <= n; d++ {
		if n%d != 0 {
			continue
		}
		count := make([]int, d*letters)
		for i := 0; i < n; i++ {
			count[(i%d)*letters+int(s[i]-'a')]++
		}
		best := make([]byte, d)
		changes := n
		for r := 0; r < d; r++ {
			top := 0
			for c := 1; c < letters; c++ {
				if count[r*letters+c] > count[r*letters+top] {
					top = c
				}
			}
			best[r] = byte('a' + top)
			changes -= count[r*letters+top]
		}
		if changes <= k {
			result := make([]byte, n)
			for i := range result {
				result[i] = best[i%d]
			}
			fmt.Printf("%d\n%s\n", d, result)
			return
		}
	}
}
