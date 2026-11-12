package main

import "syscall"

const (
	maxVertices         = 1000
	step                = 2
	limit               = 999
	bufferSize          = 256
	pointReserve        = 12
	digitsPerCoordinate = 4
)

var head, depth, position [maxVertices + 1]uint16
var to, next [2 * maxVertices]uint16
var stack [maxVertices]uint16
var input, output [bufferSize]byte
var cursor, available int

func readByte() byte {
	for cursor == available {
		count, err := syscall.Read(syscall.Stdin, input[:])
		if count > 0 {
			cursor, available = 0, count
			break
		}
		if err != syscall.EINTR {
			return 0
		}
	}
	character := input[cursor]
	cursor++
	return character
}

func number() int {
	c := readByte()
	for c != 0 && c <= ' ' {
		c = readByte()
	}
	value := 0
	for c >= '0' && c <= '9' {
		value = value*10 + int(c-'0')
		c = readByte()
	}
	return value
}

func appendNumber(buffer []byte, value int) []byte {
	if value < 0 {
		buffer = append(buffer, '-')
		value = -value
	}
	var digits [digitsPerCoordinate]byte
	start := len(digits)
	for {
		start--
		digits[start] = '0' + byte(value%10)
		value /= 10
		if value == 0 {
			return append(buffer, digits[start:]...)
		}
	}
}

func flush(buffer []byte) {
	for len(buffer) > 0 {
		count, err := syscall.Write(syscall.Stdout, buffer)
		if count > 0 {
			buffer = buffer[count:]
		}
		if err == syscall.EINTR {
			continue
		}
		if count <= 0 || err != nil {
			return
		}
	}
}

func main() {
	n := number()
	for edge := 1; edge < 2*n-1; edge += 2 {
		a, b := number(), number()
		to[edge], next[edge], head[a] = uint16(b), head[a], uint16(edge)
		to[edge+1], next[edge+1], head[b] = uint16(a), head[b], uint16(edge+1)
	}
	stack[0], depth[1] = 1, 1
	length := 1
	for order := uint16(0); length > 0; order++ {
		length--
		v := stack[length]
		position[v] = order
		for e := head[v]; e != 0; e = next[e] {
			w := to[e]
			if depth[w] == 0 {
				depth[w] = depth[v] + 1
				stack[length] = w
				length++
			}
		}
	}
	buffer := output[:0]
	for v := 1; v <= n; v++ {
		if len(buffer)+pointReserve > cap(buffer) {
			flush(buffer)
			buffer = output[:0]
		}
		buffer = appendNumber(buffer, int(position[v])*step-limit)
		buffer = append(buffer, ' ')
		buffer = appendNumber(buffer, int(depth[v]-1))
		buffer = append(buffer, '\n')
	}
	flush(buffer)
}
