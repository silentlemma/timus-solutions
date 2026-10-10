package main

import (
	"fmt"
	"math/big"
)

const islands = 3

type plane [][][islands]*big.Int

func newPlane(n int) plane {
	p := make(plane, n+1)
	for b := range p {
		p[b] = make([][islands]*big.Int, n+1)
		for c := range p[b] {
			for i := range p[b][c] {
				p[b][c][i] = new(big.Int)
			}
		}
	}
	return p
}

func main() {
	var n int
	fmt.Scan(&n)
	// plane[b][c][i]: sequences of islands that start on the tourist's island
	// 0, use a, b and c cities of the islands (a fixed per plane), never
	// repeat an island twice in a row and end on island i
	var prev plane
	for a := 1; a <= n; a++ {
		cur := newPlane(n)
		for b := 0; b <= n; b++ {
			for c := 0; c <= n; c++ {
				cell := &cur[b][c]
				if a == 1 && b == 0 && c == 0 {
					cell[0].SetInt64(1)
				}
				if a > 1 {
					cell[0].Add(prev[b][c][1], prev[b][c][2])
				}
				if b > 0 {
					cell[1].Add(cur[b-1][c][0], cur[b-1][c][2])
				}
				if c > 0 {
					cell[2].Add(cur[b][c-1][0], cur[b][c-1][1])
				}
			}
		}
		prev = cur
	}
	// the trip closes back on island 0, so it must not end there
	total := new(big.Int).Add(prev[n][n][1], prev[n][n][2])
	// cities fill the island slots in any order, except the fixed start, and
	// every trip is counted once in each direction; (n-1)! n!^2 is the
	// product of k^2 (k-1) over k from 2 to n
	for k := int64(2); k <= int64(n); k++ {
		total.Mul(total, big.NewInt(k*k*(k-1)))
	}
	total.Rsh(total, 1)
	fmt.Println(total.String())
}
