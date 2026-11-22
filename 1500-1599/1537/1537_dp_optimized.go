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

func writeText(text string) {
	for index := 0; index < len(text); index++ {
		writeByte(text[index])
	}
}

func main() {
	defer flushOutput()
	words, modulus := number(), number()
	if words < 2 {
		writeText("0\n")
		return
	}
	top := words / 2
	half := top / 2
	capacity := int(half/2) + 1
	ring := make([]int32, capacity)
	current := int64(1) % modulus
	if half >= 1 {
		ring[1%capacity] = int32(current)
	}
	readAt, writeAt := 1%capacity, 2%capacity
	for index := int64(2); index <= top; index++ {
		current = (current + int64(ring[readAt])) % modulus
		// g(j) is last read at 2j+1; storing after that read safely reuses its slot.
		if index <= half {
			ring[writeAt] = int32(current)
			writeAt++
			if writeAt == capacity {
				writeAt = 0
			}
		}
		if index&1 != 0 {
			readAt++
			if readAt == capacity {
				readAt = 0
			}
		}
	}
	writeNumber(current)
	writeByte('\n')
}
