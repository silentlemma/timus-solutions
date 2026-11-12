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

const inputSize = 8192

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

const outputSize = 64

var output [outputSize]byte
var used int

func writeNumber(value int) {
	const maxDigits = 20
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
	used += copy(output[used:], digits[first:])
}

const maxSide = 100
const maxCells = maxSide * maxSide
const maxPadded = (maxSide + 2) * (maxSide + 2)
const maxHeight = 100000
const directionCount = 2 * 2
const infinity = uint16(65535)

var stride, size, start int
var height [maxPadded]int32
var flood, distance [maxPadded]uint16
var queue [maxCells]uint16

func spread(source int) {
	queue[0] = uint16(source)
	flood[source] = 0
	head, tail := 0, 1
	for head < tail {
		cell := int(queue[head])
		head++
		for _, next := range [directionCount]int{cell - stride, cell - 1, cell + 1, cell + stride} {
			if flood[next] == infinity && height[next] <= height[cell] {
				flood[next] = flood[cell] + 1
				queue[tail] = uint16(next)
				tail++
			}
		}
	}
}

func canEscape(jump int) bool {
	if flood[start] == infinity {
		return true
	}
	for cell := 0; cell < size; cell++ {
		distance[cell] = infinity
	}
	distance[start] = 0
	queue[0] = uint16(start)
	head, tail := 0, 1
	for head < tail {
		cell := int(queue[head])
		head++
		arrival := distance[cell] + 1
		for _, next := range [directionCount]int{cell - stride, cell - 1, cell + 1, cell + stride} {
			if distance[next] != infinity || arrival >= flood[next] ||
				int(height[next]-height[cell]) > jump {
				continue
			}
			if flood[next] == infinity {
				return true
			}
			distance[next] = arrival
			queue[tail] = uint16(next)
			tail++
		}
	}
	return false
}

func main() {
	rows, columns := number(), number()
	stride = columns + 2
	size = (rows + 2) * stride
	for cell := 0; cell < size; cell++ {
		height[cell] = -1
	}
	for row := 1; row <= rows; row++ {
		for column := 1; column <= columns; column++ {
			cell := row*stride + column
			height[cell] = int32(number())
			flood[cell] = infinity
		}
	}
	row, column := number(), number()
	start = row*stride + column
	row, column = number(), number()
	spread(row*stride + column)
	if !canEscape(maxHeight) {
		writeAll([]byte("-1\n"))
		return
	}
	low, high := 0, maxHeight
	for low < high {
		middle := (low + high) / 2
		if canEscape(middle) {
			high = middle
		} else {
			low = middle + 1
		}
	}
	// Borders have flood time zero; every real shortest path has fewer than 10000 steps.
	writeNumber(low)
	output[used] = '\n'
	used++
	writeAll(output[:used])
}
