package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, s int64
	var k int
	fmt.Fscan(in, &n, &s, &k)
	moves := make([]int64, k)
	for i := range moves {
		fmt.Fscan(in, &moves[i])
	}
	half := k / 2
	// the depths the first half of the moves can reach without leaving
	// [0, n]; equal depths are kept once
	start := []int64{s}
	for _, d := range moves[:half] {
		var next []int64
		for _, p := range start {
			if p+d <= n {
				next = append(next, p+d)
			}
			if p-d >= 0 {
				next = append(next, p-d)
			}
		}
		sort.Slice(next, func(i, j int) bool { return next[i] < next[j] })
		var unique []int64
		for i, p := range next {
			if i == 0 || p != next[i-1] {
				unique = append(unique, p)
			}
		}
		start = unique
	}
	rest := moves[half:]
	shallowest, deepest := n+1, int64(-1)
	// a signing of the second half with this total and these lowest and
	// highest running sums fits after depth x exactly when
	// -low <= x <= n - high, and it ends at x + total
	var walk func(i int, total, low, high int64)
	walk = func(i int, total, low, high int64) {
		if i == len(rest) {
			j := sort.Search(len(start), func(t int) bool { return start[t] >= -low })
			if j == len(start) || start[j] > n-high {
				return
			}
			if start[j]+total < shallowest {
				shallowest = start[j] + total
			}
			last := sort.Search(len(start), func(t int) bool { return start[t] > n-high }) - 1
			if start[last]+total > deepest {
				deepest = start[last] + total
			}
			return
		}
		for _, u := range [2]int64{total + rest[i], total - rest[i]} {
			a, b := low, high
			if u < a {
				a = u
			}
			if u > b {
				b = u
			}
			if b-a <= n {
				walk(i+1, u, a, b)
			}
		}
	}
	walk(0, 0, 0, 0)
	fmt.Println(shallowest, deepest)
}
