package main

import (
	"math/bits"
	"os"
)

const (
	maxDigits = 100
	limbBits  = 64
	inputSize = 16
)

type wordPair struct{ high, low uint64 }

var (
	input         [inputSize]byte
	inputPosition int
	inputLength   int
	answer        [maxDigits + 1]byte
)

func nextByte() byte {
	if inputPosition == inputLength {
		inputLength, _ = os.Stdin.Read(input[:])
		inputPosition = 0
		if inputLength == 0 {
			return 0
		}
	}
	value := input[inputPosition]
	inputPosition++
	return value
}

func (a wordPair) add(b wordPair) wordPair {
	low, carry := bits.Add64(a.low, b.low, 0)
	return wordPair{a.high + b.high + carry, low}
}

func (a wordPair) timesTen() wordPair {
	high, low := bits.Mul64(a.low, 10)
	return wordPair{a.high*10 + high, low}
}

func (a wordPair) bit(index int) uint64 {
	if index < limbBits {
		return (a.low >> uint(index)) & 1
	}
	return (a.high >> uint(index-limbBits)) & 1
}

func main() {
	c := nextByte()
	for c != 0 && c <= ' ' {
		c = nextByte()
	}
	n := 0
	for c >= '0' && c <= '9' {
		n = 10*n + int(c-'0')
		c = nextByte()
	}
	var value wordPair
	power := wordPair{low: 1}
	for k := 0; k < n; k++ {
		// The lower k bits are already zero. Bit k decides the new digit.
		value = value.add(power)
		digit := byte('1')
		if value.bit(k) != 0 {
			value = value.add(power)
			digit = '2'
		}
		answer[n-k-1] = digit
		power = power.timesTen()
	}
	answer[n] = '\n'
	os.Stdout.Write(answer[:n+1])
}
