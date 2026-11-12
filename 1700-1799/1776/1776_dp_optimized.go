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

const maxRockets = 400
const maxInner = maxRockets - 2
const seconds = 10
const decimalScale int64 = 1000000000

var first, second [maxInner + 1]float64

const rounding = 0.5

func main() {
	m := number() - 2
	previous, current := &first, &second
	previous[0], current[0] = 1, 1
	volleys := 0.0
	for round := 1; round <= m; round++ {
		volleys += 1 - previous[m]
		for size := 1; size <= m; size++ {
			if size <= round {
				current[size] = 1
				continue
			}
			sum := 0.0
			for left := 0; left < size/2; left++ {
				sum += 2 * previous[left] * previous[size-1-left]
			}
			if size%2 != 0 {
				middle := previous[size/2]
				sum += middle * middle
			}
			current[size] = sum / float64(size)
		}
		previous, current = current, previous
	}
	scaled := int64(volleys*seconds*float64(decimalScale) + rounding)
	writeNumber(int(scaled / decimalScale))
	output[used] = '.'
	used++
	for power := decimalScale / 10; power != 0; power /= 10 {
		output[used] = '0' + byte(scaled/power%10)
		used++
	}
	output[used] = '\n'
	used++
	writeAll(output[:used])
}
