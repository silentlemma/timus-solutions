package main

import "fmt"

func main() {
	var n int
	if _, err := fmt.Scan(&n); err != nil {
		return
	}
	for k := 0; k < n; k++ {
		// kids take the first free horse at or after a random one: linear
		// probing on a circle of n slots with k taken. By Knuth's analysis
		// the wait is (Q - 1)/2 with Q = sum (j + 1) k!/(k - j)! / n^j
		q, term := 0.0, 1.0
		for j := 0; j <= k; j++ {
			q += float64(j+1) * term
			term *= float64(k-j) / float64(n)
		}
		fmt.Printf("%.9f\n", (q-1)/2)
	}
}
