package main

import (
	"bufio"
	"fmt"
	"os"
)

// multiply returns the boolean product of two matrices kept as row bitmasks.
func multiply(x, y []uint64) []uint64 {
	out := make([]uint64, len(x))
	for i, row := range x {
		for j := range y {
			if row>>uint(j)&1 == 1 {
				out[i] |= y[j]
			}
		}
	}
	return out
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	// only whether an entry is zero matters: all entries are non-negative
	a := make([]uint64, n)
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			var v int
			fmt.Fscan(in, &v)
			if v != 0 {
				a[i] |= 1 << uint(j)
			}
		}
	}
	low, high := n*(n-1), n*(n+1)
	// A^low by repeated squaring
	cur, base := make([]uint64, n), a
	for i := range cur {
		cur[i] = 1 << uint(i)
	}
	for e := low; e > 0; e >>= 1 {
		if e&1 == 1 {
			cur = multiply(cur, base)
		}
		base = multiply(base, base)
	}
	seen := make([]uint64, n)
	for k := low; k <= high; k++ {
		for i := range seen {
			seen[i] |= cur[i]
		}
		cur = multiply(cur, a)
	}
	full := uint64(1)<<uint(n) - 1
	for _, s := range seen {
		if s != full {
			fmt.Println("No")
			return
		}
	}
	fmt.Println("Yes")
}
