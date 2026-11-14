package main

import "syscall"

const (
	top = iota
	bottom
	north
	south
	east
	west
	sides
)

const (
	goEast = iota
	goWest
	goNorth
	goSouth
	moves
)

const stride = 12
const decimal = 10
const answerBuffer = 8
const inputSize = 512
const maxStates = stride * stride * sides
const bitsPerWord = 64
const stateWords = (maxStates + bitsPerWord - 1) / bitsPerWord

var step = [moves]int{1, -1, stride, -stride}
var roll = [moves][sides]int{
	{east, west, north, south, bottom, top},
	{west, east, north, south, top, bottom},
	{north, south, bottom, top, east, west},
	{south, north, top, bottom, east, west},
}

var input [inputSize]byte
var start, end int

func nextByte() byte {
	if start == end {
		for {
			n, err := syscall.Read(syscall.Stdin, input[:])
			if err == syscall.EINTR {
				continue
			}
			if n <= 0 {
				return 0
			}
			start, end = 0, n
			break
		}
	}
	value := input[start]
	start++
	return value
}

func write(data []byte) {
	for len(data) > 0 {
		n, err := syscall.Write(syscall.Stdout, data)
		if err == syscall.EINTR {
			continue
		}
		if n <= 0 {
			return
		}
		data = data[n:]
	}
}

func token() (int, byte) {
	c := nextByte()
	for c != 0 && c <= ' ' {
		c = nextByte()
	}
	if c < '0' || c > '9' {
		return 0, c
	}
	value := 0
	for '0' <= c && c <= '9' {
		value = decimal*value + int(c-'0')
		c = nextByte()
	}
	return value, '0'
}

func number() int {
	value, _ := token()
	return value
}

func blockWalls(width, height int) [stride * stride]uint8 {
	var blocked [stride * stride]uint8
	for x := 1; x <= width; x++ {
		blocked[stride+x] |= 1 << goSouth
		blocked[stride*height+x] |= 1 << goNorth
	}
	for y := 1; y <= height; y++ {
		blocked[stride*y+1] |= 1 << goWest
		blocked[stride*y+width] |= 1 << goEast
	}
	direction := goEast
	for {
		x, marker := token()
		switch marker {
		case 0:
			return blocked
		case 'v':
			direction = goEast
		case 'h':
			direction = goNorth
		default:
			cell := x + stride*number()
			blocked[cell] |= 1 << direction
			blocked[cell+step[direction]] |= 1 << (direction + 1)
		}
	}
}

func shortest(start, goal int, blocked *[stride * stride]uint8) int {
	var queue [maxStates]uint16
	var seen [stateWords]uint64
	startState, goalState := start*sides+top, goal*sides+top
	queue[0] = uint16(startState)
	seen[startState/bitsPerWord] = 1 << (startState % bitsPerWord)
	// States in one frontier have the same distance, so only visited bits are needed.
	for distance, first, last := 0, 0, 1; first < last; distance++ {
		after := last
		for _, state := range queue[first:last] {
			if int(state) == goalState {
				return distance
			}
			cell, side := int(state)/sides, int(state)%sides
			for direction, offset := range step {
				if blocked[cell]&(1<<direction) != 0 {
					continue
				}
				next := (cell+offset)*sides + roll[direction][side]
				word := &seen[next/bitsPerWord]
				mask := uint64(1) << (next % bitsPerWord)
				if *word&mask == 0 {
					*word |= mask
					queue[after] = uint16(next)
					after++
				}
			}
		}
		first, last = last, after
	}
	return -1
}

func main() {
	width, height := number(), number()
	start := number() + stride*number()
	goal := number() + stride*number()
	blocked := blockWalls(width, height)
	answer := shortest(start, goal, &blocked)
	if answer < 0 {
		write([]byte("No solution\n"))
		return
	}
	var digits [answerBuffer]byte
	pos := len(digits) - 1
	digits[pos] = '\n'
	for {
		pos--
		digits[pos] = '0' + byte(answer%decimal)
		answer /= decimal
		if answer == 0 {
			break
		}
	}
	write(digits[pos:])
}
