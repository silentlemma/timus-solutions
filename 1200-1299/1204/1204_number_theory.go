package main

import (
	"bufio"
	"fmt"
	"os"
)

const root = 31623

// inverse returns a^-1 modulo m by the extended Euclidean algorithm.
func inverse(a, m int64) int64 {
	r0, r1, s0, s1 := m, a%m, int64(0), int64(1)
	for r1 != 0 {
		t := r0 / r1
		r0, r1 = r1, r0-t*r1
		s0, s1 = s1, s0-t*s1
	}
	return (s0%m + m) % m
}

func main() {
	composite := make([]bool, root+1)
	var primes []int64
	for i := 2; i <= root; i++ {
		if !composite[i] {
			primes = append(primes, int64(i))
			for j := i * i; j <= root; j += i {
				composite[j] = true
			}
		}
	}
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var k int
	fmt.Fscan(in, &k)
	for ; k > 0; k-- {
		var n, p int64
		fmt.Fscan(in, &n)
		for _, d := range primes {
			if n%d == 0 {
				p = d
				break
			}
		}
		q := n / p
		// x = 1 (mod p) and x = 0 (mod q); the other root is n + 1 - x
		x := q * inverse(q, p) % n
		y := n + 1 - x
		if x > y {
			x, y = y, x
		}
		fmt.Fprintf(out, "0 1 %d %d\n", x, y)
	}
}
