package main

import (
	"bufio"
	"os"
	"sort"
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

const cityBits = 17

func main() {
	in := bufio.NewReader(os.Stdin)
	n := next(in)
	// city <= 69999 needs 17 bits; count < 10^9 uses 30 more, within uint64.
	pairs := make([]uint64, n)
	for i := range pairs {
		pairs[i] = uint64(next(in))<<cityBits | uint64(i+1)
	}
	sort.Slice(pairs, func(i, j int) bool { return pairs[i] < pairs[j] })
	q := next(in)
	out := bufio.NewWriter(os.Stdout)
	for i := 0; i < q; i++ {
		lo, hi, x := next(in), next(in), next(in)
		base := uint64(x) << cityBits
		k := sort.Search(n, func(k int) bool { return pairs[k] >= base+uint64(lo) })
		if k < n && pairs[k] <= base+uint64(hi) {
			out.WriteByte('1')
		} else {
			out.WriteByte('0')
		}
	}
	out.WriteByte('\n')
	out.Flush()
}
