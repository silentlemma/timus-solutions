package main

import "syscall"

const (
	inputSize  = 64
	outputSize = 24
)

var (
	input         [inputSize]byte
	inputPosition int
	inputLength   int
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

func nextInt() int64 {
	c := nextByte()
	for c != 0 && c <= ' ' {
		c = nextByte()
	}
	var value int64
	for c >= '0' && c <= '9' {
		value = value*10 + int64(c-'0')
		c = nextByte()
	}
	return value
}

func main() {
	var gcd int64
	for remaining := nextInt(); remaining > 0; remaining-- {
		length := nextInt()
		for length != 0 {
			gcd, length = length, gcd%length
		}
		// Once the gcd is one, no unread length can change the answer.
		if gcd == 1 {
			break
		}
	}
	var output [outputSize]byte
	position := len(output) - 1
	output[position] = '\n'
	for {
		position--
		output[position] = '0' + byte(gcd%10)
		gcd /= 10
		if gcd == 0 {
			break
		}
	}
	writeAll(output[position:])
}
