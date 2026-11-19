package main

import "os"

const maxInt64Digits = 20
const largestRadix = 36

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

func wordByte() byte {
	character := nextByte()
	for character >= 0 && character <= ' ' {
		character = nextByte()
	}
	first := byte(character)
	for character > ' ' {
		character = nextByte()
	}
	return first
}

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
	total, highest := 0, 1
	character := nextByte()
	for character >= 0 && character <= ' ' {
		character = nextByte()
	}
	for character > ' ' {
		digit := character - '0'
		if character >= 'A' {
			digit = character - 'A' + 10
		}
		total += digit
		if digit > highest {
			highest = digit
		}
		character = nextByte()
	}
	for radix := highest + 1; radix <= largestRadix; radix++ {
		if total%(radix-1) == 0 {
			writeNumber(int64(radix))
			writeByte('\n')
			return
		}
	}
	writeText("No solution.\n")
}
