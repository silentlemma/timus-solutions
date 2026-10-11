package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	// Euler's totient: the turns 2*pi*m/n with gcd(m, n) = 1
	phi, rest := n, n
	for p := 2; p*p <= rest; p++ {
		if rest%p == 0 {
			for rest%p == 0 {
				rest /= p
			}
			phi -= phi / p
		}
	}
	if rest > 1 {
		phi -= phi / rest
	}
	fmt.Println(phi / 2)
}
