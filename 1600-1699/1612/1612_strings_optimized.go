package main

import "syscall"

const maxInt64Digits = 20

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

func writeText(text string) {
	for index := 0; index < len(text); index++ {
		writeByte(text[index])
	}
}

func main() {
	defer flushOutput()
	const tram, trolley = "tram", "trolleybus"
	length, trams, trolleys := 0, 0, 0
	couldTram, couldTrolley := true, true
	for {
		character := nextByte()
		if character >= 'a' && character <= 'z' {
			if length >= len(tram) || byte(character) != tram[length] {
				couldTram = false
			}
			if length >= len(trolley) || byte(character) != trolley[length] {
				couldTrolley = false
			}
			length++
			continue
		}
		if couldTram && length == len(tram) {
			trams++
		}
		if couldTrolley && length == len(trolley) {
			trolleys++
		}
		if character < 0 {
			break
		}
		length, couldTram, couldTrolley = 0, true, true
	}
	switch {
	case trams > trolleys:
		writeText("Tram driver\n")
	case trolleys > trams:
		writeText("Trolleybus driver\n")
	default:
		writeText("Bus driver\n")
	}
}
