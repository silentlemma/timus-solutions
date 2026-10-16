package main

import (
	"bufio"
	"fmt"
	"math/bits"
	"os"
)

func gcd(a, b uint64) uint64 {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

// floorSum is the sum of (a*i + b) / m over i = 0 .. n-1. Every term
// added is a part of the result, which stays below 2^63 here, so only
// a*n + b needs 128 bits; its quotient by m is below n + 1.
func floorSum(n, m, a, b uint64) uint64 {
	total := uint64(0)
	for {
		if a >= m {
			total += n * (n - 1) / 2 * (a / m)
			a %= m
		}
		if b >= m {
			total += n * (b / m)
			b %= m
		}
		hi, lo := bits.Mul64(a, n)
		lo, carry := bits.Add64(lo, b, 0)
		hi += carry
		if hi == 0 && lo < m {
			return total
		}
		n, b = bits.Div64(hi, lo, m)
		m, a = a, m
	}
}

// countUpTo is how many numbers from 1 to limit are a*x + b*y with
// a, b >= 0
func countUpTo(limit, x, y uint64) uint64 {
	g := gcd(x, y)
	limit, x, y = limit/g, x/g, y/g
	// with x and y coprime every such number has exactly one form with
	// b < x; for each b the values of a run from 0 to (limit - b*y) / x
	last := limit / y
	if x-1 < last {
		last = x - 1
	}
	forms := floorSum(last+1, x, y, limit-y*last) + last + 1
	return forms - 1 // zero is not a volume size
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	var tests int
	if _, err := fmt.Fscan(reader, &tests); err != nil {
		return
	}
	for ; tests > 0; tests-- {
		var x, y, l, r uint64
		fmt.Fscan(reader, &x, &y, &l, &r)
		fmt.Fprintln(writer, countUpTo(r, x, y)-countUpTo(l-1, x, y))
	}
}
