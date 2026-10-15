package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var s string
	if _, err := fmt.Fscan(in, &s); err != nil {
		return
	}
	n := len(s)
	// dp[j]: fewest palindromes for the prefix of length j. Centres go left
	// to right, so every palindrome s[l..r] meets a final dp[l]: those that
	// end before l have their centres before l.
	dp, prev := make([]int, n+1), make([]int, n+1)
	for j := 1; j <= n; j++ {
		dp[j] = n + 1
	}
	for twice := 0; twice < 2*n-1; twice++ {
		l := twice / 2
		r := l + twice%2
		for l >= 0 && r < n && s[l] == s[r] {
			if dp[l]+1 < dp[r+1] {
				dp[r+1] = dp[l] + 1
				prev[r+1] = l
			}
			l--
			r++
		}
	}
	var parts []string
	for end := n; end > 0; end = prev[end] {
		parts = append(parts, s[prev[end]:end])
	}
	for i, j := 0, len(parts)-1; i < j; i, j = i+1, j-1 {
		parts[i], parts[j] = parts[j], parts[i]
	}
	fmt.Println(dp[n])
	fmt.Println(strings.Join(parts, " "))
}
