package main

import (
	"bufio"
	"os"
	"strconv"
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
	n, k, m := next(in), next(in), next(in)
	// island numbers are at most 10000 and fit uint16 exactly.
	parent := make([]uint16, n+1)
	for i := range parent {
		parent[i] = uint16(i)
	}
	find := func(v uint16) uint16 {
		for parent[v] != v {
			parent[v] = parent[parent[v]]
			v = parent[v]
		}
		return v
	}
	// tunnels are free; every bridge joins two of the remaining groups
	groups := n
	for i := 0; i < k; i++ {
		a, b := find(uint16(next(in))), find(uint16(next(in)))
		if a != b {
			parent[a] = b
			groups--
		}
	}
	// bridges do not change tunnel components; still consume every pair.
	for i := 0; i < m; i++ {
		next(in)
		next(in)
	}
	out := bufio.NewWriter(os.Stdout)
	out.WriteString(strconv.Itoa(groups-1) + "\n")
	out.Flush()
}
