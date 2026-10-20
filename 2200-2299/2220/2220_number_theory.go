package main

import (
	"bufio"
	"fmt"
	"os"
)

const modulus int64 = 1000000007
const sieveLimit = 100000

func power(base, exponent int64) int64 {
	result := int64(1)
	for exponent > 0 {
		if exponent%2 == 1 {
			result = result * base % modulus
		}
		base = base * base % modulus
		exponent /= 2
	}
	return result
}

type totients struct {
	n, limit     int
	small, large []int64
}

func (t *totients) get(x int) int64 {
	if x <= t.limit {
		return t.small[x]
	}
	return t.large[t.n/x]
}

func newTotients(n int) *totients {
	limit := n
	if limit > sieveLimit {
		limit = sieveLimit
	}
	t := &totients{n: n, limit: limit, small: make([]int64, limit+1)}
	for i := range t.small {
		t.small[i] = int64(i)
	}
	for prime := 2; prime <= limit; prime++ {
		if t.small[prime] == int64(prime) {
			for multiple := prime; multiple <= limit; multiple += prime {
				t.small[multiple] -= t.small[multiple] / int64(prime)
			}
		}
	}
	for i := 1; i <= limit; i++ {
		t.small[i] += t.small[i-1]
	}
	count := n / (limit + 1)
	t.large = make([]int64, count+1)
	// Smaller quotient arguments have already been computed.
	for index := count; index >= 1; index-- {
		x := n / index
		total := int64(x) * int64(x+1) / 2
		for left := 2; left <= x; {
			quotient := x / left
			right := x / quotient
			total -= int64(right-left+1) * t.get(quotient)
			left = right + 1
		}
		t.large[index] = total
	}
	return t
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	t := newTotients(n)
	factorial, weighted, previous, total := int64(1), int64(0), int64(0), int64(0)
	for left := 1; left <= n; {
		quotient := n / left
		right := n / quotient
		// weighted is factorial times the current harmonic sum.
		for i := int64(left); i <= int64(right); i++ {
			weighted = (weighted*i + factorial) % modulus
			factorial = factorial * i % modulus
		}
		harmonic := weighted * power(factorial, modulus-2) % modulus
		difference := (harmonic - previous + modulus) % modulus
		total = (total + difference*(t.get(quotient)%modulus)) % modulus
		previous = harmonic
		left = right + 1
	}
	pairs := int64(n) * int64(n+1) / 2 % modulus
	fmt.Println(total * power(pairs, modulus-2) % modulus)
}
