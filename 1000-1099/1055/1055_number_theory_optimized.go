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

const maxNumber = 50000
const wordBits = 64
const sieveWords = (maxNumber/2 + wordBits) / wordBits
const firstOddPrime = 3

func exponent(value, prime int) int {
	count := 0
	for value > 0 {
		value /= prime
		count += value
	}
	return count
}

func main() {
	n, m := number(), number()
	var composite [sieveWords]uint64
	count := 0
	if exponent(n, 2) > exponent(m, 2)+exponent(n-m, 2) {
		count++
	}
	for prime := firstOddPrime; prime <= n; prime += 2 {
		index := prime / 2
		if composite[index/wordBits]&(uint64(1)<<uint(index%wordBits)) != 0 {
			continue
		}
		// Only odd multiples need flags; there are at most 25000 odd positions.
		for multiple := prime * prime; multiple <= n; multiple += 2 * prime {
			index := multiple / 2
			composite[index/wordBits] |= uint64(1) << uint(index%wordBits)
		}
		if exponent(n, prime) > exponent(m, prime)+exponent(n-m, prime) {
			count++
		}
	}
	writeNumber(count)
	output[used] = '\n'
	used++
	writeAll(output[:used])
}
