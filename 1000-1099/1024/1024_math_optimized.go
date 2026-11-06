package main

import "syscall"

const (
	maxSize    = 1000
	inputSize  = 64
	outputSize = 16
)

var (
	input         [inputSize]byte
	inputPosition int
	inputLength   int
	permutation   [maxSize + 1]uint16
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

func gcd(a, b int64) int64 {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func main() {
	n := nextInt()
	for i := 1; i <= n; i++ {
		permutation[i] = uint16(nextInt())
	}
	order := int64(1)
	for i := 1; i <= n; i++ {
		if permutation[i] == 0 {
			continue
		}
		// Zero is outside the permutation and marks an already counted vertex.
		var length int64
		for node := uint16(i); permutation[node] != 0; length++ {
			next := permutation[node]
			permutation[node] = 0
			node = next
		}
		order = order / gcd(order, length) * length
	}
	var output [outputSize]byte
	position := len(output) - 1
	output[position] = '\n'
	for {
		position--
		output[position] = '0' + byte(order%10)
		order /= 10
		if order == 0 {
			break
		}
	}
	writeAll(output[position:])
}
