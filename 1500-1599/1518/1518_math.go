package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	n     int
	y     uint64
	steps []int // the j with C[n + 1 - j] = 1
)

// times returns p * q modulo the characteristic polynomial and y.
func times(p, q []uint64) []uint64 {
	prod := make([]uint64, 2*n-1)
	for i := 0; i < n; i++ {
		if p[i] == 0 {
			continue
		}
		for j := 0; j < n; j++ {
			prod[i+j] = (prod[i+j] + p[i]*q[j]) % y
		}
	}
	// x^n is the sum of x^(n - j) over the steps
	for d := 2*n - 2; d >= n; d-- {
		if prod[d] == 0 {
			continue
		}
		for _, j := range steps {
			prod[d-j] = (prod[d-j] + prod[d]) % y
		}
	}
	return prod[:n]
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var x int64
	fmt.Fscan(in, &n, &x, &y)
	keys := make([]uint64, n)
	shifts := make([]int, n)
	for i := range keys {
		fmt.Fscan(in, &keys[i])
	}
	for i := range shifts {
		fmt.Fscan(in, &shifts[i])
	}
	// K[i] = sum of K[i - j] * C[n + 1 - j] over j = 1 ... n
	for j := 1; j <= n; j++ {
		if shifts[n-j] == 1 {
			steps = append(steps, j)
		}
	}
	// K[x] is the x - 1 st term counting from K[1], and the coefficients of
	// x^(x - 1) reduced modulo the characteristic polynomial weigh K[1 ... n]
	result, base := make([]uint64, n), make([]uint64, n)
	result[0] = 1
	if n > 1 {
		base[1] = 1
	} else {
		base[0] = uint64(shifts[0]) % y
	}
	for e := x - 1; e > 0; e >>= 1 {
		if e&1 == 1 {
			result = times(result, base)
		}
		base = times(base, base)
	}
	answer := uint64(0)
	for i := 0; i < n; i++ {
		answer = (answer + result[i]*(keys[i]%y)) % y
	}
	fmt.Println(answer)
}
