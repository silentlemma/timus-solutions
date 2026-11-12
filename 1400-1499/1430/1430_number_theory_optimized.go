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

func gcd(a, b int64) int64 {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func main() {
	a, b, n := int64(number()), int64(number()), int64(number())
	swapped := a < b
	if swapped {
		a, b = b, a
	}
	divisor := gcd(a, b)
	limit := n / a
	if b/divisor-1 < limit {
		limit = b/divisor - 1
	}
	step, remainder := a%b, n%b
	best, bx, lower := remainder, int64(0), n%divisor
	for x := int64(1); x <= limit && best > lower; x++ {
		if remainder >= step {
			remainder -= step
		} else {
			remainder += b - step
		}
		if remainder < best {
			best, bx = remainder, x
		}
	}
	by := (n - bx*a) / b
	if swapped {
		bx, by = by, bx
	}
	writeNumber(int(bx))
	output[used] = ' '
	used++
	writeNumber(int(by))
	output[used] = '\n'
	used++
	writeAll(output[:used])
}
