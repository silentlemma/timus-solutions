package main

import (
	"os"
)

const mod = 1000000007

func sequences(n, a, b int) int {
	if n == 0 {
		return 2
	}
	// one[i], two[i]: sequences of length i that end with a run of ones or twos,
	// the empty sequence counts once on both sides, so one[0] = two[0] = 1
	// the last run of ones has length 1..a and follows a sequence ending in twos

	// Eliminate the conceptual one/two states using their generating functions.
	// F(x) = (1-x^(a+1))(1-x^(b+1)) /
	//        (1-2*x+x^(a+2)+x^(b+2)-x^(a+b+2)); F counts the empty word once.

	// Only bounded delayed coefficients are needed, so keep a ring of residues.
	capacity := a + b + 3
	if capacity > n+1 {
		capacity = n + 1
	}
	values := make([]uint32, capacity)
	values[0] = 1
	indexA := (capacity - (a+1)%capacity) % capacity
	indexB := (capacity - (b+1)%capacity) % capacity
	indexC := (capacity - (a+b+1)%capacity) % capacity
	position, previous := 1%capacity, int64(1)
	for i := 1; i <= n; i++ {
		value := 2 * previous
		if i >= a+2 {
			value -= int64(values[indexA])
		}
		if i >= b+2 {
			value -= int64(values[indexB])
		}
		if i >= a+b+2 {
			value += int64(values[indexC])
		}
		if i == a+1 {
			value--
		}
		if i == b+1 {
			value--
		}
		if i == a+b+2 {
			value++
		}
		value %= mod
		if value < 0 {
			value += mod
		}
		values[position] = uint32(value)
		previous = value
		position++
		if position == capacity {
			position = 0
		}
		indexA++
		if indexA == capacity {
			indexA = 0
		}
		indexB++
		if indexB == capacity {
			indexB = 0
		}
		indexC++
		if indexC == capacity {
			indexC = 0
		}
	}
	return int(previous)
}

func main() {
	n, a, b := integer(), integer(), integer()
	writeInteger(sequences(n, a, b))
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
func writeInteger(value int) {
	var bytes [24]byte
	out := appendInteger(bytes[:0], int64(value))
	out = append(out, '\n')
	writeBytes(out)
}
