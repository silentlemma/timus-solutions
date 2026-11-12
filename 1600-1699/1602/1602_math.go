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

const inputSize = 128

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

const hundred int64 = 100
const stand = 15 * hundred
const board = 5 * hundred

func hundredths() int64 {
	c := nextByte()
	for c != 0 && c <= ' ' {
		c = nextByte()
	}
	var value int64
	for c >= '0' && c <= '9' {
		value = value*10 + int64(c-'0')
		c = nextByte()
	}
	value *= hundred
	if c == '.' {
		for scale := hundred / 10; scale > 0; scale /= 10 {
			c = nextByte()
			if c < '0' || c > '9' {
				break
			}
			value += int64(c-'0') * scale
		}
	}
	return value
}

func main() {
	n, k := int64(number()), int64(number())
	u, v := hundredths(), hundredths()
	ready := (k-1)*v + stand
	bestFloor, bestTime := int64(1), (n-1)*u
	upper := n - ready/u
	for _, floor := range [...]int64{2, n, upper - 1, upper} {
		if floor < 2 {
			floor = 2
		}
		if floor > n {
			floor = n
		}
		start := (n - floor) * u
		if ready > start {
			start = ready
		}
		total := start + 2*(floor-1)*v + board
		if total < bestTime || total == bestTime && floor > bestFloor {
			bestTime, bestFloor = total, floor
		}
	}
	writeNumber(int(bestFloor))
	output[used] = '\n'
	used++
	writeAll(output[:used])
}
