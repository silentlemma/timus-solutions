package main

import (
	"bufio"
	"os"
	"strconv"
)

const bufferSize = 4096
const outputLength = 32

func nextInt(input *bufio.Reader) int64 {
	ch, err := input.ReadByte()
	for err == nil && ch <= ' ' {
		ch, err = input.ReadByte()
	}
	if err != nil {
		return -1
	}
	value := int64(0)
	for ch >= '0' && ch <= '9' {
		value = value*10 + int64(ch-'0')
		ch, err = input.ReadByte()
		if err != nil {
			break
		}
	}
	return value
}

func main() {
	input := bufio.NewReaderSize(os.Stdin, bufferSize)
	output := bufio.NewWriterSize(os.Stdout, bufferSize)
	defer output.Flush()
	var text [outputLength]byte
	for {
		n := nextInt(input)
		if n < 0 {
			return
		}
		p := nextInt(input)
		if n == 0 && p == 0 {
			return
		}
		result := int64(1)
		if n >= p {
			result = 0
		}
		i := int64(2)
		// Pairing factors halves modulo operations; every product is below2e17.
		for ; i+1 <= n && result != 0; i += 2 {
			result = result * i * (i + 1) % p
		}
		if i <= n && result != 0 {
			result = result * i % p
		}
		row := strconv.AppendInt(text[:0], result, 10)
		row = append(row, '\n')
		output.Write(row)
	}
}
