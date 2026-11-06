package main

import "syscall"

const (
	inputSize       = 16
	outputSize      = 16
	firstOddDivisor = 3
)

var (
	input         [inputSize]byte
	inputPosition int
	inputLength   int
	output        [outputSize]byte
)

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

func main() {
	c := nextByte()
	for c != 0 && c <= ' ' {
		c = nextByte()
	}
	if c == '+' {
		c = nextByte()
	}
	rest := 0
	for c >= '0' && c <= '9' {
		rest = 10*rest + int(c-'0')
		c = nextByte()
	}
	phi := rest
	if rest%2 == 0 {
		phi /= 2
		for rest%2 == 0 {
			rest /= 2
		}
	}
	// After removing factors of two, every remaining prime factor is odd.
	for divisor := firstOddDivisor; divisor*divisor <= rest; divisor += 2 {
		if rest%divisor == 0 {
			phi -= phi / divisor
			for rest%divisor == 0 {
				rest /= divisor
			}
		}
	}
	if rest > 1 {
		phi -= phi / rest
	}
	answer := phi / 2
	position := len(output) - 1
	output[position] = '\n'
	for {
		position--
		output[position] = '0' + byte(answer%10)
		answer /= 10
		if answer == 0 {
			break
		}
	}
	writeAll(output[position:])
}
