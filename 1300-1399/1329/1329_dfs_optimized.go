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

const ids = 40001
const none uint16 = 65535
const outputSize = 8192

type node struct{ parent, child, sibling, enter, leave uint16 }

var nodes [ids]node
var output [outputSize]byte

func ancestor(a, b int) bool {
	return nodes[a].enter != none && nodes[a].enter <= nodes[b].enter &&
		nodes[b].enter < nodes[a].leave
}

func main() {
	n, root := number(), none
	for i := range nodes {
		nodes[i] = node{none, none, none, none, 0}
	}
	for i := 0; i < n; i++ {
		vertex, parent := number(), number()
		if parent < 0 {
			root = uint16(vertex)
		} else {
			nodes[vertex].parent = uint16(parent)
			nodes[vertex].sibling = nodes[parent].child
			nodes[parent].child = uint16(vertex)
		}
	}
	vertex, clock := root, uint16(0)
	for vertex != none {
		nodes[vertex].enter = clock
		clock++
		if nodes[vertex].child != none {
			vertex = nodes[vertex].child
			continue
		}
		for vertex != none {
			nodes[vertex].leave = clock
			if nodes[vertex].sibling != none {
				vertex = nodes[vertex].sibling
				break
			}
			vertex = nodes[vertex].parent
		}
	}
	queries, used := number(), 0
	for i := 0; i < queries; i++ {
		a, b := number(), number()
		answer := byte('0')
		if ancestor(a, b) {
			answer = '1'
		} else if ancestor(b, a) {
			answer = '2'
		}
		output[used] = answer
		output[used+1] = '\n'
		used += 2
		if used == len(output) {
			writeAll(output[:used])
			used = 0
		}
	}
	writeAll(output[:used])
}
