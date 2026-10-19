package main

import "fmt"

const mod = 1000000007

func main() {
	var n int
	fmt.Scan(&n)
	// F_n is the product of k^fib(n - k + 1) over k from 1 to n, with
	// fib(1) = fib(2) = 1; weight[k] = fib(n - k + 1) modulo mod
	fib := make([]int64, n+2)
	fib[1] = 1
	for i := 2; i <= n+1; i++ {
		fib[i] = (fib[i-1] + fib[i-2]) % mod
	}
	weight := make([]int64, n+1)
	for k := 1; k <= n; k++ {
		weight[k] = fib[n-k+1]
	}
	composite := make([]bool, n+1)
	// the exponent of a prime p sums the weights of the multiples of p, of
	// p^2, and so on; the divisors number the product of exponents plus 1
	answer := int64(1)
	for p := 2; p <= n; p++ {
		if composite[p] {
			continue
		}
		for q := p * p; q <= n; q += p {
			composite[q] = true
		}
		exponent := int64(0)
		for power := p; power <= n; power *= p {
			for k := power; k <= n; k += power {
				exponent += weight[k]
			}
			exponent %= mod
			if power > n/p {
				break
			}
		}
		answer = answer * ((exponent + 1) % mod) % mod
	}
	fmt.Println(answer)
}
