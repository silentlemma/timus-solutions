package main

import "fmt"

// p is a prime above the 4e9 + 1 possible answers and below 2^32, so products
// fit in 64 bits; no Fibonacci number with index up to 2000 is divisible by it
const p uint64 = 4294967291

func reduce(v int64) uint64 {
	return uint64((v%int64(p) + int64(p)) % int64(p))
}

func power(b, e uint64) uint64 {
	r := uint64(1)
	for ; e > 0; e, b = e/2, b*b%p {
		if e%2 == 1 {
			r = r * b % p
		}
	}
	return r
}

func main() {
	var i, fi, j, fj, n int64
	fmt.Scan(&i, &fi, &j, &fj, &n)
	if i > j {
		i, fi, j, fj = j, fj, i, fi
	}
	// F(j) = A F(i) + B F(i + 1), with A and B found by stepping coefficients
	a, b, na, nb := uint64(1), uint64(0), uint64(0), uint64(1)
	for k := i; k < j; k++ {
		a, b, na, nb = na, nb, (a+na)%p, (b+nb)%p
	}
	cur := reduce(fi)
	next := (reduce(fj) + p - a*cur%p) % p * power(b, p-2) % p
	for k := i; k < n; k++ {
		cur, next = next, (cur+next)%p
	}
	for k := i; k > n; k-- {
		cur, next = (next+p-cur)%p, cur
	}
	answer := int64(cur)
	if cur > p/2 {
		answer -= int64(p)
	}
	fmt.Println(answer)
}
