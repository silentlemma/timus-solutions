package main

import (
	"fmt"
	"math/big"
)

func main() {
	var n int
	fmt.Scan(&n)
	// a number of k digits 1 and 2 divisible by 2^k: put 1 or 2 in front of the
	// one for k - 1, whichever keeps one more factor 2
	value, power := new(big.Int), big.NewInt(1)
	ten := big.NewInt(10)
	digits := make([]byte, n)
	for k := 0; k < n; k++ {
		next := new(big.Int).Add(value, power)
		d := byte('1')
		// divisible by 2^(k+1): no set bit below k + 1
		if next.TrailingZeroBits() <= uint(k) {
			next.Add(next, power)
			d = '2'
		}
		value = next
		digits[n-1-k] = d
		power.Mul(power, ten)
	}
	fmt.Println(string(digits))
}
