package main

import (
	"bufio"
	"fmt"
	"os"
)

func number(input *bufio.Reader) int {
	c, err := input.ReadByte()
	for err == nil && c <= ' ' {
		c, err = input.ReadByte()
	}
	negative := c == '-'
	if negative {
		c, err = input.ReadByte()
	}
	value := 0
	for err == nil && c >= '0' && c <= '9' {
		value = 10*value + int(c-'0')
		c, err = input.ReadByte()
	}
	if negative {
		return -value
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
	input := bufio.NewReader(os.Stdin)
	n, value := number(input), number(input)
	untouched, ending, used := value, -value, -value
	// Ending flips the last value. Used allows the flip to end anywhere.
	for i := 1; i < n; i++ {
		value = number(input)
		ending = min(-value, max(ending, untouched))
		used = max(ending, min(value, used))
		untouched = min(value, untouched)
	}
	fmt.Println(used)
}
