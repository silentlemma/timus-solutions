package main

import "os"

const factorDigitCapacity = 32
const largestDigit = 9

const inputCapacity = 256
const outputCapacity = 64

var inputBuffer [inputCapacity]byte
var inputAt, inputSize int
var outputBuffer [outputCapacity]byte
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

func writeText(text string) {
	for index := 0; index < len(text); index++ {
		writeByte(text[index])
	}
}

func main() {
	defer flushOutput()
	value := number()
	if value == 0 {
		writeText("10\n")
		return
	}
	if value == 1 {
		writeText("1\n")
		return
	}
	// Every appended factor is at least two and the input is at most 10^9.
	var digits [factorDigitCapacity]byte
	count := 0
	for divisor := int64(largestDigit); divisor >= 2; divisor-- {
		for value%divisor == 0 {
			digits[count] = byte(divisor) + '0'
			count++
			value /= divisor
		}
	}
	if value != 1 {
		writeText("-1\n")
		return
	}
	for index := count - 1; index >= 0; index-- {
		writeByte(digits[index])
	}
	writeByte('\n')
}
