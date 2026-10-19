package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	squareFactor   int64 = 3
	constantFactor int64 = 12
	searchLimit    int64 = 2000000000
)

func solve(a, b, c int64) int64 {
	scaled := squareFactor*b*b/a - constantFactor*c
	if scaled < 0 {
		return 1
	}
	threshold := scaled/a + 1
	low, high := int64(1), searchLimit
	for low < high {
		middle := low + (high-low)/2
		if middle*middle > threshold {
			high = middle
		} else {
			low = middle + 1
		}
	}
	return low
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var cases int
	fmt.Fscan(in, &cases)
	for ; cases > 0; cases-- {
		var a, b, c int64
		fmt.Fscan(in, &a, &b, &c)
		fmt.Fprintln(out, solve(a, b, c))
	}
}
