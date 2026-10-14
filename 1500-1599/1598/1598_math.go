package main

import (
	"fmt"
	"math"
	"math/bits"
)

func mulmod(a, b, m uint64) uint64 {
	hi, lo := bits.Mul64(a, b)
	return bits.Rem64(hi, lo, m)
}

func power(b, e, m uint64) uint64 {
	r := 1 % m
	for b %= m; e > 0; e >>= 1 {
		if e&1 == 1 {
			r = mulmod(r, b, m)
		}
		b = mulmod(b, b, m)
	}
	return r
}

// discreteLog finds the x in [0, q) with g^x = y modulo p, where g has
// order q: baby steps g^j for j < m, then giant steps y g^(-m i).
func discreteLog(g, y, p, q uint64) uint64 {
	m := uint64(math.Sqrt(float64(q))) + 1
	baby := make(map[uint64]uint64, 2*m)
	cur := uint64(1)
	for j := uint64(0); j < m; j++ {
		if _, ok := baby[cur]; !ok {
			baby[cur] = j
		}
		cur = mulmod(cur, g, p)
	}
	step := power(g, (q-m%q)%q, p) // g^(-m), since g^q = 1
	cur = y % p
	for i := uint64(0); i <= m; i++ {
		if j, ok := baby[cur]; ok {
			return (i*m + j) % q
		}
		cur = mulmod(cur, step, p)
	}
	return 0
}

func main() {
	var nBits, lBits, q, p, g, y, h uint64
	if _, err := fmt.Scan(&nBits, &lBits, &q, &p, &g, &y, &h); err != nil {
		return
	}
	// the hash is fixed, so the signature needs the secret key x itself
	x := discreteLog(g, y, p, q)
	for k := uint64(1); ; k++ {
		r := power(g, k, p) % q
		if r == 0 {
			continue
		}
		// q is prime, so k^(q-2) is the inverse of k
		s := mulmod(power(k, q-2, q), (h+mulmod(x, r, q))%q, q)
		if s != 0 {
			fmt.Println(r, s)
			return
		}
	}
}
