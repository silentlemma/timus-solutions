package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	size = 4
	base = 10
)

type matrix [size][size]int64

func multiply(a, b matrix, m int64) matrix {
	var c matrix
	for i := 0; i < size; i++ {
		for k := 0; k < size; k++ {
			for j := 0; j < size; j++ {
				c[i][j] = (c[i][j] + a[i][k]*b[k][j]) % m
			}
		}
	}
	return c
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var digits string
	var k, m int64
	fmt.Fscan(in, &digits, &k, &m)
	// going left to right, E is the sum of the substrings ending at the
	// current digit: E' = 10 E + digit * (its position), and S adds up E,
	// so one copy of p acts linearly on (S, E, J, 1), J digits before it
	power, value, weighted := 1%m, int64(0), int64(0)
	var sumPower, sumValue, sumWeighted int64
	for i := 0; i < len(digits); i++ {
		d := int64(digits[i] - '0')
		power = power * base % m
		value = (value*base + d) % m
		weighted = (weighted*base + d*int64(i+1)) % m
		sumPower = (sumPower + power) % m
		sumValue = (sumValue + value) % m
		sumWeighted = (sumWeighted + weighted) % m
	}
	block := matrix{
		{1 % m, sumPower, sumValue, sumWeighted},
		{0, power, value, weighted},
		{0, 0, 1 % m, int64(len(digits)) % m},
		{0, 0, 0, 1 % m},
	}
	var result matrix
	for i := 0; i < size; i++ {
		result[i][i] = 1 % m
	}
	for ; k > 0; k >>= 1 {
		if k&1 == 1 {
			result = multiply(result, block, m)
		}
		block = multiply(block, block, m)
	}
	// starting from S = E = J = 0, the total is the constant column of S
	fmt.Println(result[0][size-1])
}
