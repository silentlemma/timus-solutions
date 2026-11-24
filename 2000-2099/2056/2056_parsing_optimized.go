package main

import (
	"syscall"
)

const (
	lowMark          = 3
	topMark          = 5
	doubledThreshold = 9
)

func classify(count, total, lowest int) string {
	if lowest == lowMark {
		return "None"
	}
	if lowest == topMark {
		return "Named"
	}
	if 2*total >= doubledThreshold*count {
		return "High"
	}
	return "Common"
}
func main() {
	count := integer()
	total, lowest := 0, topMark
	for i := 0; i < count; i++ {
		grade := integer()
		// One lowest mark settles the result regardless of the remaining grades.
		if grade == lowMark {
			writeBytes([]byte("None\n"))
			return
		}
		total += grade
		if grade < lowest {
			lowest = grade
		}
	}
	writeBytes(append([]byte(classify(count, total, lowest)), '\n'))
}

const inputBufferBytes = 256

var inputBuffer [inputBufferBytes]byte
var inputPosition, inputLength int

// Keep only a bounded refill buffer and the current token; Read may return partial data.
// Refill a fixed byte buffer; EOF is separate from every possible input byte.

// Read the single input stream once and convert tokens without fmt reflection.
// Parse decimal input directly to avoid fmt's reflection and token allocations.
func integer() int {
	position, length := inputPosition, inputLength
	for {
		for position < length && inputBuffer[position] <= ' ' {
			position++
		}
		if position < length {
			break
		}
		length, _ = syscall.Read(syscall.Stdin, inputBuffer[:])
		position = 0
		if length == 0 {
			inputPosition, inputLength = 0, 0
			return 0
		}
	}
	negative := inputBuffer[position] == '-'
	if negative || inputBuffer[position] == '+' {
		position++
	}
	value := 0
	for {
		// Keep the cursor local until the number ends or the current block is exhausted.
		for position < length {
			ch := inputBuffer[position]
			if ch < '0' || ch > '9' {
				inputPosition, inputLength = position, length
				if negative {
					return value
				}
				return -value
			}
			value = value*10 - int(ch-'0')
			position++
		}
		length, _ = syscall.Read(syscall.Stdin, inputBuffer[:])
		position = 0
		if length == 0 {
			inputPosition, inputLength = 0, 0
			if negative {
				return value
			}
			return -value
		}
	}
}

// Reuse one output buffer; io.Writer cannot retain it after Write returns.
func writeBytes(data []byte) {
	for len(data) > 0 {
		count, err := syscall.Write(syscall.Stdout, data)
		if count > 0 {
			data = data[count:]
		}
		if err != nil || count == 0 {
			return
		}
	}
}
