package main

import (
	"fmt"
	"strings"
)

func main() {
	var n int
	var k int64
	fmt.Scan(&n, &k)
	// count[r]: strings of length r without two adjacent ones (Fibonacci)
	count := []int64{1, 2}
	for len(count) <= n {
		count = append(count, count[len(count)-1]+count[len(count)-2])
	}
	if k > count[n] {
		fmt.Println(-1)
		return
	}
	var out strings.Builder
	last := byte('0')
	for pos := 0; pos < n; pos++ {
		rest := n - pos - 1
		// strings with 0 here come first; a 1 is only possible after a 0
		if last == '1' || k <= count[rest] {
			last = '0'
		} else {
			k -= count[rest]
			last = '1'
		}
		out.WriteByte(last)
	}
	fmt.Println(out.String())
}
