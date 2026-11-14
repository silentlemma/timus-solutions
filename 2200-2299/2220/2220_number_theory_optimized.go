package main

import (
	"bufio"
	"fmt"
	"os"
)

const modulus int64 = 1000000007
const sieveLimit = 100000
const groupSize = 4

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
	n, limit int
	small    []uint32
	large    []int64
}

func (t *totients) get(x int) int64 {
	if x <= t.limit {
		return int64(t.small[x])
	}
	return t.large[t.n/x]
}

func newTotients(n int) *totients {
	limit := n
	if limit > sieveLimit {
		limit = sieveLimit
	}
	t := &totients{n: n, limit: limit, small: make([]uint32, limit+1)}
	for i := range t.small {
		t.small[i] = uint32(i)
	}
	for prime := 2; prime <= limit; prime++ {
		if t.small[prime] == uint32(prime) {
			for multiple := prime; multiple <= limit; multiple += prime {
				t.small[multiple] -= t.small[multiple] / uint32(prime)
			}
		}
	}
	for i := 1; i <= limit; i++ {
		t.small[i] += t.small[i-1]
		if t.small[i] >= uint32(modulus) {
			t.small[i] -= uint32(modulus)
		}
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
		t.large[index] = (total%modulus + modulus) % modulus
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
		i, end := int64(left), int64(right)
		for ; i+groupSize-1 <= end; i += groupSize {
			// Two pairs give the product and its derivative by the product rule.
			j := i + 2
			first := i * (i + 1) % modulus
			second := j * (j + 1) % modulus
			product := first * second % modulus
			derivative := ((2*i+1)*second + (2*j+1)*first) % modulus
			weighted = (weighted*product + factorial*derivative) % modulus
			factorial = factorial * product % modulus
		}
		for ; i <= end; i++ {
			weighted = (weighted*i + factorial) % modulus
			factorial = factorial * i % modulus
		}
		harmonic := weighted * power(factorial, modulus-2) % modulus
		difference := (harmonic - previous + modulus) % modulus
		total = (total + difference*t.get(quotient)) % modulus
		previous = harmonic
		left = right + 1
	}
	pairs := int64(n) * int64(n+1) / 2 % modulus
	fmt.Println(total * power(pairs, modulus-2) % modulus)
}
