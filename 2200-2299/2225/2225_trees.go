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

const maxNails = 100000
const maxDigits = 20

type component struct {
	height uint32
	width  uint32
}

func main() {
	n := number()
	var stack [maxNails]component
	used := 0
	var answer int64
	for i := 0; i <= n; i++ {
		height := uint32(0)
		if i < n {
			height = uint32(number())
		}
		span := uint32(0)
		for used > 0 && stack[used-1].height >= height {
			used--
			top := stack[used]
			span += top.width
			floor := height
			if used > 0 && stack[used-1].height > floor {
				floor = stack[used-1].height
			}
			// At these levels the completed component needs ceil(span/2) strikes.
			answer += int64(top.height-floor) * int64((span+1)/2)
		}
		if i < n {
			stack[used] = component{height, span + 1}
			used++
		}
	}
	var output [maxDigits]byte
	first := len(output) - 1
	output[first] = '\n'
	for {
		first--
		output[first] = byte(answer%10) + '0'
		answer /= 10
		if answer == 0 {
			break
		}
	}
	writeAll(output[first:])
}
