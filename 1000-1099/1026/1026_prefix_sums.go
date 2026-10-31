package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

// digits are parsed by hand instead of fmt.Fscan; the buffered reader refills,
// so no total input-size bound is needed.
var input = bufio.NewReader(os.Stdin)

func number() int {
	c, _ := input.ReadByte()
	for c < '0' || c > '9' {
		c, _ = input.ReadByte()
	}
	value := 0
	for c >= '0' && c <= '9' {
		value = value*10 + int(c-'0')
		next, err := input.ReadByte()
		if err != nil {
			break
		}
		c = next
	}
	return value
}

const maxValue = 5000

func main() {
	n := number()
	// the bounded value domain replaces the database with frequencies.
	counts := make([]int, maxValue+1)
	for i := 0; i < n; i++ {
		counts[number()]++
	}
	for i := 1; i <= maxValue; i++ {
		counts[i] += counts[i-1]
	}
	k := number()
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for i := 0; i < k; i++ {
		rank := number()
		fmt.Fprintln(out, sort.SearchInts(counts, rank))
	}
}
