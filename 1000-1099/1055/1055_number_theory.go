package main

import "fmt"

// exponent of the prime p in x! (Legendre's formula)
func exponent(x, p int) int {
	e := 0
	for ; x > 0; x /= p {
		e += x / p
	}
	return e
}

func main() {
	var n, m int
	fmt.Scan(&n, &m)
	composite := make([]bool, n+1)
	count := 0
	for p := 2; p <= n; p++ {
		if composite[p] {
			continue
		}
		for q := p * p; q <= n; q += p {
			composite[q] = true
		}
		if exponent(n, p)-exponent(m, p)-exponent(n-m, p) > 0 {
			count++
		}
	}
	fmt.Println(count)
}
