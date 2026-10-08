package main

import "fmt"

func main() {
	var n, k int64
	fmt.Scan(&n, &k)
	// numbers of valid prefixes ending with a zero and with another digit,
	// where the first digit is not zero
	zero, other := int64(0), k-1
	for i := int64(1); i < n; i++ {
		zero, other = other, (zero+other)*(k-1)
	}
	fmt.Println(zero + other)
}
