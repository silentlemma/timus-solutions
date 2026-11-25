package main

import (
	"syscall"
)

const (
	whole = 10000
	none  = -1
)

func main() {
	n := integer()
	low, high, previous, unknown := 0, 0, whole, 0
	// shares never grow down the list, so an unknown share is at least the
	// next given one (or 1) and at most the last given one before it (or
	// 100%); every total between the two extremes can be reached
	for i := 0; i < n; i++ {
		skipToken()
		shown := integer()
		if shown == 1 {
			value := integer()
			low += (unknown + 1) * value
			high += unknown*previous + value
			previous = value
			unknown = 0
			// Later ingredients cannot reduce this accumulated lower bound.
			if low > whole {
				writeBytes([]byte("NO\n"))
				syscall.Exit(0)
			}
		} else {
			unknown++
		}
	}
	low += unknown
	high += unknown * previous
	if low <= whole && whole <= high {
		writeBytes([]byte("YES\n"))
	} else {
		writeBytes([]byte("NO\n"))
	}
	syscall.Exit(0)
}

const inputBufferBytes = 32768

var inputBuffer [inputBufferBytes]byte
var inputPosition, inputLength int

// Keep only a bounded refill buffer and the current token; Read may return partial data.
// Refill a fixed byte buffer; EOF is separate from every possible input byte.
func nextByte() int {
	if inputPosition == inputLength {
		inputLength, _ = syscall.Read(syscall.Stdin, inputBuffer[:])
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
	// Keep the cursor local until the number ends or the current block is exhausted.
	position, length := inputPosition, inputLength
	started, value := false, 0
	for {
		for position < length {
			ch := inputBuffer[position]
			position++
			if ch >= '0' && ch <= '9' {
				value = value*10 + int(ch-'0')
				started = true
			} else if started {
				inputPosition, inputLength = position, length
				return value
			}
		}
		length, _ = syscall.Read(syscall.Stdin, inputBuffer[:])
		position = 0
		if length == 0 {
			inputPosition, inputLength = 0, 0
			return value
		}
	}
}

func skipToken() {
	ch := nextByte()
	for ch >= 0 && ch <= ' ' {
		ch = nextByte()
	}
	for ch > ' ' {
		ch = nextByte()
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
