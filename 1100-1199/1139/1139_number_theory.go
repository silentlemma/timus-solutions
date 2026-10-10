package main

import "fmt"

func gcd(a, b int64) int64 {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func main() {
	var n, m int64
	fmt.Scan(&n, &m)
	// an a by b grid: the diagonal crosses a + b - 2 inner lines, two at once
	// at each of the gcd(a, b) - 1 inner corners; it starts in one block and
	// every crossing enters a new one
	a, b := n-1, m-1
	fmt.Println(a + b - gcd(a, b))
}
