package main

import (
	"io"
)

import (
	"os"
)

const three = 3

func main() {
	n, m := integer(), integer()
	// every dark region is a rectangle exactly when no 2 x 2 window holds
	// three dark cells. Two rows avoid a full byte-per-pixel image,
	// which can exceed 4 MB at the maximum dimensions.
	prev, cur := make([]byte, m), make([]byte, m)
	for i := 0; i < n; i++ {
		pixelRow(cur)
		if i > 0 {
			for j := 1; j < m; j++ {
				if prev[j-1]+prev[j]+cur[j-1]+cur[j] == three {
					fastPrint(os.Stdout, true, true, "No")
					return
				}
			}
		}

		prev, cur = cur, prev
	}
	fastPrint(os.Stdout, true, true, "Yes")
}

// Decode each available input block directly, then inspect adjacent row cells.
func pixelRow(row []byte) {
	filled := 0
	for filled < len(row) {
		if inputPosition == inputLength {
			if nextByte() < 0 {
				panic("incomplete image")
			}
			inputPosition--
		}
		position := inputPosition
		for position < inputLength && filled < len(row) {
			ch := inputBuffer[position]
			position++
			if ch == '0' || ch == '1' {
				row[filled] = ch - '0'
				filled++
			}
		}
		inputPosition = position
	}
}

var fastOutputBuffer = make([]byte, 0, 64)

// Reuse one output buffer; io.Writer cannot retain it after Write returns.
func fastPrint(writer io.Writer, spaced, newline bool, values ...interface{}) (int, error) {
	buffer := fastOutputBuffer[:0]
	previousString := false
	for index, value := range values {
		_, isString := value.(string)
		if index > 0 && (spaced || (!previousString && !isString)) {
			buffer = append(buffer, ' ')
		}
		switch value := value.(type) {
		case string:
			buffer = append(buffer, value...)

		default:
			panic("unsupported output type")
		}
		previousString = isString
	}
	if newline {
		buffer = append(buffer, '\n')
	}
	fastOutputBuffer = buffer
	return writer.Write(buffer)
}

const inputBufferBytes = 8192

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

// Parse decimal input directly to avoid fmt's reflection and token allocations.
func integer() int {
	ch := nextByte()
	for ch >= 0 && ch <= ' ' {
		ch = nextByte()
	}
	value := 0
	for ch >= '0' && ch <= '9' {
		value = value*10 + ch - '0'
		ch = nextByte()
	}
	if ch >= 0 {
		inputPosition--
	}
	return value
}
