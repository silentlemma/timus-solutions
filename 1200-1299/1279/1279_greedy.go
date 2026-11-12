package main

import "syscall"

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

const maxHeight = 1000
const maxDigits = 20

func main() {
	count := number() * number()
	budget := int64(number())
	var histogram [maxHeight + 1]int
	for i := 0; i < count; i++ {
		histogram[number()]++
	}
	active, level := int64(0), 1
	for level <= maxHeight {
		active += int64(histogram[level])
		// Only the currently lowest stacks need one container for the next level.
		if active == int64(count) {
			level += int(budget / active)
			break
		}
		if budget < active {
			break
		}
		budget -= active
		level++
	}
	var output [maxDigits]byte
	first := len(output) - 1
	output[first] = '\n'
	for level > 0 {
		first--
		output[first] = byte(level%10) + '0'
		level /= 10
	}
	writeAll(output[first:])
}
