package main

import "fmt"

const (
	mod    = 1000000009
	low    = 100 // the three-digit numbers
	high   = 1000
	pairs  = 100 // the last two digits
	base   = 10
	window = 3 // neighbouring digits that form a prime
)

func main() {
	var n int
	fmt.Scan(&n)
	var primes []int
	for p := low; p < high; p++ {
		prime := true
		for d := 2; d*d <= p; d++ {
			if p%d == 0 {
				prime = false
			}
		}
		if prime {
			primes = append(primes, p)
		}
	}
	// ways[t]: numbers of the length so far that end in the two digits t and
	// whose every three neighbouring digits form a three-digit prime
	ways := make([]int64, pairs)
	for _, p := range primes {
		ways[p%pairs]++
	}
	for step := window; step < n; step++ {
		next := make([]int64, pairs)
		// a prime abc extends a number ending in ab to one ending in bc
		for _, p := range primes {
			next[p%pairs] = (next[p%pairs] + ways[p/base]) % mod
		}
		ways = next
	}
	total := int64(0)
	for _, w := range ways {
		total = (total + w) % mod
	}
	fmt.Println(total)
}
