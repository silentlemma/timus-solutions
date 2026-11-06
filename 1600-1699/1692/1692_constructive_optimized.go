package main

import "os"

const (
	inputSize  = 16
	outputSize = 1024
	maxDigits  = 16
)

var (
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

func nextInt() int {
	c := nextByte()
	for c != 0 && c <= ' ' {
		c = nextByte()
	}
	value := 0
	for c >= '0' && c <= '9' {
		value = value*10 + int(c-'0')
		c = nextByte()
	}
	return value
}

func writeByte(value byte) {
	if outputLength == len(output) {
		os.Stdout.Write(output[:])
		outputLength = 0
	}
	output[outputLength] = value
	outputLength++
}

func writeNumber(value int) {
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
	for ; position < len(digits); position++ {
		writeByte(digits[position])
	}
}

func main() {
	n := nextInt()
	flags := 1
	for flags*(flags+1)/2 <= n {
		flags++
	}
	writeNumber(flags)
	writeByte('\n')
	for flag := 0; flag < flags; flag++ {
		writeNumber(flags - 1)
		for other := 0; other < flags; other++ {
			if other == flag {
				continue
			}
			a, b := flag, other
			if a > b {
				a, b = b, a
			}
			// Count earlier pairs, then locate this pair within row a.
			colour := a*(2*flags-a-1)/2 + b - a
			writeByte(' ')
			writeNumber(colour)
		}
		writeByte('\n')
	}
	os.Stdout.Write(output[:outputLength])
}
