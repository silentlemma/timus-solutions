package main

import "fmt"

// divisorSum is the sum of all divisors of n by trial division
func divisorSum(n int64) int64 {
	total := int64(0)
	for d := int64(1); d*d <= n; d++ {
		if n%d == 0 {
			if d*d == n {
				total += d
			} else {
				total += d + n/d
			}
		}
	}
	return total
}

func main() {
	var lo, hi int64
	fmt.Scan(&lo, &hi)
	// 1 has no proper divisors at all
	if lo == 1 {
		fmt.Println(1)
		return
	}
	// a prime p has the ratio 1/p, and the largest prime in range beats every
	// composite there (it is above hi / 2 by Bertrand's postulate), so only a
	// range without primes, at most 113 numbers here, needs comparing
	for n := hi; n >= lo; n-- {
		if divisorSum(n) == n+1 {
			fmt.Println(n)
			return
		}
	}
	best := lo
	for n := lo + 1; n <= hi; n++ {
		// sigma(n) / n < sigma(best) / best, the smaller number winning a tie
		if divisorSum(n)*best < divisorSum(best)*n {
			best = n
		}
	}
	fmt.Println(best)
}
