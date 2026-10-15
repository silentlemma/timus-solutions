package main

import "fmt"

const (
	mod            = 1000000007
	edgeKinds      = 3
	middleKinds    = 4
	oneColourKinds = 2
)

var fact, inv []int64

func power(a, e int64) int64 {
	r := int64(1)
	for a %= mod; e > 0; e >>= 1 {
		if e&1 == 1 {
			r = r * a % mod
		}
		a = a * a % mod
	}
	return r
}

func choose(a, b int) int64 {
	if b < 0 || b > a {
		return 0
	}
	return fact[a] * inv[b] % mod * inv[a-b] % mod
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	var n, k int
	fmt.Scan(&n, &k)
	squares, row := n*n/2, n/2
	middle := squares - 2*row
	fact = make([]int64, squares+1)
	inv = make([]int64, squares+1)
	fact[0] = 1
	for i := 1; i <= squares; i++ {
		fact[i] = fact[i-1] * int64(i) % mod
	}
	inv[squares] = power(fact[squares], mod-2)
	for i := squares; i > 0; i-- {
		inv[i-1] = inv[i] * int64(i) % mod
	}
	// a dark square on the first or last row takes three kinds of piece
	// (the man that would be crowned there is out), any other square four
	var total int64
	for a := 0; a <= min(2*row, k); a++ {
		edge := choose(2*row, a) * power(edgeKinds, int64(a)) % mod
		rest := choose(middle, k-a) * power(middleKinds, int64(k-a)) % mod
		total = (total + edge*rest) % mod
	}
	// positions of one colour: on its last row only the king, elsewhere
	// the man or the king
	var one int64
	for a := 0; a <= min(row, k); a++ {
		rest := choose(middle+row, k-a) * power(oneColourKinds, int64(k-a)) % mod
		one = (one + choose(row, a)*rest) % mod
	}
	fmt.Println(((total-2*one)%mod + mod) % mod)
}
