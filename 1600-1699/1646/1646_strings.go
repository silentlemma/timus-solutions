package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

const mod = 1000000007

type sample struct {
	count      int64  // occurrences mod 1e9 + 7; the string can be 2^100 long
	head, tail string // its first and last letters
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var pattern, first, second string
	var m int
	if _, err := fmt.Fscan(in, &pattern, &first, &second, &m); err != nil {
		return
	}
	edge := len(pattern) - 1 // letters kept at each end of a sample
	occurrences := func(text string) int64 {
		var found int64
		for i := 0; i+len(pattern) <= len(text); i++ {
			if strings.HasPrefix(text[i:], pattern) {
				found++
			}
		}
		return found
	}
	head := func(s string) string {
		if len(s) > edge {
			return s[:edge]
		}
		return s
	}
	tail := func(s string) string {
		if len(s) > edge {
			return s[len(s)-edge:]
		}
		return s
	}
	samples := []sample{
		{occurrences(first), head(first), tail(first)},
		{occurrences(second), head(second), tail(second)},
	}
	for k := 0; k < m; k++ {
		var i, j int
		fmt.Fscan(in, &i, &j)
		a, b := samples[i-1], samples[j-1]
		// every new occurrence crosses the seam, so it lies in these letters
		seam := occurrences(a.tail + b.head)
		count := (a.count + b.count + seam) % mod
		samples = append(samples, sample{count, head(a.head + b.head), tail(a.tail + b.tail)})
	}
	fmt.Println(samples[len(samples)-1].count)
}
