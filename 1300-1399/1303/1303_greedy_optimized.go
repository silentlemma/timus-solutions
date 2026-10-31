package main

import (
	"bufio"
	"fmt"
	"os"
)

// a buffered reader keeps input memory bounded while integers are parsed once.
func nextInt(in *bufio.Reader) int {
	c, err := in.ReadByte()
	for err == nil && c <= ' ' {
		c, err = in.ReadByte()
	}
	sign, value := 1, 0
	if c == '-' {
		sign = -1
		c, err = in.ReadByte()
	}
	for err == nil && c >= '0' && c <= '9' {
		value = value*10 + int(c-'0')
		c, err = in.ReadByte()
	}
	return sign * value
}

func main() {
	in := bufio.NewReader(os.Stdin)
	m := nextInt(in)
	left, right := make([]int, m), make([]int, m)
	// starts at or below zero share bucket zero; only the farthest end matters.
	// m <= 5000 bounds the bucket count, regardless of the number of intervals.
	for {
		l, r := nextInt(in), nextInt(in)
		if l == 0 && r == 0 {
			break
		}
		if l >= m || r <= 0 {
			continue
		}
		at := l
		if at < 0 {
			at = 0
		}
		if r > right[at] || (r == right[at] && l < left[at]) {
			left[at], right[at] = l, r
		}
	}
	chosen := make([]int, 0, m)
	covered, at := 0, 0
	for covered < m {
		// among the segments that start inside the covered part, take the
		// one that reaches furthest; it is never worse than any other
		best := -1
		for ; at < m && at <= covered; at++ {
			if best < 0 || right[at] > right[best] {
				best = at
			}
		}
		if best < 0 || right[best] <= covered {
			fmt.Println("No solution")
			return
		}
		chosen = append(chosen, best)
		covered = right[best]
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	fmt.Fprintln(out, len(chosen))
	for _, best := range chosen {
		fmt.Fprintln(out, left[best], right[best])
	}
}
