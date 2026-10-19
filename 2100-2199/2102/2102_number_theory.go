package main

import "fmt"

const (
	target = 20
	bound  = 2000000 // trial divisors; beyond them at most two primes remain
)

func main() {
	var n int64
	fmt.Scan(&n)
	count := 0
	d := int64(2)
	for ; d <= bound && d*d <= n; d++ {
		for n%d == 0 {
			n /= d
			count++
		}
	}
	if n > 1 {
		if d*d > n {
			count++ // what is left is prime
		} else {
			// n >= bound^2 here, so the divided part is at most 10^18 / bound^2,
			// fewer than 18 factors, and the rest adds at most two
			count = -1
		}
	}
	if count == target {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
