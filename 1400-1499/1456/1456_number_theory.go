package main

import "fmt"

func gcd(a, b int64) int64 {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func primesOf(n int64) []int64 {
	var found []int64
	for p := int64(2); p*p <= n; p++ {
		if n%p == 0 {
			found = append(found, p)
			for n%p == 0 {
				n /= p
			}
		}
	}
	if n > 1 {
		found = append(found, n)
	}
	return found
}

func power(base, exp, mod int64) int64 {
	result := int64(1)
	base %= mod
	for ; exp > 0; exp >>= 1 {
		if exp&1 == 1 {
			result = result * base % mod
		}
		base = base * base % mod
	}
	return result
}

func main() {
	var a, n int64
	fmt.Scan(&a, &n)
	if gcd(a, n) != 1 { // the remainders keep a common factor with N and never reach 1
		fmt.Println(0)
		return
	}
	// the order divides phi(N): strip prime factors while a power stays 1
	phi := n
	for _, p := range primesOf(n) {
		phi = phi / p * (p - 1)
	}
	order := phi
	for _, p := range primesOf(phi) {
		for order%p == 0 && power(a, order/p, n) == 1 {
			order /= p
		}
	}
	fmt.Println(order)
}
