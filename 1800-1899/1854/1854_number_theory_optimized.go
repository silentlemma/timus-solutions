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

const firstOddDivisor = 3
const maxSquareRoot = 1000000000

func squareRoot(value int64) int64 {
	low, high := int64(0), int64(maxSquareRoot+1)
	for high-low > 1 {
		middle := (low + high) / 2
		if middle*middle <= value {
			low = middle
		} else {
			high = middle
		}
	}
	return low
}

func squarePart(value int64) int64 {
	root := squareRoot(value)
	if root*root == value {
		return value
	}
	answer := int64(1)
	for divisor := int64(firstOddDivisor); divisor*divisor*divisor <= value; divisor += 2 {
		power := 0
		for value%divisor == 0 {
			value /= divisor
			power++
		}
		for pair := 0; pair < power/2; pair++ {
			answer *= divisor * divisor
		}
		if power > 0 {
			root = squareRoot(value)
			// A square residual is itself its largest square divisor.
			if root*root == value {
				return answer * value
			}
		}
	}
	root = squareRoot(value)
	if root*root == value {
		answer *= value
	}
	return answer
}

func main() {
	writeNumber(int(squarePart(int64(number()))))
	output[used] = '\n'
	used++
	writeAll(output[:used])
}
