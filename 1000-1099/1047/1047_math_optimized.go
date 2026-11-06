package main

import "os"

const (
	cents      = 100
	inputSize  = 64
	outputSize = 32
	maxDigits  = 20
)

var (
	input         [inputSize]byte
	inputPosition int
	inputLength   int
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

func scaledNumber() int64 {
	c := nextByte()
	for c != 0 && c <= ' ' {
		c = nextByte()
	}
	negative := c == '-'
	if negative || c == '+' {
		c = nextByte()
	}
	var value int64
	// Removing the point preserves N and scales two-decimal values to cents.
	for c >= '0' && c <= '9' || c == '.' {
		if c != '.' {
			value = value*10 + int64(c-'0')
		}
		c = nextByte()
	}
	if negative {
		return -value
	}
	return value
}

func appendInteger(output []byte, value int64) []byte {
	var digits [maxDigits]byte
	position := len(digits)
	for {
		position--
		digits[position] = '0' + byte(value%10)
		value /= 10
		if value == 0 {
			break
		}
	}
	return append(output, digits[position:]...)
}

func main() {
	n := scaledNumber()
	first, last := scaledNumber(), scaledNumber()
	var weighted int64
	for weight := n; weight > 0; weight-- {
		weighted += weight * scaledNumber()
	}
	num, den := n*first+last-2*weighted, n+1
	negative := num < 0
	if negative {
		num = -num
	}
	value := (2*num + den) / (2 * den)
	var storage [outputSize]byte
	output := storage[:0]
	if negative && value != 0 {
		output = append(output, '-')
	}
	output = appendInteger(output, value/cents)
	fraction := value % cents
	output = append(output, '.', '0'+byte(fraction/10), '0'+byte(fraction%10), '\n')
	os.Stdout.Write(output)
}
