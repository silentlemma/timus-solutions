package main

import (
	"sort"
	"syscall"
)

func readInput(buffer []byte) int {
	for {
		count, err := syscall.Read(syscall.Stdin, buffer)
		if count > 0 {
			return count
		}
		if err != syscall.EINTR {
			return 0
		}
	}
}

func writeAll(buffer []byte) {
	for len(buffer) > 0 {
		count, err := syscall.Write(syscall.Stdout, buffer)
		if count > 0 {
			buffer = buffer[count:]
		}
		if err == syscall.EINTR {
			continue
		}
		if count <= 0 {
			return
		}
	}
}

const inputSize = 256

var input [inputSize]byte
var position, length int

func nextByte() byte {
	if position == length {
		length = readInput(input[:])
		position = 0
		if length == 0 {
			return 0
		}
	}
	value := input[position]
	position++
	return value
}

func number() int {
	c := nextByte()
	for c != 0 && c <= ' ' {
		c = nextByte()
	}
	sign := 1
	if c == '-' {
		sign = -1
		c = nextByte()
	}
	value := 0
	for '0' <= c && c <= '9' {
		value = value*10 + int(c-'0')
		c = nextByte()
	}
	return sign * value
}

const outputSize = 2048
const maxDigits = 20

var output [outputSize]byte
var used int

func writeNumber(value int) {
	var digits [maxDigits]byte
	first := len(digits)
	for {
		first--
		digits[first] = '0' + byte(value%10)
		value /= 10
		if value == 0 {
			break
		}
	}
	used += copy(output[used:], digits[first:])
}

const maxSleepers = 100
const coordinateOffset = 1000
const coordinateBits = 11
const coordinateMask = (1 << coordinateBits) - 1

func main() {
	n := number()
	var sleepers, tails [maxSleepers]int
	for i := 0; i < n; i++ {
		left, right := number(), number()
		// Shifted coordinates 0..2000 each fit in eleven bits.
		sleepers[i] = (left+coordinateOffset)<<coordinateBits | (right + coordinateOffset)
	}
	sort.Ints(sleepers[:n])
	kept := 0
	for _, sleeper := range sleepers[:n] {
		right := (sleeper & coordinateMask) - coordinateOffset
		at := sort.Search(kept, func(i int) bool { return tails[i] >= right })
		tails[at] = right
		if at == kept {
			kept++
		}
	}
	writeNumber(n - kept)
	output[used] = '\n'
	used++
	writeAll(output[:used])
}
