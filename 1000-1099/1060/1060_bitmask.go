package main

import (
	"math/bits"
	"syscall"
)

const (
	size       = 4
	rowMask    = 1<<size - 1
	impossible = size*size + 1
	inputSize  = 64
	outputSize = 8
)

var (
	input         [inputSize]byte
	inputPosition int
	inputLength   int
)

// Use standard handles directly; retry interrupts and finish short writes.
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
	if inputPosition == inputLength {
		inputLength = readInput(input[:])
		inputPosition = 0
		if inputLength == 0 {
			return 0
		}
	}
	value := input[inputPosition]
	inputPosition++
	return value
}

func minimum(board [size]uint8, target uint8) int {
	best := impossible
	for first := uint8(0); first <= rowMask; first++ {
		previous, current := uint8(0), first
		count := 0
		for _, row := range board {
			count += bits.OnesCount8(current)
			within := current ^ (current<<1)&rowMask ^ (current >> 1)
			// Each remaining mismatch forces the press directly below it.
			previous, current = current, row^target^within^previous
		}
		if current == 0 && count < best {
			best = count
		}
	}
	return best
}

func main() {
	var board [size]uint8
	for row := range board {
		for col := 0; col < size; col++ {
			c := nextByte()
			for c != 0 && c <= ' ' {
				c = nextByte()
			}
			if c == 0 {
				return
			}
			if c == 'b' {
				board[row] |= 1 << uint(col)
			}
		}
	}
	best := minimum(board, 0)
	if black := minimum(board, rowMask); black < best {
		best = black
	}
	if best == impossible {
		writeAll([]byte("Impossible\n"))
		return
	}
	var output [outputSize]byte
	position := len(output) - 1
	output[position] = '\n'
	for {
		position--
		output[position] = '0' + byte(best%10)
		best /= 10
		if best == 0 {
			break
		}
	}
	writeAll(output[position:])
}
