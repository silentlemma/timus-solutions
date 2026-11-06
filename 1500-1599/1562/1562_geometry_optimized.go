package main

import (
	"math"
	"syscall"
)

const (
	roundingOffset = 0.5
)

const (
	inputSize   = 256
	outputSize  = 2048
	lineSize    = 16
	decimal     = 10
	precision   = 6
	micrograms  = 1_000_000
	squareScale = 3
	volumeScale = math.Pi / 12
)

var input [inputSize]byte
var output [outputSize]byte
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

func nextDecimal() float64 {
	ch := nextByte()
	for ch != 0 && ch <= ' ' {
		ch = nextByte()
	}
	value := 0.0
	for digit(ch) {
		value = value*decimal + float64(ch-'0')
		ch = nextByte()
	}
	if ch == '.' {
		place := 1.0
		for ch = nextByte(); digit(ch); ch = nextByte() {
			place /= decimal
			value += float64(ch-'0') * place
		}
	}
	return value
}

func appendWeight(result []byte, weight int64) []byte {
	var line [lineSize]byte
	at := len(line) - 1
	line[at] = '\n'
	for i := 0; i < precision; i++ {
		at--
		line[at] = '0' + byte(weight%decimal)
		weight /= decimal
	}
	at--
	line[at] = '.'
	for {
		at--
		line[at] = '0' + byte(weight%decimal)
		weight /= decimal
		if weight == 0 {
			return append(result, line[at:]...)
		}
	}
}

func main() {
	width, height, count := nextDecimal(), nextDecimal(), int(nextDecimal())
	square := count * count
	scale := volumeScale * width * width * height * micrograms / float64(square*count)
	result := output[:0]
	for i := 0; i < count; i++ {
		middle := 2*i + 1 - count
		// Integrate the quadratic cross-section over this slice.
		weight := scale * float64(squareScale*(square-middle*middle)-1)
		result = appendWeight(result, int64(weight+roundingOffset))
	}
	writeAll(result)
}
