package main

import (
	"bufio"
	"fmt"
	"os"
)

// smallest starts trial division: n is a product of two odd primes
const smallest = 3

func power(b, e, n int64) int64 {
	r := int64(1)
	for b %= n; e > 0; e, b = e/2, b*b%n {
		if e%2 == 1 {
			r = r * b % n
		}
	}
	return r
}

// inverse is the inverse of e modulo phi by the extended Euclidean algorithm
func inverse(e, phi int64) int64 {
	a, b, x, y := e%phi, phi, int64(1), int64(0)
	for b != 0 {
		q := a / b
		a, b = b, a-q*b
		x, y = y, x-q*y
	}
	return (x%phi + phi) % phi
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var k int
	fmt.Fscan(in, &k)
	for ; k > 0; k-- {
		var e, n, c int64
		fmt.Fscan(in, &e, &n, &c)
		p := int64(smallest)
		for n%p != 0 {
			p += 2
		}
		phi := (p - 1) * (n/p - 1)
		// m^(e d) = m modulo n when e d = 1 modulo phi, so the private
		// exponent d undoes the public one
		fmt.Fprintln(out, power(c, inverse(e, phi), n))
	}
}
