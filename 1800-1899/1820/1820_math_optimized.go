package main

import "os"

const maxInt64Digits = 20

const ioCapacity = 4096

var inputBuffer [ioCapacity]byte
var inputAt, inputSize int
var outputBuffer [ioCapacity]byte
var outputSize int

func nextByte() int {
	for inputAt == inputSize {
		count, err := os.Stdin.Read(inputBuffer[:])
		inputAt, inputSize = 0, count
		if count == 0 && err != nil {
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
		count, err := os.Stdout.Write(outputBuffer[start:outputSize])
		if err != nil || count == 0 {
			os.Exit(1)
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
	steaks, capacity := number(), number()
	minutes := (2*steaks + capacity - 1) / capacity
	if minutes < 2 {
		minutes = 2
	}
	writeNumber(minutes)
	writeByte('\n')
}
