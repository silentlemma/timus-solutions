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

const maxSide = 50
const maxCells = maxSide * maxSide
const colors = 10
const players = 2

type simulation struct {
	width, cells int
	color, owner [maxCells]byte
	area         [players]int
	frontier     [players][colors][]uint16
	head         [players][colors]int
}

func (s *simulation) offer(side, cell int) {
	if s.owner[cell] == 0 {
		alliance := s.color[cell]
		s.frontier[side][alliance] = append(s.frontier[side][alliance], uint16(cell))
	}
}

func (s *simulation) claim(side, cell int) {
	s.owner[cell] = byte(side + 1)
	s.area[side]++
	if cell >= s.width {
		s.offer(side, cell-s.width)
	}
	if cell+s.width < s.cells {
		s.offer(side, cell+s.width)
	}
	if cell%s.width != 0 {
		s.offer(side, cell-1)
	}
	if cell%s.width+1 < s.width {
		s.offer(side, cell+1)
	}
}

func (s *simulation) expand(side, alliance int) {
	for s.head[side][alliance] < len(s.frontier[side][alliance]) {
		cell := int(s.frontier[side][alliance][s.head[side][alliance]])
		s.head[side][alliance]++
		// Stale entries and duplicates must never capture an already owned cell.
		if s.owner[cell] == 0 {
			s.claim(side, cell)
		}
	}
}

func main() {
	height, width := number(), number()
	s := simulation{width: width, cells: height * width}
	for cell := 0; cell < s.cells; cell++ {
		c := nextByte()
		for c <= ' ' {
			c = nextByte()
		}
		s.color[cell] = c - '0'
	}
	seeds := [players]int{(height - 1) * width, width - 1}
	for side, seed := range seeds {
		s.claim(side, seed)
		s.expand(side, int(s.color[seed]))
	}
	moves := number()
	for turn := 0; turn < moves; turn++ {
		s.expand(turn%players, number())
	}
	for _, area := range s.area {
		writeNumber(area)
		output[used] = '\n'
		used++
	}
	writeAll(output[:used])
}
