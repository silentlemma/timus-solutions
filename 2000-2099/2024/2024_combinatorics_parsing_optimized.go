package main

import (
	"os"
)

func solve(text string, limit int) (int, int64) {
	const alphabet = 26
	counts := [alphabet]int{}
	for index := range text {
		counts[text[index]-'a']++
	}
	if limit == alphabet {
		return len(text), 1
	}
	if limit == 1 {
		largest, tied := 0, 0
		for _, count := range counts {
			if count > largest {
				largest = count
				tied = 1
			} else if count == largest {
				tied++
			}
		}
		if largest == 0 {
			return 0, 1
		}
		return largest, int64(tied)
	}
	for i := 1; i < len(counts); i++ {
		value, j := counts[i], i
		for j > 0 && counts[j-1] < value {
			counts[j] = counts[j-1]
			j--
		}
		counts[j] = value
	}
	size := 0
	for _, count := range counts[:limit] {
		size += count
	}
	boundary := counts[limit-1]
	if boundary == 0 {
		return size, 1
	}
	greater, tied := 0, 0
	for _, count := range counts {
		if count > boundary {
			greater++
		}
		if count == boundary {
			tied++
		}
	}
	chosen := limit - greater
	if tied-chosen < chosen {
		chosen = tied - chosen
	}
	ways := int64(1)
	for index := 1; index <= chosen; index++ {
		ways = ways * int64(tied-index+1) / int64(index)
	}
	return size, ways
}

func main() {
	text := token()
	limit := integer()
	size, ways := solve(text, limit)
	var bytes [48]byte
	out := appendInteger(bytes[:0], int64(size))
	out = append(out, ' ')
	out = appendInteger(out, ways)
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

func token() string {
	ch := nextByte()
	for ch >= 0 && ch <= ' ' {
		ch = nextByte()
	}
	var bytes []byte
	for ch > ' ' {
		bytes = append(bytes, byte(ch))
		ch = nextByte()
	}
	return string(bytes)
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
