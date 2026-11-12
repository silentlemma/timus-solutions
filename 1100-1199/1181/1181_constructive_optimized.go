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

// At most 997 diagonals, each with two four-digit indices and separators.
const outputSize = 12000

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

const maxVertices = 1000
const colorCount = 3
const triangleSize = 3

func main() {
	n := number()
	var color [maxVertices]byte
	var left, right [maxVertices]int
	var alive [maxVertices]bool
	var counts [colorCount]int
	for v := 0; v < n; v++ {
		c := nextByte()
		for c <= ' ' {
			c = nextByte()
		}
		value := byte(2)
		if c == 'R' {
			value = 0
		} else if c == 'G' {
			value = 1
		}
		color[v] = value
		counts[value]++
		left[v], right[v] = (v+n-1)%n, (v+1)%n
		alive[v] = true
	}
	var pending [maxVertices + 2*maxVertices]int
	head, tail := 0, 0
	for v := 0; v < n; v++ {
		if color[left[v]] != color[right[v]] {
			pending[tail] = v
			tail++
		}
	}
	writeNumber(n - triangleSize)
	output[used] = '\n'
	used++
	printCut := func(a, b int) {
		writeNumber(a + 1)
		output[used] = ' '
		used++
		writeNumber(b + 1)
		output[used] = '\n'
		used++
	}
	remaining := n
	for remaining > triangleSize {
		if counts[0] == 1 || counts[1] == 1 || counts[2] == 1 {
			anchor := 0
			for !alive[anchor] || counts[color[anchor]] != 1 {
				anchor++
			}
			for v := right[right[anchor]]; right[v] != anchor; v = right[v] {
				printCut(anchor, v)
			}
			break
		}
		v := pending[head]
		head++
		if !alive[v] || color[left[v]] == color[right[v]] {
			continue
		}
		before, after := left[v], right[v]
		printCut(before, after)
		alive[v] = false
		right[before], left[after] = after, before
		counts[color[v]]--
		remaining--
		// Only the neighbours can change; the queue receives at most 3*n entries.
		pending[tail], pending[tail+1] = before, after
		tail += 2
	}
	writeAll(output[:used])
}
