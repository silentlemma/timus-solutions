package main

import "os"

const (
	maxColumns = 100
	inputSize  = 1024
	outputSize = 1024
	maxDigits  = 4 // At most 5000 bricks.
)

var input [inputSize]byte
var inputPosition, inputLength int
var output [outputSize]byte
var outputLength int

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

func number() int {
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
	first := len(digits)
	for {
		first--
		digits[first] = '0' + byte(value%10)
		value /= 10
		if value == 0 {
			break
		}
	}
	for ; first < len(digits); first++ {
		writeByte(digits[first])
	}
}

func main() {
	rows, cols := number(), number()
	var standing [maxColumns / 2]bool
	blocks := standing[:cols/2]
	for row := 0; row < rows; row += 2 {
		for col := range blocks {
			blocks[col] = number() == number()
		}
		for col := range blocks {
			left, right := number(), number()
			blocks[col] = blocks[col] || left == right
		}
		for offset := 0; offset < 2; offset++ {
			for col, vertical := range blocks {
				id := row*len(blocks) + 2*col + 1
				left, right := id+offset, id+offset
				if vertical {
					left, right = id, id+1
				}
				if col != 0 {
					writeByte(' ')
				}
				writeNumber(left)
				writeByte(' ')
				writeNumber(right)
			}
			writeByte('\n')
		}
	}
	os.Stdout.Write(output[:outputLength])
}
