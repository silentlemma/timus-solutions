package main

import (
	"os"
)

const mod = 1000000000

func countDecreasing(flipped []uint32, k int) int64 {
	n := len(flipped)
	if k == 1 {
		return int64(n)
	}
	// ends[i]: decreasing runs of the current length that end at position i
	ends := make([]uint32, n)
	tree := make([]uint32, n+1)
	for i := range ends {
		ends[i] = 1
	}
	for length := 2; length <= k; length++ {
		for i := range tree {
			tree[i] = 0
		}
		for i, v := range flipped {
			previous := ends[i]
			// the runs one shorter that end earlier at a larger value
			sum := uint32(0)
			for j := int(v) - 1; j > 0; j &= j - 1 {
				sum += tree[j]
				if sum >= mod {
					sum -= mod
				}
			}
			ends[i] = sum
			for j := int(v); j <= n; j += j & -j {
				tree[j] += previous
				if tree[j] >= mod {
					tree[j] -= mod
				}
			}
		}
	}
	total := uint32(0)
	for _, value := range ends {
		total += value
		if total >= mod {
			total -= mod
		}
	}
	return int64(total)
}

func main() {
	n, k := integer(), integer()
	// count values from the top, so that "larger" becomes a prefix
	flipped := make([]uint32, n)
	for i := range flipped {
		value := integer()
		flipped[i] = uint32(n + 1 - value)
	}
	writeInteger(int(countDecreasing(flipped, k)))
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
func writeInteger(value int) {
	var bytes [24]byte
	out := appendInteger(bytes[:0], int64(value))
	out = append(out, '\n')
	writeBytes(out)
}
