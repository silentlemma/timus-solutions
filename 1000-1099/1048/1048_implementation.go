package main

import (
	"bufio"
	"os"
)

const (
	base   = 10
	buffer = 1 << 16
)

func main() {
	in := bufio.NewReaderSize(os.Stdin, buffer)
	isDigit := func(c byte) bool { return c >= '0' && c <= '9' }
	// nextDigit skips spaces and line breaks
	nextDigit := func() int {
		c, err := in.ReadByte()
		for err == nil && !isDigit(c) {
			c, err = in.ReadByte()
		}
		return int(c - '0')
	}
	n := 0
	c, _ := in.ReadByte()
	for !isDigit(c) {
		c, _ = in.ReadByte()
	}
	for isDigit(c) {
		n = n*base + int(c-'0')
		c, _ = in.ReadByte()
	}
	// column sums from 0 to 18, then the carries from the last column up
	out := make([]byte, n+1)
	out[n] = '\n'
	for i := 0; i < n; i++ {
		a := nextDigit()
		out[i] = byte(a + nextDigit())
	}
	carry := 0
	for i := n - 1; i >= 0; i-- {
		t := int(out[i]) + carry
		carry = t / base
		out[i] = byte('0' + t%base)
	}
	os.Stdout.Write(out)
}
