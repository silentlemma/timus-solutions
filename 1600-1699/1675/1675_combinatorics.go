package main

import "fmt"

const mod = 1000000007

func power(base, exp int64) int64 {
	result := int64(1)
	for base %= mod; exp > 0; exp >>= 1 {
		if exp&1 == 1 {
			result = result * base % mod
		}
		base = base * base % mod
	}
	return result
}

func main() {
	var m, n, k, l int
	fmt.Scan(&m, &n, &k, &l)
	top := m
	if n > top {
		top = n
	}
	fact, inv := make([]int64, top+1), make([]int64, top+1)
	fact[0] = 1
	for i := 1; i <= top; i++ {
		fact[i] = fact[i-1] * int64(i) % mod
	}
	inv[top] = power(fact[top], mod-2)
	for i := top; i > 0; i-- {
		inv[i-1] = inv[i] * int64(i) % mod
	}
	choose := func(a, b int) int64 { return fact[a] * inv[b] % mod * inv[a-b] % mod }
	// the other a x b cells must leave no row and no column empty. With j of
	// the b columns forced empty, each of the a rows is any nonzero pattern
	// on the rest; inclusion-exclusion over j, along the shorter side
	a, b := m-k, n-l
	if a > b {
		a, b = b, a
	}
	rest := int64(0)
	for j := 0; j <= a; j++ {
		term := choose(a, j) * power((power(2, int64(a-j))-1+mod)%mod, int64(b)) % mod
		if j%2 == 1 {
			term = mod - term
		}
		rest = (rest + term) % mod
	}
	fmt.Println(choose(m, k) * choose(n, l) % mod * rest % mod)
}
