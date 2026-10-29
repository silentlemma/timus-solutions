package main

import (
	"bufio"
	"os"
)

const (
	dwarfs     = 7
	bufferSize = 128
)

func main() {
	// the digits are read byte by byte from a 128-byte buffered reader
	// instead of reading the number as a string with fmt.Scan
	input := bufio.NewReaderSize(os.Stdin, bufferSize)
	// the number has up to 51 digits, so take it modulo 7 digit by digit
	rest := 0
	for {
		ch, err := input.ReadByte()
		if err != nil {
			break
		}
		if ch >= '0' && ch <= '9' {
			rest = (rest*10 + int(ch-'0')) % dwarfs
		}
	}
	os.Stdout.Write([]byte{byte(rest) + '0', '\n'})
}
