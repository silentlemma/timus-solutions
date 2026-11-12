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

const inputSize = 32

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

const outputSize = 64

var output [outputSize]byte
var used int

func writeNumber(value int) {
	const maxDigits = 20
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

const forbiddenChoices int64 = 3

func count(n int64) (int64, int64) {
	if n%2 != 0 {
		size := (n - forbiddenChoices) / 2
		if size >= 2 {
			return n * size, 0
		}
		return 0, 0
	}
	half := n / 2
	first, second := half-1, half-2
	if first < 2 {
		first = 0
	}
	if second < 2 {
		second = 0
	}
	return half * (first + second), half * (n - forbiddenChoices)
}

func main() {
	parallel, perpendicular := count(int64(number()))
	writeNumber(int(parallel))
	output[used] = ' '
	used++
	writeNumber(int(perpendicular))
	output[used] = '\n'
	used++
	writeAll(output[:used])
}
