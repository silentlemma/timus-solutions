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

const symbolCount = 90
const alphabetSize = symbolCount * symbolCount * symbolCount
const lowestSymbol = '!'
const maxPattern = 8000
const maxDigits = 20

func code(first byte) int {
	second, third := nextByte(), nextByte()
	return (int(first-lowestSymbol)*symbolCount+int(second-lowestSymbol))*symbolCount +
		int(third-lowestSymbol)
}

func main() {
	var deficit [alphabetSize]int16
	var ring [maxPattern]uint32
	size := 0
	c := nextByte()
	for c != 0 && c != '\n' {
		if c > ' ' {
			deficit[code(c)]++
			size++
		}
		c = nextByte()
	}
	missing, position, filled, answer := size, 0, 0, 0
	for c = nextByte(); c != 0; c = nextByte() {
		if c <= ' ' {
			continue
		}
		if filled == size {
			old := ring[position]
			if deficit[old] >= 0 {
				missing++
			}
			deficit[old]++
		} else {
			filled++
		}
		letter := code(c)
		if deficit[letter] > 0 {
			missing--
		}
		// Each count difference lies in [-size,size], within signed 16-bit bounds.
		deficit[letter]--
		ring[position] = uint32(letter)
		position++
		if position == size {
			position = 0
		}
		if missing == 0 {
			answer++
		}
	}
	var output [maxDigits]byte
	first := len(output) - 1
	output[first] = '\n'
	for {
		first--
		output[first] = byte(answer%10) + '0'
		answer /= 10
		if answer == 0 {
			break
		}
	}
	writeAll(output[first:])
}
