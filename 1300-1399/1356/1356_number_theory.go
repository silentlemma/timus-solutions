package main

import (
	"bufio"
	"fmt"
	"os"
)

// these bases make Miller-Rabin exact for every n below 3.2 * 10^9
var bases = []int64{2, 3, 5, 7}

const smallestSplit = 4 // the smallest even number that is a sum of two primes

func power(b, e, m int64) int64 {
	r := int64(1)
	b %= m
	for ; e > 0; e >>= 1 {
		if e&1 == 1 {
			r = r * b % m
		}
		b = b * b % m
	}
	return r
}

func isPrime(n int64) bool {
	if n < 2 {
		return false
	}
	for _, b := range bases {
		if n%b == 0 {
			return n == b
		}
	}
	d, s := n-1, 0
	for d%2 == 0 {
		d /= 2
		s++
	}
	for _, b := range bases {
		x := power(b, d, n)
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

// twoPrimes: an even n >= 4 as the smallest prime p and n - p.
func twoPrimes(n int64) []int64 {
	p := int64(2)
	for !(isPrime(p) && isPrime(n-p)) {
		p++
	}
	return []int64{p, n - p}
}

func split(n int64) []int64 {
	if isPrime(n) {
		return []int64{n}
	}
	if n%2 == 0 {
		return twoPrimes(n)
	}
	if isPrime(n - 2) {
		return []int64{2, n - 2}
	}
	// the largest prime p that leaves an even rest of at least 4
	p := n - smallestSplit
	for !isPrime(p) {
		p -= 2
	}
	return append([]int64{p}, twoPrimes(n-p)...)
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var t int
	fmt.Fscan(in, &t)
	for ; t > 0; t-- {
		var n int64
		fmt.Fscan(in, &n)
		for i, p := range split(n) {
			if i > 0 {
				out.WriteByte(' ')
			}
			fmt.Fprint(out, p)
		}
		out.WriteByte('\n')
	}
}
