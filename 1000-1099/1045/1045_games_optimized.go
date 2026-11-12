package main

import "syscall"

const inputSize = 256
const decimalBase = 10
const maxVertices = 1000

type vertex struct {
	neighbour uint16
	degree    uint8
	winning   bool
}

const maxDigits = 4
const winPrefix = "First player wins flying to airport "

var input [inputSize]byte
var position, available int
var nodes [maxVertices + 1]vertex
var queue [maxVertices]uint16

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
	c := input[position]
	position++
	return c
}

func number() int {
	c := readByte()
	for c != 0 && c <= ' ' {
		c = readByte()
	}
	value := 0
	for c >= '0' && c <= '9' {
		value = value*decimalBase + int(c-'0')
		c = readByte()
	}
	return value
}

func main() {
	n, root := number(), number()
	for i := 1; i < n; i++ {
		a, b := number(), number()
		nodes[a].neighbour ^= uint16(b)
		nodes[b].neighbour ^= uint16(a)
		nodes[a].degree++
		nodes[b].degree++
	}
	length := 0
	for v := 1; v <= n; v++ {
		if v != root && nodes[v].degree == 1 {
			queue[length] = uint16(v)
			length++
		}
	}
	best := 0
	for head := 0; head < length; head++ {
		v := queue[head]
		parent := nodes[v].neighbour
		if !nodes[v].winning {
			nodes[parent].winning = true
			if int(parent) == root && (best == 0 || int(v) < best) {
				best = int(v)
			}
		}
		nodes[parent].neighbour ^= v
		nodes[parent].degree--
		if int(parent) != root && nodes[parent].degree == 1 {
			queue[length] = parent
			length++
		}
	}
	writeAnswer(best)
}

func writeAnswer(best int) {
	var buffer [len(winPrefix) + maxDigits + 1]byte
	var output []byte
	if best == 0 {
		output = buffer[:copy(buffer[:], "First player loses\n")]
	} else {
		var digits [maxDigits]byte
		start := len(digits)
		for best != 0 {
			start--
			digits[start] = '0' + byte(best%decimalBase)
			best /= decimalBase
		}
		length := copy(buffer[:], winPrefix)
		length += copy(buffer[length:], digits[start:])
		buffer[length] = '\n'
		output = buffer[:length+1]
	}
	for len(output) > 0 {
		count, err := syscall.Write(syscall.Stdout, output)
		if count > 0 {
			output = output[count:]
		}
		if err == syscall.EINTR {
			continue
		}
		if count <= 0 || err != nil {
			return
		}
	}
}
