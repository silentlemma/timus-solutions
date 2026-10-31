package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

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
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	x := make([]int64, n)
	y := make([]int64, n)
	for i := range x {
		fmt.Fscan(in, &x[i], &y[i])
	}
	// walking along the streets, a visit covers |dx| + |dy|
	pairs := int64(n) * int64(n-1) / 2
	fmt.Println((pairSum(x) + pairSum(y)) / pairs)
}
