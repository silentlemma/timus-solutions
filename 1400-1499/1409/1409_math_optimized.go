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

// the two numbers are parsed by hand from a 64-byte buffered reader and the
// answer is appended to a byte slice, without fmt
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
	harry, larry := nextInt(reader), nextInt(reader)
	// the last can was shot by both, so each missed the other's count minus one
	answer := larry - 1
	output := make([]byte, 0, outputBufferBytes)
	output = strconv.AppendInt(output, int64(answer), 10)
	output = append(output, ' ')
	output = strconv.AppendInt(output, int64(harry-1), 10)
	output = append(output, '\n')
	os.Stdout.Write(output)
}
