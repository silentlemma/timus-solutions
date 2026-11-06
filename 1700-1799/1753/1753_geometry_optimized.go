package main

import (
	"math"
	"syscall"
)

const (
	inputSize  = 64
	outputSize = 32
	maxDigits  = 20
	scale      = uint64(1000000)
)

var input [inputSize]byte
var inputPosition, inputLength int

// Use standard handles directly; retry interrupts and finish short writes.
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

func nextByte() byte {
	if inputPosition == inputLength {
		inputLength = readInput(input[:])
		inputPosition = 0
		if inputLength == 0 {
			return 0
		}
	}
	value := input[inputPosition]
	inputPosition++
	return value
}

func number() int {
	c := nextByte()
	for c != 0 && c <= ' ' {
		c = nextByte()
	}
	value := 0
	for c >= '0' && c <= '9' {
		value = value*10 + int(c-'0')
		c = nextByte()
	}
	return value
}

func appendNumber(output []byte, value uint64) []byte {
	var digits [maxDigits]byte
	position := len(digits)
	for {
		position--
		digits[position] = '0' + byte(value%10)
		value /= 10
		if value == 0 {
			break
		}
	}
	return append(output, digits[position:]...)
}

func main() {
	rim, book := number(), number()
	shift := 0.0
	if book > 2*rim {
		ratio := math.Cbrt(float64(book) / float64(2*rim))
		factor := (ratio - 1) * (ratio + 1)
		shift = float64(rim) * factor * math.Sqrt(factor)
	}
	value := uint64(math.Round(shift * float64(scale)))
	var storage [outputSize]byte
	output := appendNumber(storage[:0], value/scale)
	output = append(output, '.')
	for place := scale / 10; place > 0; place /= 10 {
		output = append(output, '0'+byte(value/place%10))
	}
	writeAll(append(output, '\n'))
}
