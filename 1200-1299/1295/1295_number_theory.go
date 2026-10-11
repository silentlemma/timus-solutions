package main

import "fmt"

const mod = 100
const bases = 4

func power(base, n int) int {
	r := 1
	for ; n > 0; n >>= 1 {
		if n&1 == 1 {
			r = r * base % mod
		}
		base = base * base % mod
	}
	return r
}

func main() {
	var n int
	fmt.Scan(&n)
	// from the second power on the sum is even but never divisible by 8,
	// so it ends in at most two zeros and its remainder mod 100 decides
	s := 0
	for b := 1; b <= bases; b++ {
		s = (s + power(b, n)) % mod
	}
	switch {
	case s == 0:
		fmt.Println(2)
	case s%10 == 0:
		fmt.Println(1)
	default:
		fmt.Println(0)
	}
}
