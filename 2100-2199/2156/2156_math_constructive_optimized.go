package main

import (
	"bufio"
	"os"
	"strconv"
)

const bufferSize = 1 << 15
const decimalInt64Bytes = 20

func number(input *bufio.Reader) int {
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

func writeGroup(output *bufio.Writer, falls []bool, group bool, count int) {
	var digits [decimalInt64Bytes]byte
	output.Write(strconv.AppendInt(digits[:0], int64(count), 10))
	output.WriteByte('\n')
	separator := false
	for edge, fall := range falls {
		if fall == group {
			if separator {
				output.WriteByte(' ')
			}
			output.Write(strconv.AppendInt(digits[:0], int64(edge+1), 10))
			separator = true
		}
	}
	output.WriteByte('\n')
}

func main() {
	input := bufio.NewReaderSize(os.Stdin, bufferSize)
	output := bufio.NewWriterSize(os.Stdout, bufferSize)
	defer output.Flush()
	n, first := number(input), number(input)
	previous := first
	falls := make([]bool, n)
	count := 0
	// Signed differences cancel around the circle. Keep one flag per edge.
	for edge := range falls {
		current := first
		if edge+1 < n {
			current = number(input)
		}
		if previous > current {
			falls[edge] = true
			count++
		}
		previous = current
	}
	if count == 0 {
		falls[0], count = true, 1
	}
	output.WriteString("YES\n")
	writeGroup(output, falls, true, count)
	writeGroup(output, falls, false, n-count)
}
