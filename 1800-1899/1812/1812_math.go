package main

import (
	"fmt"
	"math"
)

func gcd(a, b int64) int64 {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func isqrt(v int64) int64 {
	r := int64(math.Sqrt(float64(v)))
	for r*r > v {
		r--
	}
	for (r+1)*(r+1) <= v {
		r++
	}
	return r
}

func main() {
	var r1, r2, n, i int64
	if _, err := fmt.Scan(&r1, &r2, &n, &i); err != nil {
		return
	}
	pos := i - 1
	if pos == 0 {
		fmt.Printf("%d/1\n", r1)
		return
	}
	if pos == 1<<uint(n) {
		fmt.Printf("%d/1\n", r2)
		return
	}
	// between touching neighbours 1/sqrt(r) adds up, so circle pos has
	// 1/sqrt(r) = a/sqrt(r1) + b/sqrt(r2), with a and b from Stern's sequence
	// found as alpha f(x) + beta f(x + 1) while x is halved level by level
	alpha, beta, x := int64(1), int64(0), pos
	for level := int64(0); level < n; level++ {
		if x%2 == 0 {
			alpha += beta
		} else {
			beta += alpha
		}
		x /= 2
	}
	// with both a and b positive the radius is rational exactly when
	// r1 = g p^2 and r2 = g q^2 for g = gcd(r1, r2)
	g := gcd(r1, r2)
	p, q := isqrt(r1/g), isqrt(r2/g)
	if p*p*g != r1 || q*q*g != r2 {
		fmt.Println("Irrational")
		return
	}
	// r = 1 / ((a q + b p) / (p q sqrt(g)))^2
	d := alpha*q + beta*p
	num, den := g*p*p*q*q, d*d
	common := gcd(num, den)
	fmt.Printf("%d/%d\n", num/common, den/common)
}
