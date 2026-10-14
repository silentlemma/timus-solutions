package main

import "fmt"

func gcd(a, b int64) int64 {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func main() {
	var n int64
	if _, err := fmt.Scan(&n); err != nil {
		return
	}
	// the chance that the row ends with two cards: (n^2 + 3n - 2) / (2n (2n - 1))
	num := n*(n+2) + n - 2
	den := 2 * n * (2*n - 1)
	g := gcd(num, den)
	fmt.Printf("%d/%d\n", num/g, den/g)
}
