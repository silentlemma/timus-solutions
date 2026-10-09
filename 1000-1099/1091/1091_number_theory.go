package main

import "fmt"

const capacity = 10000

func main() {
	var k, s int
	fmt.Scan(&k, &s)
	binom := make([][]int64, s+1)
	for n := range binom {
		binom[n] = make([]int64, s+1)
		binom[n][0] = 1
		for r := 1; r <= n; r++ {
			binom[n][r] = binom[n-1][r-1] + binom[n-1][r]
		}
	}
	// Moebius function by a sieve: -1 per prime factor, 0 with a square factor
	mu := make([]int64, s+1)
	prime := make([]bool, s+1)
	for i := range mu {
		mu[i], prime[i] = 1, true
	}
	for p := 2; p <= s; p++ {
		if !prime[p] {
			continue
		}
		for m := p; m <= s; m += p {
			prime[m] = m == p
			mu[m] = -mu[m]
		}
		for m := p * p; m <= s; m += p * p {
			mu[m] = 0
		}
	}
	// inclusion-exclusion: sets of multiples of d count with the sign -mu(d)
	var total int64
	for d := 2; d <= s; d++ {
		if s/d >= k {
			total -= mu[d] * binom[s/d][k]
		}
	}
	if total > capacity {
		total = capacity
	}
	fmt.Println(total)
}
