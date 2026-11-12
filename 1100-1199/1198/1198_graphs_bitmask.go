package main

import (
	"math/bits"
	"syscall"
)

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

const outputSize = 16384

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

const maxVertices = 2000
const wordBits = 64
const maxWords = (maxVertices + wordBits - 1) / wordBits

var forward, reverseGraph [maxVertices][maxWords]uint64
var unseen [maxWords]uint64
var queue [maxVertices]uint16
var words, vertices int

func reset() {
	for word := 0; word < words; word++ {
		unseen[word] = ^uint64(0)
	}
	if vertices%wordBits != 0 {
		unseen[words-1] = (uint64(1) << uint(vertices%wordBits)) - 1
	}
}

func visit(root int, graph *[maxVertices][maxWords]uint64) {
	unseen[root/wordBits] &^= uint64(1) << uint(root%wordBits)
	head, tail := 0, 1
	queue[0] = uint16(root)
	for head < tail {
		vertex := queue[head]
		head++
		for word := 0; word < words; word++ {
			fresh := graph[vertex][word] & unseen[word]
			unseen[word] &^= fresh
			for fresh != 0 {
				queue[tail] = uint16(word*wordBits + bits.TrailingZeros64(fresh))
				tail++
				fresh &= fresh - 1
			}
		}
	}
}

func main() {
	vertices = number()
	words = (vertices + wordBits - 1) / wordBits
	for from := 0; from < vertices; from++ {
		for to := number(); to != 0; to = number() {
			to--
			forward[from][to/wordBits] |= uint64(1) << uint(to%wordBits)
			reverseGraph[to][from/wordBits] |= uint64(1) << uint(from%wordBits)
		}
	}
	reset()
	root := 0
	for vertex := 0; vertex < vertices; vertex++ {
		if unseen[vertex/wordBits]>>uint(vertex%wordBits)&1 != 0 {
			root = vertex
			visit(root, &forward)
		}
	}
	reset()
	visit(root, &forward)
	for word := 0; word < words; word++ {
		if unseen[word] != 0 {
			writeAll([]byte("0\n"))
			return
		}
	}
	reset()
	visit(root, &reverseGraph)
	for vertex := 0; vertex < vertices; vertex++ {
		if unseen[vertex/wordBits]>>uint(vertex%wordBits)&1 == 0 {
			writeNumber(vertex + 1)
			output[used] = ' '
			used++
		}
	}
	output[used] = '0'
	output[used+1] = '\n'
	used += 2
	writeAll(output[:used])
}
