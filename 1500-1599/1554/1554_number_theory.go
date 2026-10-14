package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const mod = 2007

// inverse returns x^-1 modulo mod by the extended Euclidean algorithm
func inverse(x int) int {
	a, b, u, v := x%mod, mod, 1, 0
	for b != 0 {
		q := a / b
		a, b = b, a-q*b
		u, v = v, u-q*v
	}
	return (u%mod + mod) % mod
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	f := make([]int, n+1)
	for i := 1; i <= n; i++ {
		fmt.Fscan(in, &f[i])
		f[i] %= mod
	}
	// (F * G)(n) sums F(n / d) G(d) over the divisors d of n and is 0 for n > 1,
	// so G(n) = -G(1) * (the sum over the proper divisors), with G(1) = 1 / F(1),
	// and a sieve adds G(d) times F to every multiple of d once G(d) is known
	first := inverse(f[1])
	g, acc := make([]int, n+1), make([]int, n+1)
	parts := make([]string, n)
	for d := 1; d <= n; d++ {
		if d == 1 {
			g[d] = first
		} else {
			g[d] = (mod - first*acc[d]%mod) % mod
		}
		for k := 2; d*k <= n; k++ {
			acc[d*k] = (acc[d*k] + f[k]*g[d]) % mod
		}
		parts[d-1] = strconv.Itoa(g[d])
	}
	fmt.Println(strings.Join(parts, " "))
}
