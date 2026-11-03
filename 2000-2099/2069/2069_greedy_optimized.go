package main

import (
	"bufio"
	"fmt"
	"os"
)

var input = bufio.NewReader(os.Stdin)

func next() int {
	c, err := input.ReadByte()
	for err == nil && c <= ' ' {
		c, err = input.ReadByte()
	}
	value := 0
	for err == nil && c >= '0' && c <= '9' {
		value = value*10 + int(c-'0')
		c, err = input.ReadByte()
	}
	return value
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	n, m := next(), next()
	firstV := next()
	lastV, maxV := firstV, firstV
	for i := 1; i < n; i++ {
		lastV = next()
		maxV = max(maxV, lastV)
	}
	firstH := next()
	lastH, maxH := firstH, firstH
	for i := 1; i < m; i++ {
		lastH = next()
		maxH = max(maxH, lastH)
	}
	// Qualifying streets cross; only both directions and the endpoints matter.
	fmt.Println(min(min(maxV, maxH), min(max(firstV, firstH), max(lastV, lastH))))
}
