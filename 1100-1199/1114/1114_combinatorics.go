package main

import "fmt"

const top = 40

func main() {
	var n, a, b int
	fmt.Scan(&n, &a, &b)
	// Pascal's triangle; the binomials stay below 2^32
	var c [top][top]uint64
	for i := 0; i < top; i++ {
		c[i][0] = 1
		for j := 1; j <= i; j++ {
			c[i][j] = c[i-1][j-1] + c[i-1][j]
		}
	}
	// up to a identical balls in n boxes: put the unused ones in an extra box,
	// then it is a stars-and-bars count C(a + n, n); the colours are
	// independent, and the product reaches 1.05 * 10^19, past signed 64 bits
	fmt.Println(c[a+n][n] * c[b+n][n])
}
