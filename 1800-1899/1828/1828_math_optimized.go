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

const stepScale int64 = 12
const centerScale int64 = 6
const firstScale int64 = 4
const decimalScale int64 = 1000000000
const decimalDigits = 9

func appendFraction(numerator, denominator int64) {
	if numerator < 0 {
		output[used] = '-'
		used++
		numerator = -numerator
	}
	whole, remainder, fraction := numerator/denominator, numerator%denominator, int64(0)
	for i := 0; i < decimalDigits; i++ {
		remainder *= 10
		fraction = fraction*10 + remainder/denominator
		remainder %= denominator
	}
	if 2*remainder >= denominator {
		fraction++
		if fraction == decimalScale {
			fraction = 0
			whole++
		}
	}
	writeNumber(int(whole))
	output[used] = '.'
	used++
	for power := decimalScale / 10; power != 0; power /= 10 {
		output[used] = '0' + byte(fraction/power%10)
		used++
	}
}

func main() {
	n := int64(number())
	var sum, weighted int64
	for i := int64(0); i < n; i++ {
		value := int64(number())
		sum += value
		weighted += i * value
	}
	appendFraction((firstScale*n-2)*sum-centerScale*weighted, n*(n+1))
	output[used] = ' '
	used++
	appendFraction(stepScale*weighted-centerScale*(n-1)*sum, n*(n*n-1))
	output[used] = '\n'
	used++
	writeAll(output[:used])
}
