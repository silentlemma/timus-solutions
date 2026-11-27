package main

import (
	"os"
)

const percent = 100

const limbBase uint64 = 1000000000

type natural []uint32

func naturalFrom(value int64) natural {
	var result natural
	for value > 0 {
		result = append(result, uint32(value%int64(limbBase)))
		value /= int64(limbBase)
	}
	if len(result) == 0 {
		result = append(result, 0)
	}
	return result
}

func (value *natural) multiply(factor uint64) {
	carry := uint64(0)
	for i, limb := range *value {
		product := uint64(limb)*factor + carry
		(*value)[i] = uint32(product % limbBase)
		carry = product / limbBase
	}
	if carry != 0 {
		*value = append(*value, uint32(carry))
	}
	for len(*value) > 1 && (*value)[len(*value)-1] == 0 {
		*value = (*value)[:len(*value)-1]
	}
}

func (value natural) greater(other natural) bool {
	if len(value) != len(other) {
		return len(value) > len(other)
	}
	for i := len(value) - 1; i >= 0; i-- {
		if value[i] != other[i] {
			return value[i] > other[i]
		}
	}
	return false
}

func yearsUntil(gold, limit, fee int64) int {
	// after k years the gold is gold * ((100 - fee) / 100)^k exactly, so
	// compare gold * (100 - fee)^k with limit * 100^k in whole numbers
	left, right := naturalFrom(gold), naturalFrom(limit)
	keep, all := uint64(percent-fee), uint64(percent)
	// Cancel common factors before growing the exact integer products.
	a, b := keep, all
	for b != 0 {
		a, b = b, a%b
	}
	keep, all = keep/a, all/a
	years := 0
	for left.greater(right) {
		left.multiply(keep)
		right.multiply(all)
		years++
	}
	return years
}

func main() {
	gold, limit, fee := int64(integer()), int64(integer()), int64(integer())
	writeInteger(yearsUntil(gold, limit, fee))
}

const inputBufferBytes = 256
const outputBufferBytes = 24

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
	var buffer [outputBufferBytes]byte
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
	var bytes [outputBufferBytes]byte
	out := appendInteger(bytes[:0], int64(value))
	out = append(out, '\n')
	writeBytes(out)
}
