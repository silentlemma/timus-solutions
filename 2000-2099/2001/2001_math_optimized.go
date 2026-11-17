package main

import (
	"bufio"
	"os"
	"strconv"
)

const (
	inputBufferBytes  = 64
	outputBufferBytes = 32
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
	a1, b1 := nextInt(reader), nextInt(reader)
	nextInt(reader)
	b2, a3 := nextInt(reader), nextInt(reader)
	nextInt(reader)
	answer := a1 - a3
	output := make([]byte, 0, outputBufferBytes)
	output = strconv.AppendInt(output, int64(answer), 10)
	output = append(output, ' ')
	output = strconv.AppendInt(output, int64(b1-b2), 10)
	output = append(output, '\n')
	os.Stdout.Write(output)
}
