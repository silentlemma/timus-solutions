package main

import "syscall"

const (
	inputSize  = 64
	outputSize = 32
	maxDigits  = 20
	base       = 3
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

func symbol() byte {
	c := nextByte()
	for c != 0 && c <= ' ' {
		c = nextByte()
	}
	return c
}

func number() int64 {
	c := symbol()
	value := int64(0)
	for c >= '0' && c <= '9' {
		value = value*10 + int64(c-'0')
		c = nextByte()
	}
	return value
}

func appendNumber(output []byte, value int64) []byte {
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
	return append(output, digits[first:]...)
}

func main() {
	amount := number()
	var payment, tip, firstUnused int64
	power := int64(1)
	for amount > 0 {
		digit := amount % base
		amount /= base
		switch digit {
		case 1:
			payment += power
		case base - 1:
			tip += power
			amount++
		default:
			if firstUnused == 0 {
				firstUnused = power
			}
		}
		power *= base
	}
	// With no negative digit, the first unused bill can go into both sums.
	if tip == 0 {
		if firstUnused == 0 {
			firstUnused = power
		}
		tip = firstUnused
		payment += firstUnused
	}
	var storage [outputSize]byte
	output := appendNumber(storage[:0], payment)
	output = appendNumber(append(output, ' '), tip)
	writeAll(append(output, '\n'))
}
