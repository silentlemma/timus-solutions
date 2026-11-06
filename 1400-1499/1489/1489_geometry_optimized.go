package main

import (
	"math"
	"syscall"
)

const (
	roundingOffset = 0.5
)

const (
	inputSize       = 128
	outputSize      = 16
	decimal         = 10
	coordinateScale = 100
	precision       = 8
	outputScale     = 100_000_000
)

type point struct{ x, y, z int64 }

var input [inputSize]byte
var cursor, available int

// Use standard handles directly, retrying interrupts and completing short writes.
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

func nextByte() byte {
	if cursor == available {
		available = readInput(input[:])
		cursor = 0
		if available == 0 {
			return 0
		}
	}
	ch := input[cursor]
	cursor++
	return ch
}

func digit(ch byte) bool { return ch >= '0' && ch <= '9' }

func hundredths() int64 {
	ch := nextByte()
	for ch != 0 && ch <= ' ' {
		ch = nextByte()
	}
	var value int64
	for digit(ch) {
		value = decimal*value + int64(ch-'0')
		ch = nextByte()
	}
	value *= coordinateScale
	if ch == '.' {
		place, ch := int64(decimal), nextByte()
		for place > 0 && digit(ch) {
			value += int64(ch-'0') * place
			place, ch = place/decimal, nextByte()
		}
	}
	return value
}

func fold(a, b, c, x, y int64) point {
	switch {
	case x < c:
		return point{0, y - b - c, c - x}
	case x > c+a:
		return point{a, y - b - c, x - c - a}
	case y < b:
		return point{x - c, b - y, c}
	case y < b+c:
		return point{x - c, 0, b + c - y}
	case y <= 2*b+c:
		return point{x - c, y - b - c, 0}
	default:
		return point{x - c, b, y - 2*b - c}
	}
}

func printDistance(distance int64) {
	var line [outputSize]byte
	at := len(line) - 1
	line[at] = '\n'
	for i := 0; i < precision; i++ {
		at--
		line[at] = '0' + byte(distance%decimal)
		distance /= decimal
	}
	at--
	line[at] = '.'
	for {
		at--
		line[at] = '0' + byte(distance%decimal)
		distance /= decimal
		if distance == 0 {
			break
		}
	}
	writeAll(line[at:])
}

func main() {
	a, b, c := hundredths(), hundredths(), hundredths()
	p := fold(a, b, c, hundredths(), hundredths())
	q := fold(a, b, c, hundredths(), hundredths())
	dx, dy, dz := p.x-q.x, p.y-q.y, p.z-q.z
	distance := math.Sqrt(float64(dx*dx+dy*dy+dz*dz)) * (outputScale / coordinateScale)
	printDistance(int64(distance + roundingOffset))
}
