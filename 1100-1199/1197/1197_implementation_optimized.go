package main

import (
	"bufio"
	"os"
)

func readInt(in *bufio.Reader) int {
	c, err := in.ReadByte()
	for c <= ' ' && err == nil {
		c, err = in.ReadByte()
	}
	value := 0
	for c >= '0' && c <= '9' {
		value = value*10 + int(c-'0')
		c, _ = in.ReadByte()
	}
	return value
}

const (
	side             = 8
	jumpCount        = 8
	inputBufferSize  = 256
	outputBufferSize = 128
)

var jumps = [jumpCount][2]int{
	{1, 2}, {2, 1}, {2, -1}, {1, -2}, {-1, -2}, {-2, -1}, {-2, 1}, {-1, 2},
}

func main() {
	in := bufio.NewReaderSize(os.Stdin, inputBufferSize)
	out := bufio.NewWriterSize(os.Stdout, outputBufferSize)
	n := readInt(in)
	for t := 0; t < n; t++ {
		var square [2]byte
		c, _ := in.ReadByte()
		for c <= ' ' {
			c, _ = in.ReadByte()
		}
		square[0] = c
		square[1], _ = in.ReadByte()
		col, row, count := int(square[0]-'a'), int(square[1]-'1'), 0
		// the knight attacks every square one jump away that is on the board
		for _, j := range jumps {
			c, r := col+j[0], row+j[1]
			if c >= 0 && c < side && r >= 0 && r < side {
				count++
			}
		}
		out.WriteByte(byte(count) + '0')
		out.WriteByte('\n')
	}
	out.Flush()
}
