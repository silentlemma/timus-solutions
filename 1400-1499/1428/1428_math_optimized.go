package main

import "syscall"

const bufferSize = 64
const maxDigits = 10 // The largest answer is 2^31.

var input [bufferSize]byte
var position, available int

func readByte() byte {
	for position == available {
		count, err := syscall.Read(syscall.Stdin, input[:])
		if count > 0 {
			position, available = 0, count
			break
		}
		if err != syscall.EINTR {
			return 0
		}
	}
	character := input[position]
	position++
	return character
}

func readNumber() uint {
	character := readByte()
	for character != 0 && (character < '0' || character > '9') {
		character = readByte()
	}
	var number uint
	for character >= '0' && character <= '9' {
		number = number*10 + uint(character-'0')
		character = readByte()
	}
	return number
}

func appendLine(output []byte, number uint64) []byte {
	var digits [maxDigits]byte
	start := len(digits)
	for {
		start--
		digits[start] = '0' + byte(number%10)
		number /= 10
		if number == 0 {
			break
		}
	}
	return append(append(output, digits[start:]...), '\n')
}

func main() {
	a, b, c := readNumber(), readNumber(), readNumber()
	// The input guarantees both exponents are integers.
	x := uint64(1) << ((c - 1) / a)
	y := uint64(1) << ((c - 1) / b)
	var buffer [bufferSize]byte
	output := appendLine(buffer[:0], x)
	output = appendLine(output, y)
	output = appendLine(output, 2)
	for len(output) > 0 {
		count, err := syscall.Write(syscall.Stdout, output)
		if count > 0 {
			output = output[count:]
		}
		if err == syscall.EINTR {
			continue
		}
		if count <= 0 || err != nil {
			break
		}
	}
}
