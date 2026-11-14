package main

import (
	"bufio"
	"os"
)

const step = 1999
const maxLength = 30000
const bitsPerByte = 8
const bufferSize = 512

func main() {
	input := bufio.NewReaderSize(os.Stdin, bufferSize)
	var questions, spaces [(maxLength + bitsPerByte - 1) / bitsPerByte]byte
	length := 0
	for c, err := input.ReadByte(); err == nil; c, err = input.ReadByte() {
		if c == '\r' || c == '\n' {
			continue
		}
		// Only question marks and spaces produce a distinct answer.
		offset, bit := length/bitsPerByte, byte(1)<<(length%bitsPerByte)
		switch c {
		case '?':
			questions[offset] |= bit
		case ' ':
			spaces[offset] |= bit
		}
		length++
	}
	if length == 0 {
		return
	}
	// Grow the circle by one, translating the surviving index after each deletion.
	survivor := 0
	for size := 2; size <= length; size++ {
		survivor = (survivor + step) % size
	}
	answer := "No comments\n"
	offset, bit := survivor/bitsPerByte, byte(1)<<(survivor%bitsPerByte)
	switch {
	case questions[offset]&bit != 0:
		answer = "Yes\n"
	case spaces[offset]&bit != 0:
		answer = "No\n"
	}
	os.Stdout.WriteString(answer)
}
