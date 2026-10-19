package main

import (
	"fmt"
	"math/big"
)

func main() {
	var a, n int64
	fmt.Scan(&a, &n)
	var primes []int64
	rest := n
	for p := int64(2); p*p <= rest; p++ {
		if rest%p == 0 {
			primes = append(primes, p)
			for rest%p == 0 {
				rest /= p
			}
		}
	}
	if rest > 1 {
		primes = append(primes, rest)
	}
	// keys up to rotation without a shorter period are Lyndon words: by
	// Moebius inversion n times their number is the sum over square-free
	// divisors d of n of mu(d) a^(n / d)
	total := new(big.Int)
	for mask := 0; mask < 1<<len(primes); mask++ {
		d, negative := int64(1), false
		for i, p := range primes {
			if mask>>i&1 == 1 {
				d *= p
				negative = !negative
			}
		}
		term := new(big.Int).Exp(big.NewInt(a), big.NewInt(n/d), nil)
		if negative {
			total.Sub(total, term)
		} else {
			total.Add(total, term)
		}
	}
	fmt.Println(total.Div(total, big.NewInt(n)).String())
}
