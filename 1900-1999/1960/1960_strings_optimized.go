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

const outputSize = 8192
const maxDigits = 20
const maxLength = 100000
const rootCount = 2
const emptyRoot = 1

var output [outputSize]byte
var used int

func put(c byte) {
	if used == len(output) {
		writeAll(output[:])
		used = 0
	}
	output[used] = c
	used++
}

func writeNumber(value int) {
	var digits [maxDigits]byte
	first := len(digits)
	for {
		first--
		digits[first] = byte(value%10) + '0'
		value /= 10
		if value == 0 {
			break
		}
	}
	for _, c := range digits[first:] {
		put(c)
	}
}

type node struct {
	length               int32
	link, child, sibling uint32
	letter               byte
}

func transition(nodes []node, parent uint32, letter byte) uint32 {
	// The incoming edge belongs to the child node; siblings encode the parent's sparse edges.
	for edge := nodes[parent].child; edge != 0; edge = nodes[edge].sibling {
		if nodes[edge].letter == letter {
			return edge
		}
	}
	return 0
}

func main() {
	text := make([]byte, 0, maxLength)
	c := nextByte()
	for c != 0 && c <= ' ' {
		c = nextByte()
	}
	for c > ' ' {
		text = append(text, c)
		c = nextByte()
	}
	nodes := make([]node, len(text)+rootCount)
	nodes[0].length = -1
	count, last := uint32(rootCount), uint32(emptyRoot)
	for position, letter := range text {
		parent := last
		for {
			left := position - int(nodes[parent].length) - 1
			if left >= 0 && text[left] == letter {
				break
			}
			parent = nodes[parent].link
		}
		current := transition(nodes, parent, letter)
		if current == 0 {
			current = count
			count++
			nodes[current].length = nodes[parent].length + 2
			nodes[current].letter = letter
			nodes[current].sibling = nodes[parent].child
			nodes[parent].child = current
			if nodes[current].length == 1 {
				nodes[current].link = emptyRoot
			} else {
				candidate := nodes[parent].link
				for {
					left := position - int(nodes[candidate].length) - 1
					if left >= 0 && text[left] == letter {
						break
					}
					candidate = nodes[candidate].link
				}
				nodes[current].link = transition(nodes, candidate, letter)
			}
		}
		last = current
		if position != 0 {
			put(' ')
		}
		writeNumber(int(count - rootCount))
	}
	put('\n')
	writeAll(output[:used])
}
