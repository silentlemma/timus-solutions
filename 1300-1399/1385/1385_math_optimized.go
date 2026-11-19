package main

import "syscall"

const maxInt64Digits = 20
const significantDigits = 3
const largestDigit = 9

const inputCapacity = 256
const outputCapacity = 256

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

func writeText(text string) {
	for index := 0; index < len(text); index++ {
		writeByte(text[index])
	}
}

func main() {
	defer flushOutput()
	length := int(number())
	prefix := length
	if prefix > significantDigits {
		prefix = significantDigits
	}
	power := int64(1)
	for i := 0; i < prefix; i++ {
		power *= 10
	}
	var answer int64
	for divisor := int64(1); divisor <= largestDigit; divisor++ {
		if power%divisor == 0 {
			answer += power/divisor - power/10
		}
	}
	// From the third power on, the valid divisors of 10^n are unchanged.
	writeNumber(answer)
	for i := significantDigits; i < length; i++ {
		writeByte('0')
	}
	writeByte('\n')
}
