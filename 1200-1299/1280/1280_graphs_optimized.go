package main

import (
	"bufio"
	"os"
)

// bufio refills its fixed buffer, so input is never retained in full.
func next(in *bufio.Reader) int {
	c, err := in.ReadByte()
	for err == nil && c <= ' ' {
		c, err = in.ReadByte()
	}
	value := 0
	for c >= '0' && c <= '9' && err == nil {
		value = value*10 + int(c-'0')
		c, err = in.ReadByte()
	}
	return value
}

func main() {
	in := bufio.NewReader(os.Stdin)
	n, m := next(in), next(in)
	// subject numbers are at most 1000, so uint16 stores every endpoint exactly.
	from, to := make([]uint16, m), make([]uint16, m)
	for i := 0; i < m; i++ {
		from[i], to[i] = uint16(next(in)), uint16(next(in))
	}
	place := make([]int, n+1)
	for i := 0; i < n; i++ {
		place[next(in)] = i
	}
	// the plan is right exactly when every rule points forward in it; a
	// rule from a subject to itself can never hold
	ok := true
	for i := 0; i < m; i++ {
		if place[from[i]] >= place[to[i]] {
			ok = false
		}
	}
	out := bufio.NewWriter(os.Stdout)
	if ok {
		out.WriteString("YES\n")
	} else {
		out.WriteString("NO\n")
	}
	out.Flush()
}
