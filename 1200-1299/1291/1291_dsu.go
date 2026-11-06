package main

import (
	"os"
	"strconv"
)

const (
	maxGears   = 1000
	bufferSize = 4096
	lineSize   = 16
	decimal    = 10
)

var input, output [bufferSize]byte
var cursor, available int
var links [maxGears + 1]int16
var teeth [maxGears + 1]uint16

func nextByte() byte {
	if cursor == available {
		available, _ = os.Stdin.Read(input[:])
		cursor = 0
		if available == 0 {
			return 0
		}
	}
	ch := input[cursor]
	cursor++
	return ch
}

func nextInt() int {
	ch := nextByte()
	for ch != 0 && ch <= ' ' {
		ch = nextByte()
	}
	value := 0
	for ch >= '0' && ch <= '9' {
		value = decimal*value + int(ch-'0')
		ch = nextByte()
	}
	return value
}

// A root stores the negative component size. Other entries store the
// parent in the high bits and the direction relative to it in the low bit.
func find(gear int16) (int16, int16) {
	link := links[gear]
	if link < 0 {
		return gear, 0
	}
	root, parity := find(link >> 1)
	parity ^= link & 1
	links[gear] = root<<1 | parity
	return root, parity
}

func join(left, right int16) {
	a, aParity := find(left)
	b, bParity := find(right)
	if a == b {
		return
	}
	if links[a] > links[b] {
		a, b = b, a
	}
	links[a] += links[b]
	links[b] = a<<1 | (aParity ^ bParity ^ 1)
}

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func main() {
	size := int16(nextInt())
	for gear := int16(1); gear <= size; gear++ {
		links[gear] = -1
	}
	for gear := int16(1); gear <= size; gear++ {
		teeth[gear] = uint16(nextInt())
		for other := int16(nextInt()); other != 0; other = int16(nextInt()) {
			join(gear, other)
		}
	}
	driven, speed := int16(nextInt()), nextInt()
	drivenRoot, drivenParity := find(driven)
	rim := speed * int(teeth[driven])
	buffer := output[:0]
	for gear := int16(1); gear <= size; gear++ {
		if len(buffer)+lineSize > len(output) {
			os.Stdout.Write(buffer)
			buffer = output[:0]
		}
		root, parity := find(gear)
		if root != drivenRoot {
			buffer = append(buffer, "0/1\n"...)
			continue
		}
		divisor := gcd(rim, int(teeth[gear]))
		numerator := rim / divisor
		if parity != drivenParity {
			numerator = -numerator
		}
		buffer = strconv.AppendInt(buffer, int64(numerator), decimal)
		buffer = append(buffer, '/')
		buffer = strconv.AppendInt(buffer, int64(int(teeth[gear])/divisor), decimal)
		buffer = append(buffer, '\n')
	}
	os.Stdout.Write(buffer)
}
