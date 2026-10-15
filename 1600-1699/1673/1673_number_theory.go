package main

import (
	"fmt"
	"sort"
)

// witnesses are enough for a deterministic test below 3.2 * 10^9
var witnesses = []int64{2, 3, 5, 7}

func power(base, exp, mod int64) int64 {
	result := int64(1)
	for base %= mod; exp > 0; exp >>= 1 {
		if exp&1 == 1 {
			result = result * base % mod
		}
		base = base * base % mod
	}
	return result
}

// isPrime is Miller-Rabin with fixed witnesses, exact for these sizes.
func isPrime(n int64) bool {
	if n < 2 {
		return false
	}
	for _, p := range witnesses {
		if n%p == 0 {
			return n == p
		}
	}
	d, s := n-1, 0
	for d%2 == 0 {
		d /= 2
		s++
	}
	for _, a := range witnesses {
		x := power(a, d, n)
		if x == 1 || x == n-1 {
			continue
		}
		composite := true
		for i := 1; i < s && composite; i++ {
			x = x * x % n
			composite = x != n-1
		}
		if composite {
			return false
		}
	}
	return true
}

type key struct {
	rest  int64
	start int
}

var primes []int64
var memo = map[key]int64{}

// least is the smallest product of powers of primes[start:] whose totient
// is rest, or 0 if there is none.
func least(rest int64, start int) int64 {
	if rest == 1 {
		return 1
	}
	if v, ok := memo[key{rest, start}]; ok {
		return v
	}
	best := int64(0)
	for i := start; i < len(primes) && primes[i]-1 <= rest; i++ {
		p := primes[i]
		if rest%(p-1) != 0 {
			continue
		}
		part, pw := rest/(p-1), p
		for {
			if sub := least(part, i+1); sub != 0 && (best == 0 || pw*sub < best) {
				best = pw * sub
			}
			if part%p != 0 {
				break
			}
			part /= p
			pw *= p
		}
	}
	memo[key{rest, start}] = best
	return best
}

func main() {
	var k int64
	fmt.Scan(&k)
	// student j is admitted exactly when gcd(j, N) = 1, so K = phi(N); every
	// p - 1 over the primes of N divides K, so the candidates are d + 1, d | K
	divs := []int64{1}
	rest := k
	for p := int64(2); p*p <= rest; p++ {
		if rest%p == 0 {
			size, pw := len(divs), int64(1)
			for rest%p == 0 {
				rest /= p
				pw *= p
				for i := 0; i < size; i++ {
					divs = append(divs, divs[i]*pw)
				}
			}
		}
	}
	if rest > 1 {
		for _, d := range append([]int64(nil), divs...) {
			divs = append(divs, d*rest)
		}
	}
	sort.Slice(divs, func(i, j int) bool { return divs[i] < divs[j] })
	for _, d := range divs {
		if isPrime(d + 1) {
			primes = append(primes, d+1)
		}
	}
	fmt.Println(least(k, 0))
}
