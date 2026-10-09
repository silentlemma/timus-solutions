package main

import "fmt"

const (
	count = 10
	base  = 10
)

func main() {
	// the exponents of the primes in the product of all the numbers
	exponent := map[int]int{}
	for i := 0; i < count; i++ {
		var x int
		fmt.Scan(&x)
		for p := 2; p*p <= x; p++ {
			for ; x%p == 0; x /= p {
				exponent[p]++
			}
		}
		if x > 1 {
			exponent[x]++
		}
	}
	// a divisor picks each prime from 0 to its exponent times
	last := 1
	for _, e := range exponent {
		last = last * (e + 1) % base
	}
	fmt.Println(last)
}
