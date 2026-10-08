package main

import (
	"fmt"
	"math/bits"
)

type matrix [2][2]uint64

// mulMod: a*b mod m without overflow; a, b < m, so the high word is below m.
func mulMod(a, b, m uint64) uint64 {
	hi, lo := bits.Mul64(a, b)
	_, r := bits.Div64(hi, lo, m)
	return r
}

func addMod(a, b, m uint64) uint64 {
	s, carry := bits.Add64(a, b, 0)
	if carry != 0 || s >= m {
		s -= m
	}
	return s
}

func multiply(x, y matrix, m uint64) matrix {
	var r matrix
	for i := 0; i < 2; i++ {
		for j := 0; j < 2; j++ {
			r[i][j] = addMod(mulMod(x[i][0], y[0][j], m), mulMod(x[i][1], y[1][j], m), m)
		}
	}
	return r
}

func main() {
	var n, k, m uint64
	fmt.Scan(&n, &k, &m)
	d := (k - 1) % m
	// (zero, other) -> (other, (zero + other)(K - 1)) is the matrix step,
	// after the first digit the pair is (0, K - 1)
	step := matrix{{0, 1 % m}, {d, d}}
	power := matrix{{1 % m, 0}, {0, 1 % m}}
	for e := n - 1; e > 0; e >>= 1 {
		if e&1 == 1 {
			power = multiply(power, step, m)
		}
		step = multiply(step, step, m)
	}
	zero, other := mulMod(power[0][1], d, m), mulMod(power[1][1], d, m)
	fmt.Println(addMod(zero, other, m))
}
