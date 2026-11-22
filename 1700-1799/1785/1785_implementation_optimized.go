package main

import "os"

const swarmMinimum = 250
const throngMinimum = 100
const hordeMinimum = 50
const lotsMinimum = 20
const severalMinimum = 5

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

func writeText(text string) {
	for index := 0; index < len(text); index++ {
		writeByte(text[index])
	}
}

func main() {
	defer flushOutput()
	count := number()
	const legion, zounds = 1000, 500
	word := "few"
	switch {
	case count >= legion:
		word = "legion"
	case count >= zounds:
		word = "zounds"
	case count >= swarmMinimum:
		word = "swarm"
	case count >= throngMinimum:
		word = "throng"
	case count >= hordeMinimum:
		word = "horde"
	case count >= lotsMinimum:
		word = "lots"
	case count >= 10:
		word = "pack"
	case count >= severalMinimum:
		word = "several"
	}
	writeText(word)
	writeByte('\n')
}
