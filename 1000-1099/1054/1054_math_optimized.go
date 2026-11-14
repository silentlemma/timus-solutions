package main

import "syscall"

const (
	sourceRod  = 1
	targetRod  = 2
	decimal    = 10
	maxDisks   = 31
	inputSize  = 64
	numberSize = 12
)

var input [inputSize]byte
var offset, length int

func nextByte() byte {
	if offset == length {
		for {
			size, err := syscall.Read(syscall.Stdin, input[:])
			if err == syscall.EINTR {
				continue
			}
			if size <= 0 || err != nil {
				return 0
			}
			length = size
			break
		}
		offset = 0
		if length == 0 {
			return 0
		}
	}
	value := input[offset]
	offset++
	return value
}

func number() int {
	c := nextByte()
	for c != 0 && c <= ' ' {
		c = nextByte()
	}
	value := 0
	for c >= '0' && c <= '9' {
		value = decimal*value + int(c-'0')
		c = nextByte()
	}
	return value
}

func main() {
	count := number()
	var rods [maxDisks]byte
	for j := 0; j < count; j++ {
		rods[j] = byte(number())
	}

	source, target := byte(sourceRod), byte(targetRod)
	var moves uint32
	for i := count - 1; i >= 0; i-- {
		// The source and target XOR to the spare rod.
		spare := source ^ target
		moves <<= 1
		switch rods[i] {
		case source:
			target = spare
		case target:
			moves++
			source = spare
		default:
			write([]byte("-1\n"))
			return
		}
	}

	var output [numberSize]byte
	end := len(output) - 1
	output[end] = '\n'
	for {
		end--
		output[end] = '0' + byte(moves%decimal)
		moves /= decimal
		if moves == 0 {
			break
		}
	}
	write(output[end:])
}
func write(data []byte) {
	for len(data) != 0 {
		size, err := syscall.Write(syscall.Stdout, data)
		if err == syscall.EINTR {
			continue
		}
		if size <= 0 || err != nil {
			return
		}
		data = data[size:]
	}
}
