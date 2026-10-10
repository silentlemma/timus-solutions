package main

import (
	"fmt"
	"math"
	"math/big"
)

func gcd(a, b int64) int64 {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func main() {
	var n, m int64
	fmt.Scan(&n, &m)
	// from the target backwards: the last m km take one load; before it, a
	// stretch of m / (2k - 1) km is crossed 2k - 1 times to bring k loads
	stretch := 0.0
	k := int64(1)
	for stretch+float64(m)/float64(2*k-1) < float64(n) {
		stretch += float64(m) / float64(2*k-1)
		k++
	}
	// fuel = (k-1) m + (2k-1) n - sum over i < k of m (2k-1) / (2i-1); its
	// fractional sum f = sum r_i / (2i-1) is kept exactly as num / den
	whole := (k-1)*m + (2*k-1)*n
	num, den := big.NewInt(0), big.NewInt(1)
	approx := 0.0
	rest, part := new(big.Int), new(big.Int)
	for i := int64(1); i < k; i++ {
		d := 2*i - 1
		r := m * (2*k - 1) % d
		whole -= m * (2*k - 1) / d
		if r == 0 {
			continue
		}
		approx += float64(r) / float64(d)
		g := gcd(d, rest.Mod(den, big.NewInt(d)).Int64())
		scale := big.NewInt(d / g)
		// num/den + r/d over the denominator den * (d / g)
		part.Div(den, big.NewInt(g))
		part.Mul(part, big.NewInt(r))
		num.Mul(num, scale)
		num.Add(num, part)
		den.Mul(den, scale)
	}
	// floor(f) from its approximation, then corrected exactly
	t := int64(math.Floor(approx))
	times := func(v int64) *big.Int { return new(big.Int).Mul(den, big.NewInt(v)) }
	for t > 0 && times(t).Cmp(num) > 0 {
		t--
	}
	for times(t+1).Cmp(num) <= 0 {
		t++
	}
	fmt.Println(whole - t)
}
