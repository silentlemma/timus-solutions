package main

import "fmt"

const smallest = 3

func main() {
	var k int64
	fmt.Scan(&k)
	// the second player wins exactly when L + 1 divides K: find the smallest
	// divisor of K that is at least 3
	for d := int64(smallest); d*d <= k; d++ {
		if k%d == 0 {
			fmt.Println(d - 1)
			return
		}
	}
	// no such divisor up to sqrt(K): above it the candidates are K / 2 and K
	d := k
	if k%2 == 0 && k/2 >= smallest {
		d = k / 2
	}
	fmt.Println(d - 1)
}
