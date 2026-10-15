package main

import "fmt"

const eps = 1e-9 // keeps an exact integer whole; no expectation lies that close below one

func gcd(a, b int64) int64 {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func main() {
	var n int
	if _, err := fmt.Scan(&n); err != nil {
		return
	}
	// dp[s][l]: the chance that a random permutation of s elements has only
	// cycles of the lengths seen so far, and that their lcm is l
	dp := make([]map[int64]float64, n+1)
	for s := range dp {
		dp[s] = map[int64]float64{}
	}
	dp[0][1] = 1
	for k := 1; k <= n; k++ {
		next := make([]map[int64]float64, n+1)
		for s := range dp {
			next[s] = make(map[int64]float64, len(dp[s]))
			for l, w := range dp[s] {
				next[s][l] = w
			}
		}
		for s := 0; s < n; s++ {
			for l, w := range dp[s] {
				joined := l / gcd(l, int64(k)) * int64(k)
				weight := w
				for m := 1; s+m*k <= n; m++ {
					weight /= float64(k * m) // m cycles of length k: 1 / (k^m m!)
					next[s+m*k][joined] += weight
				}
			}
		}
		dp = next
	}
	expected := 0.0
	for l, w := range dp[n] {
		expected += float64(l) * w
	}
	fmt.Println(int64(expected + eps))
}
