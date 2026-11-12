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

func word() byte {
	c := nextByte()
	for c != 0 && c <= ' ' {
		c = nextByte()
	}
	first := c
	for c > ' ' {
		c = nextByte()
	}
	return first
}

const outputSize = 4096

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

const maxDestroyed = 10000
const maxNumberBytes = 11

func main() {
	number()
	events := number()
	gone := make([]int, 0, maxDestroyed)
	for event := 0; event < events; event++ {
		command, room := word(), number()
		low, high := 0, len(gone)
		for low < high {
			middle := (low + high) / 2
			if gone[middle]-middle <= room {
				low = middle + 1
			} else {
				high = middle
			}
		}
		original := room + low
		if command == 'D' {
			gone = append(gone, 0)
			copy(gone[low+1:], gone[low:len(gone)-1])
			gone[low] = original
		} else {
			// At most ten digits and a newline; flush before a record can cross the bound.
			if used+maxNumberBytes > len(output) {
				writeAll(output[:used])
				used = 0
			}
			writeNumber(original)
			output[used] = '\n'
			used++
		}
	}
	writeAll(output[:used])
}
