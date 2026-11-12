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

const inputSize = 8192

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

func absolute(value int) int {
	if value < 0 {
		return -value
	}
	return value
}

func main() {
	count := number()
	y, vertical := 1, 0
	low, high, right := 0, 0, 0
	for i := 0; i < count; i++ {
		number()
		bottom, end, top := number(), number(), number()
		if i > 0 {
			first, last := low+1, high-1
			if bottom > low {
				first = bottom + 1
			}
			if top < high {
				last = top - 1
			}
			if first > last {
				writeAll([]byte("-1\n"))
				return
			}
			// Project onto the crossing interval; rectangles themselves are never stored.
			target := y
			if target < first {
				target = first
			}
			if target > last {
				target = last
			}
			vertical += absolute(target - y)
			y = target
		}
		low, high, right = bottom, top, end
	}
	writeNumber(right - 2 + vertical + absolute(high-1-y))
	output[used] = '\n'
	used++
	writeAll(output[:used])
}
