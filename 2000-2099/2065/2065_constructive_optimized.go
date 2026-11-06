package main

import "syscall"

const (
	maxCount   = 500
	inputSize  = 64
	outputSize = maxCount*6 + 1
	maxDigits  = 4
)

var (
	input         [inputSize]byte
	inputPosition int
	inputLength   int
	output        [outputSize]byte
	outputLength  int
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

func nextInt() int {
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

func writeByte(value byte) {
	output[outputLength] = value
	outputLength++
}

func writeNumber(value int) {
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
	for ; position < len(digits); position++ {
		writeByte(digits[position])
	}
}

func main() {
	n, k := nextInt(), nextInt()
	writeByte('0')
	for i := 0; i < n-k; i++ {
		writeByte(' ')
		writeByte('0')
	}
	// The prefix sums alternate between zero and consecutive positive integers.
	for i := 1; i < k; i++ {
		writeByte(' ')
		if i%2 == 0 {
			writeByte('-')
			writeNumber(i / 2)
		} else {
			writeNumber((i + 1) / 2)
		}
	}
	writeByte('\n')
	writeAll(output[:outputLength])
}
