package main

import (
	"os"
)

// the exponents p of the first 38 Mersenne primes 2^p - 1 (OEIS A000043)
var exponents = []int{
	2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127, 521, 607, 1279, 2203, 2281, 3217, 4253,
	4423, 9689, 9941, 11213, 19937, 21701, 23209, 44497, 86243, 110503, 132049, 216091,
	756839, 859433, 1257787, 1398269, 2976221, 3021377, 6972593,
}

func main() {
	count := integer()
	const outputCapacity = 4096
	out := make([]byte, 0, outputCapacity)
	for i := 0; i < count; i++ {
		out = appendInteger(out, int64(exponents[integer()-1]))
		out = append(out, '\n')
		if len(out) > outputCapacity-24 {
			writeBytes(out)
			out = out[:0]
		}
	}
	writeBytes(out)
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
		length, _ = os.Stdin.Read(inputBuffer[:])
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
		length, _ = os.Stdin.Read(inputBuffer[:])
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
