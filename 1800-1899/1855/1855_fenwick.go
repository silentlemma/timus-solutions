package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

// all sums are kept modulo 2^64: some of them overflow on the way, but the
// final total of a guild fits in a signed 64-bit number
func main() {
	in := bufio.NewScanner(os.Stdin)
	in.Split(bufio.ScanWords)
	word := func() string {
		in.Scan()
		return in.Text()
	}
	number := func() int {
		v, _ := strconv.Atoi(word())
		return v
	}
	n, m := number(), number()
	// sums of i and of i^2 for i up to x
	linear, square := make([]int64, n+2), make([]int64, n+2)
	for i := int64(1); i <= int64(n+1); i++ {
		linear[i] = linear[i-1] + i
		square[i] = square[i-1] + i*i
	}
	// toll t_i on segment i (cities i and i + 1) is the prefix sum of the
	// differences dif_j; the sum of i^k t_i over i <= x is
	// S_k(x) * (sum of dif_j) - (sum of dif_j * S_k(j - 1)) over j <= x
	size := n + 1
	plain, zero := make([]int64, size+1), make([]int64, size+1)
	one, two := make([]int64, size+1), make([]int64, size+1)
	add := func(j int, d int64) {
		w0, w1, w2 := d*int64(j-1), d*linear[j-1], d*square[j-1]
		for ; j <= size; j += j & -j {
			plain[j] += d
			zero[j] += w0
			one[j] += w1
			two[j] += w2
		}
	}
	prefix := func(x int) (int64, int64, int64) {
		// the sums of t_i, i t_i and i^2 t_i over i <= x
		var s, s0, s1, s2 int64
		for j := x; j > 0; j -= j & -j {
			s += plain[j]
			s0 += zero[j]
			s1 += one[j]
			s2 += two[j]
		}
		return int64(x)*s - s0, linear[x]*s - s1, square[x]*s - s2
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for e := 0; e < m; e++ {
		kind := word()
		a, b := number(), number()
		if kind == "change" {
			d := int64(number())
			add(a, d)
			add(b, -d)
			continue
		}
		h0, h1, h2 := prefix(b - 1)
		l0, l1, l2 := prefix(a - 1)
		// segment i lies on (i - a + 1)(b - i) of the guild's routes
		total := -(h2 - l2) + int64(a+b-1)*(h1-l1) + int64(b)*int64(1-a)*(h0-l0)
		routes := int64(b-a+1) * int64(b-a) / 2
		fmt.Fprintf(out, "%.8f\n", float64(total)/float64(routes))
	}
}
