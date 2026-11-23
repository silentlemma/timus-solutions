package main

import (
	"os"
)

// keys holds the characters of each key in the order of presses; the space
// has a key of its own
var keys = []string{"abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vwx", "yz", ".,!", " "}

func main() {
	// the whole first line, spaces included; anything else costs nothing
	// Build the byte lookup once instead of searching eleven keys per character.
	var costs [256]byte
	for _, key := range keys {
		for i := range key {
			costs[key[i]] = byte(i + 1)
		}
	}
	total := 0
	for c := nextByte(); c >= 0; c = nextByte() {
		if c == '\n' {
			break
		}
		total += int(costs[c])
	}
	writeInteger(total)
}

func writeInteger(value int) {
	var buffer [24]byte
	first := len(buffer) - 1
	buffer[first] = '\n'
	for {
		first--
		buffer[first] = byte('0' + value%10)
		value /= 10
		if value == 0 {
			break
		}
	}
	os.Stdout.Write(buffer[first:])
}

const inputBufferBytes = 256

var inputBuffer [inputBufferBytes]byte
var inputPosition, inputLength int

// Refill a fixed byte buffer; EOF is separate from every possible input byte.
func nextByte() int {
	if inputPosition == inputLength {
		inputLength, _ = os.Stdin.Read(inputBuffer[:])
		inputPosition = 0
		if inputLength == 0 {
			return -1
		}
	}
	value := inputBuffer[inputPosition]
	inputPosition++
	return int(value)
}
