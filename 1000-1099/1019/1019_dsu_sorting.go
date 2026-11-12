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

func word() byte {
	c := nextByte()
	for c != 0 && c <= ' ' {
		c = nextByte()
	}
	first := c
	for c > ' ' {
		c = nextByte()
	}
	return first
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

const end = 1000000000

func find(parent []int, position int) int {
	for parent[position] != position {
		parent[position] = parent[parent[position]]
		position = parent[position]
	}
	return position
}

func main() {
	n := number()
	left, right := make([]int, n), make([]int, n)
	colors := make([]byte, n)
	points := make([]int, 2, 2*n+2)
	points[1] = end
	for i := 0; i < n; i++ {
		left[i], right[i], colors[i] = number(), number(), word()
		points = append(points, left[i], right[i])
	}
	sort.Ints(points)
	unique := points[:1]
	for _, point := range points[1:] {
		if point != unique[len(unique)-1] {
			unique = append(unique, point)
		}
	}
	points = unique
	pieces := len(points) - 1
	parent := make([]int, pieces+1)
	white := make([]bool, pieces)
	for i := range parent {
		parent[i] = i
	}
	for i := range white {
		white[i] = true
	}
	// In reverse order each piece is assigned once, by its final repainting.
	for i := n - 1; i >= 0; i-- {
		stop := sort.SearchInts(points, right[i])
		for p := find(parent, sort.SearchInts(points, left[i])); p < stop; p = find(parent, p) {
			white[p] = colors[i] == 'w'
			parent[p] = p + 1
		}
	}
	bestLeft, bestRight, runStart := 0, 0, 0
	for i, isWhite := range white {
		if !isWhite {
			runStart = i + 1
		} else if points[i+1]-points[runStart] > bestRight-bestLeft {
			bestLeft, bestRight = points[runStart], points[i+1]
		}
	}
	writeNumber(bestLeft)
	output[used] = ' '
	used++
	writeNumber(bestRight)
	output[used] = '\n'
	used++
	writeAll(output[:used])
}
