package main

import "os"

const (
	fixed       = 153
	decimalBase = 10
	inputSize   = 4096
	outputSize  = 8192
	digitsSize  = 20
)

var (
	cubes         = [decimalBase]int{0, 1, 8, 27, 64, 125, 216, 343, 512, 729}
	input         [inputSize]byte
	inputPosition int
	inputLength   int
	output        [outputSize]byte
	outputLength  int
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

func number() int64 {
	c := nextByte()
	for c <= ' ' {
		c = nextByte()
	}
	var value int64
	for c > ' ' {
		value = decimalBase*value + int64(c-'0')
		c = nextByte()
	}
	return value
}

func writeByte(value byte) {
	output[outputLength] = value
	outputLength++
	if outputLength == len(output) {
		os.Stdout.Write(output[:])
		outputLength = 0
	}
}

func writeNumber(value int64) {
	if value < 0 {
		writeByte('-')
		value = -value
	}
	var digits [digitsSize]byte
	position := len(digits)
	for {
		position--
		digits[position] = '0' + byte(value%decimalBase)
		value /= decimalBase
		if value == 0 {
			break
		}
	}
	for _, digit := range digits[position:] {
		writeByte(digit)
	}
	writeByte('\n')
}

func cubeSum(value int) int {
	sum := 0
	for value != 0 {
		sum += cubes[value%decimalBase]
		value /= decimalBase
	}
	return sum
}

func main() {
	for queries := number(); queries > 0; queries-- {
		n, gap, offset := int(number()), int(number()), number()
		for step := 1; step < n && gap != fixed; step++ {
			gap = cubeSum(gap)
		}
		writeNumber(int64(gap) - offset)
	}
	if outputLength != 0 {
		os.Stdout.Write(output[:outputLength])
	}
}
