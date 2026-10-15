package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

var in = bufio.NewReaderSize(os.Stdin, 1<<16)

func readInt() int64 {
	c, _ := in.ReadByte()
	for c < '0' {
		c, _ = in.ReadByte()
	}
	var v int64
	for c >= '0' {
		v = v*10 + int64(c-'0')
		c, _ = in.ReadByte()
	}
	return v
}

// the sum of |a_i - a_j| over all pairs: in sorted order the i-th value
// is larger than the i values before it
func pairSum(a []int64) int64 {
	sort.Slice(a, func(i, j int) bool { return a[i] < a[j] })
	var total, before int64
	for i, v := range a {
		total += v*int64(i) - before
		before += v
	}
	return total
}

func main() {
	n := readInt()
	x := make([]int64, n)
	y := make([]int64, n)
	for i := range x {
		x[i], y[i] = readInt(), readInt()
	}
	// walking along the streets, a visit covers |dx| + |dy|
	pairs := n * (n - 1) / 2
	fmt.Println((pairSum(x) + pairSum(y)) / pairs)
}
