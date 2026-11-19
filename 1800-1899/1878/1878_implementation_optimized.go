package main

import "syscall"

const maxInt64Digits = 20
const sideLength = 4
const initialMoveBound = 16

const inputCapacity = 256
const outputCapacity = 64

var inputBuffer [inputCapacity]byte
var inputAt, inputSize int
var outputBuffer [outputCapacity]byte
var outputSize int

func nextByte() int {
	for inputAt == inputSize {
		count, err := syscall.Read(syscall.Stdin, inputBuffer[:])
		if count > 0 {
			inputAt, inputSize = 0, count
		} else if err == syscall.EINTR {
			continue
		} else {
			// A zero-byte read is EOF even when the raw syscall returns no error.
			return -1
		}
	}
	value := inputBuffer[inputAt]
	inputAt++
	return int(value)
}

func readNumber() (int64, bool) {
	character := nextByte()
	for character >= 0 && character <= ' ' {
		character = nextByte()
	}
	if character < 0 {
		return 0, false
	}
	negative := character == '-'
	if negative || character == '+' {
		character = nextByte()
	}
	var value int64
	for character >= '0' && character <= '9' {
		// Negative accumulation also handles the minimum signed 64-bit value.
		value = value*10 - int64(character-'0')
		character = nextByte()
	}
	if negative {
		return value, true
	}
	return -value, true
}

func number() int64 { value, _ := readNumber(); return value }

func flushOutput() {
	for start := 0; start < outputSize; {
		count, err := syscall.Write(syscall.Stdout, outputBuffer[start:outputSize])
		if err == syscall.EINTR && count <= 0 {
			continue
		}
		if err != nil || count <= 0 {
			syscall.Exit(1)
		}
		start += count
	}
	outputSize = 0
}

func writeByte(value byte) {
	if outputSize == len(outputBuffer) {
		flushOutput()
	}
	outputBuffer[outputSize] = value
	outputSize++
}

func writeNumber(value int64) {
	magnitude := uint64(value)
	if value < 0 {
		writeByte('-')
		magnitude = uint64(-(value + 1)) + 1
	}
	var digits [maxInt64Digits]byte
	first := len(digits)
	for {
		first--
		digits[first] = '0' + byte(magnitude%10)
		magnitude /= 10
		if magnitude == 0 {
			break
		}
	}
	for _, digit := range digits[first:] {
		writeByte(digit)
	}
}

func main() {
	defer flushOutput()
	var counts [sideLength]int64
	for row := 0; row < sideLength; row++ {
		for column := 0; column < sideLength; column++ {
			colour := number()
			quadrant := column / 2
			if row >= 2 {
				quadrant = (sideLength - 1) - quadrant
			}
			if colour == 1 {
				counts[quadrant]++
			}
		}
	}
	best := int64(initialMoveBound)
	for target := 0; target < sideLength; target++ {
		var moves int64
		for at := 0; at < sideLength; at++ {
			distance := (at - target + sideLength) % sideLength
			if sideLength-distance < distance {
				distance = sideLength - distance
			}
			moves += counts[at] * int64(distance)
		}
		if moves < best {
			best = moves
		}
	}
	writeNumber(best)
	writeByte('\n')
}
