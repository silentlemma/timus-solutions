package main

import (
	"bufio"
	"fmt"
	"os"
)

func max3(a, b, c int64) int64 {
	if b > a {
		a = b
	}
	if c > a {
		a = c
	}
	return a
}

func min3(a, b, c int64) int64 {
	if b < a {
		a = b
	}
	if c < a {
		a = c
	}
	return a
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var length int64
	var n int
	if _, err := fmt.Fscan(in, &length, &n); err != nil {
		return
	}
	s := make([]int64, n)
	for i := range s {
		fmt.Fscan(in, &s[i])
	}
	// a cut at x between supports s[i] and s[i + 1] leaves both parts
	// standing when the left centre x/2 lies in [s[0], s[i]] and the right
	// centre (x + length)/2 lies in [s[i + 1], s[n - 1]]
	loAll, hiAll := 2*s[0], 2*s[n-1]-length
	var safe int64
	for i := 0; i+1 < n; i++ {
		lo := max3(s[i], loAll, 2*s[i+1]-length)
		hi := min3(s[i+1], hiAll, 2*s[i])
		if hi > lo {
			safe += hi - lo
		}
	}
	fmt.Println(length - safe)
}
