package main

import (
	"bufio"
	"os"
	"strconv"
)

const (
	parityClasses = 4
	indexDigits   = 5
)

func number(input *bufio.Reader) int {
	c, err := input.ReadByte()
	for err == nil && (c <= ' ' || c == '-') {
		c, err = input.ReadByte()
	}
	value := 0
	for err == nil && c >= '0' && c <= '9' {
		value = value*10 + int(c-'0')
		c, err = input.ReadByte()
	}
	return value
}

func main() {
	input := bufio.NewReader(os.Stdin)
	count := number(input)
	indices := make([]uint16, parityClasses*count)
	var sizes [parityClasses]int
	for i := 1; ; i++ {
		x, y := number(input), number(input)
		// The parity of a coordinate equals the parity of its magnitude.
		group := (x&1)*2 + (y & 1)
		start := group * count
		indices[start+sizes[group]] = uint16(i)
		sizes[group]++
		if sizes[group] != count {
			continue
		}
		output := bufio.NewWriter(os.Stdout)
		output.WriteString("OK\n")
		var digits [indexDigits]byte
		for j, index := range indices[start : start+count] {
			if j != 0 {
				output.WriteByte(' ')
			}
			output.Write(strconv.AppendInt(digits[:0], int64(index), 10))
		}
		output.WriteByte('\n')
		output.Flush()
		return
	}
}
