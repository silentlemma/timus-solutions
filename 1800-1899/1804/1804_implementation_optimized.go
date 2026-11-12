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

const most = 30
const wordsBeforeVenue = 3

func main() {
	tests := number()
	for test := 0; test < tests; test++ {
		for i := 0; i < wordsBeforeVenue; i++ {
			word()
		}
		home := word() == 'h'
		word()
		word()
		x := number()
		word()
		word()
		word()
		y := number()
		word()
		lowest, highest := -1, -1
		for goals := 0; goals <= most; goals++ {
			away, bestAway, worstAway := x, 0, most
			if home {
				away, bestAway, worstAway = goals, y, y
			}
			total := x + goals
			// Only the extreme opposing scores are needed.
			if lowest < 0 && (total > y || total == y && away >= bestAway) {
				lowest = goals
			}
			if total < y+most || total == y+most && away <= worstAway {
				highest = goals
			}
		}
		writeNumber(lowest)
		output[used] = ' '
		used++
		writeNumber(highest)
		output[used] = '\n'
		used++
	}
	writeAll(output[:used])
}
