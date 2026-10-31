package main

import (
	"bufio"
	"fmt"
	"os"
)

// read bytes through a refillable buffer without allocating numeric tokens.
var input = bufio.NewReader(os.Stdin)

func nextInt() int {
	c, err := input.ReadByte()
	for err == nil && c <= ' ' {
		c, err = input.ReadByte()
	}
	sign := 1
	if c == '-' {
		sign = -1
		c, err = input.ReadByte()
	}
	value := 0
	for err == nil && c >= '0' && c <= '9' {
		value = value*10 + int(c-'0')
		c, err = input.ReadByte()
	}
	return value * sign
}

const target = 10000

func main() {
	n := nextInt()
	// statement values fit signed 16 bits; convert back to int for sums.
	up := make([]int16, n)
	for i := range up {
		up[i] = int16(nextInt())
	}
	m, at, found := nextInt(), 0, false
	for j := 0; j < m; j++ {
		value := nextInt()
		for at < n && int(up[at])+value < target {
			at++
		}
		if at < n && int(up[at])+value == target {
			found = true
		}
	}
	if found {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}
}
