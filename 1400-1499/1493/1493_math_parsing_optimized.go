package main

import (
	"os"
)

const (
	half    = 1000
	tickets = 1000000
	base    = 10
)

func digitSum(n int) int {
	sum := 0
	for ; n > 0; n /= base {
		sum += n % base
	}
	return sum
}

func main() {
	// a leading zero must not turn the number octal, so read it as text
	number := integer()
	// the sums differ by one, so the ticket is neither 000000 nor 999999
	// and both neighbours are six-digit tickets
	yes := neighborLucky(number)
	if yes {
		writeBytes([]byte("Yes\n"))
	} else {
		writeBytes([]byte("No\n"))
	}
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

func neighborLucky(number int) bool {
	upper, lower := number/half, number%half
	left, right := digitSum(upper), digitSum(lower)
	if number+1 < tickets {
		if lower == half-1 {
			if digitSum(upper+1) == 0 {
				return true
			}
		} else {
			nines := 0
			for value := lower; value%base == base-1; value /= base {
				nines++
			}
			if left == right+1-(base-1)*nines {
				return true
			}
		}
	}
	if number > 0 {
		if lower == 0 {
			if digitSum(upper-1) == 3*(base-1) {
				return true
			}
		} else {
			zeros := 0
			for value := lower; value%base == 0; value /= base {
				zeros++
			}
			if left == right-1+(base-1)*zeros {
				return true
			}
		}
	}
	return false
}
