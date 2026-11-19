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

func writeText(text string) {
	for index := 0; index < len(text); index++ {
		writeByte(text[index])
	}
}

func main() {
	defer flushOutput()
	stones, count := int(number()), int(number())
	moves := make([]int, count)
	for i := range moves {
		moves[i] = int(number())
	}
	const wordBits = 64
	win := make([]uint64, stones/wordBits+1)
	win[0] = 1
	for remaining := 1; remaining <= stones; remaining++ {
		for _, take := range moves {
			if take > remaining {
				continue
			}
			previous := remaining - take
			if win[previous/wordBits]&(uint64(1)<<uint(previous%wordBits)) == 0 {
				win[remaining/wordBits] |= uint64(1) << uint(remaining%wordBits)
				break
			}
		}
	}
	if win[stones/wordBits]&(uint64(1)<<uint(stones%wordBits)) != 0 {
		writeText("1\n")
	} else {
		writeText("2\n")
	}
}
