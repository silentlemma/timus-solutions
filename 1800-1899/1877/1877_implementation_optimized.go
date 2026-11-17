package main

import (
	"bufio"
	"os"
)

const (
	inputBufferBytes = 64
)

func nextInt(reader *bufio.Reader) int {
	c, err := reader.ReadByte()
	for err == nil && c <= ' ' {
		c, err = reader.ReadByte()
	}
	sign := 1
	if c == '-' {
		sign = -1
		c, err = reader.ReadByte()
	}
	value := 0
	for err == nil && c >= '0' && c <= '9' {
		value = value*10 + int(c-'0')
		c, err = reader.ReadByte()
	}
	return value * sign
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, inputBufferBytes)
	first, second := nextInt(reader), nextInt(reader)
	answer := "no"
	if first%2 == 0 || second%2 == 1 {
		answer = "yes"
	}
	os.Stdout.WriteString(answer + "\n")
}
