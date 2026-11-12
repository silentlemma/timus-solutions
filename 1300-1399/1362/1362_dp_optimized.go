package main

import (
	"sort"
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

const maxEmployees = 100000

var employees uint32
var boss, child, sibling [maxEmployees]uint32
var parent, order, finish, times [maxEmployees]uint32

func visit(other, vertex uint32, tail *int) {
	if other != employees && other != parent[vertex] {
		parent[other] = vertex
		order[*tail] = other
		*tail = *tail + 1
	}
}

func collect(other, vertex uint32, used *int) {
	if other != employees && other != parent[vertex] {
		times[*used] = finish[other]
		*used = *used + 1
	}
}

func main() {
	employees = uint32(number())
	for vertex := uint32(0); vertex < employees; vertex++ {
		boss[vertex], child[vertex] = employees, employees
	}
	for vertex := uint32(0); vertex < employees; vertex++ {
		for {
			value := number()
			if value == 0 {
				break
			}
			next := uint32(value - 1)
			boss[next] = vertex
			sibling[next] = child[vertex]
			child[vertex] = next
		}
	}
	source := uint32(number() - 1)
	parent[source], order[0] = source, source
	tail := 1
	for cursor := 0; cursor < tail; cursor++ {
		vertex := order[cursor]
		visit(boss[vertex], vertex, &tail)
		for next := child[vertex]; next != employees; next = sibling[next] {
			visit(next, vertex, &tail)
		}
	}
	for cursor := tail - 1; cursor >= 0; cursor-- {
		vertex := order[cursor]
		used := 0
		collect(boss[vertex], vertex, &used)
		for next := child[vertex]; next != employees; next = sibling[next] {
			collect(next, vertex, &used)
		}
		if used > 1 {
			sort.Slice(times[:used], func(i, j int) bool { return times[i] > times[j] })
		}
		best := uint32(0)
		for i := 0; i < used; i++ {
			completion := times[i] + uint32(i+1)
			if completion > best {
				best = completion
			}
		}
		finish[vertex] = best
	}
	// Reuse one scratch prefix for every employee's descending child times.
	writeNumber(int(finish[source]))
	output[used] = '\n'
	used++
	writeAll(output[:used])
}
