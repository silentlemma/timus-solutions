package main

import (
	"os"
	"strconv"
)

const maxRecruits = 10000
const bufferSize = 4096
const outputSize = 3 // Two row digits and a newline.

var input [bufferSize]byte
var position, available int
var counts [maxRecruits + 1]uint16

func nextByte() byte {
	if position == available {
		available, _ = os.Stdin.Read(input[:])
		position = 0
		if available == 0 {
			return 0
		}
	}
	value := input[position]
	position++
	return value
}

func nextInt() int {
	ch := nextByte()
	for ch != 0 && ch <= ' ' {
		ch = nextByte()
	}
	value := 0
	for ch >= '0' && ch <= '9' {
		value = value*10 + int(ch-'0')
		ch = nextByte()
	}
	return value
}

func main() {
	size, rows := nextInt(), nextInt()
	best, answer := -1, 1
	for row := 1; row <= rows; row++ {
		for i := 1; i <= size; i++ {
			counts[i] = 0
		}
		jumps := 0
		for seen := 0; seen < size; seen++ {
			height := nextInt()
			jumps += seen
			for prefix := height - 1; prefix != 0; prefix &= prefix - 1 {
				jumps -= int(counts[prefix])
			}
			for at := height; at <= size; at += at & -at {
				counts[at]++
			}
		}
		if jumps > best {
			best, answer = jumps, row
		}
	}
	var output [outputSize]byte
	line := strconv.AppendInt(output[:0], int64(answer), 10)
	os.Stdout.Write(append(line, '\n'))
}
