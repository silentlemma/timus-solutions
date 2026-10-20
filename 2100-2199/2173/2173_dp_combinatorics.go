package main

import (
	"bufio"
	"fmt"
	"os"
)

const mod = 1000000007

func power(base, exponent int64) int64 {
	result := int64(1)
	base %= mod
	for exponent > 0 {
		if exponent&1 == 1 {
			result = result * base % mod
		}
		base = base * base % mod
		exponent >>= 1
	}
	return result
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var n, m int
	fmt.Fscan(reader, &n, &m)
	wishes := make([]int, n)
	for i := range wishes {
		fmt.Fscan(reader, &wishes[i])
	}
	fact := make([]int64, m+1)
	inv := make([]int64, m+1)
	fact[0] = 1
	for i := 1; i <= m; i++ {
		fact[i] = fact[i-1] * int64(i) % mod
	}
	inv[m] = power(fact[m], mod-2)
	for i := m; i > 0; i-- {
		inv[i-1] = inv[i] * int64(i) % mod
	}

	// ways[j]: the sponsors so far fill exactly j problems once; with t
	// mentions placed, (t - j) / 2 problems hold two sponsors and the rest none
	ways := make([]int64, m+1)
	ways[0] = 1
	placed := 0
	for _, s := range wishes {
		next := make([]int64, m+1)
		for j := placed % 2; j <= m; j += 2 {
			if ways[j] == 0 {
				continue
			}
			empty := m - j - (placed-j)/2
			// a of the new mentions go to problems with one sponsor, the
			// other s - a to empty problems
			base := ways[j] * fact[j] % mod * fact[empty] % mod
			from, to := s-empty, s
			if from < 0 {
				from = 0
			}
			if to > j {
				to = j
			}
			for a := from; a <= to; a++ {
				rest := s - a
				term := base * inv[a] % mod * inv[j-a] % mod
				term = term * inv[rest] % mod * inv[empty-rest] % mod
				target := j - a + rest
				next[target] = (next[target] + term) % mod
			}
		}
		ways = next
		placed += s
	}
	var answer int64
	for _, w := range ways {
		answer = (answer + w) % mod
	}
	fmt.Println(answer)
}
