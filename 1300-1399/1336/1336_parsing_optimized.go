package main

import (
	"os"
)

func main() {
	n := int64(integer())
	// (n^2)^2 = n^4 = n^3 * n
	var bytes [48]byte
	out := appendInteger(bytes[:0], n*n)
	out = append(out, '\n')
	out = appendInteger(out, n)
	out = append(out, '\n')
	writeBytes(out)
}

const inputBufferBytes = 256

var inputBuffer [inputBufferBytes]byte
var inputPosition, inputLength int

// Keep only a bounded refill buffer and the current token; Read may return partial data.
// Refill a fixed byte buffer; EOF is separate from every possible input byte.
func nextByte() int {
	if inputPosition == inputLength {
		inputLength, _ = os.Stdin.Read(inputBuffer[:])
		inputPosition = 0
		if inputLength == 0 {
			return -1
		}
	}
	ch := inputBuffer[inputPosition]
	inputPosition++
	return int(ch)
}

// Read the single input stream once and convert tokens without fmt reflection.
// Parse decimal input directly to avoid fmt's reflection and token allocations.
func integer() int {
	position, length := inputPosition, inputLength
	read := func() int {
		if position == length {
			inputPosition = position
			ch := nextByte()
			position, length = inputPosition, inputLength
			return ch
		}
		ch := int(inputBuffer[position])
		position++
		return ch
	}
	ch := read()
	for ch >= 0 && ch <= ' ' {
		ch = read()
	}
	negative := ch == '-'
	if negative || ch == '+' {
		ch = read()
	}
	value := 0
	for ch >= '0' && ch <= '9' {
		if negative {
			value = value*10 - (ch - '0')
		} else {
			value = value*10 + ch - '0'
		}
		ch = read()
	}
	if ch >= 0 {
		position--
	}
	inputPosition = position
	return value
}

// Reuse one output buffer; io.Writer cannot retain it after Write returns.
func writeBytes(data []byte) {
	for len(data) > 0 {
		count, err := os.Stdout.Write(data)
		if count > 0 {
			data = data[count:]
		}
		if err != nil || count == 0 {
			return
		}
	}
}
func appendInteger(out []byte, value int64) []byte {
	var buffer [24]byte
	at := len(buffer)
	negative := value < 0
	var magnitude uint64
	if negative {
		magnitude = uint64(-(value + 1)) + 1
	} else {
		magnitude = uint64(value)
	}
	for {
		at--
		buffer[at] = byte('0' + magnitude%10)
		magnitude /= 10
		if magnitude == 0 {
			break
		}
	}
	if negative {
		at--
		buffer[at] = '-'
	}
	return append(out, buffer[at:]...)
}
