package main

import "os"

const (
	maxSide      = 150
	reach        = 5
	diamondSides = 4
	stride       = maxSide + 2*reach
	inputSize    = 4096
	outputSize   = 8192
	digitsSize   = 16
	decimalBase  = 10
)

var (
	input         [inputSize]byte
	inputPosition int
	inputLength   int
	output        [outputSize]byte
	outputLength  int
	grid          [stride * stride]uint16
	rings         [reach][diamondSides * reach]int16
	ringCounts    [reach]int
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

func number() int {
	c := nextByte()
	for c <= ' ' {
		c = nextByte()
	}
	value := 0
	for c > ' ' {
		value = decimalBase*value + int(c-'0')
		c = nextByte()
	}
	return value
}

func abs(value int) int {
	if value < 0 {
		return -value
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

func writeNumber(value int) {
	if value == 0 {
		writeByte('0')
		return
	}
	var digits [digitsSize]byte
	position := len(digits)
	for value != 0 {
		position--
		digits[position] = '0' + byte(value%decimalBase)
		value /= decimalBase
	}
	for _, digit := range digits[position:] {
		writeByte(digit)
	}
}

func main() {
	height, width := number(), number()
	for row := reach; row < height+reach; row++ {
		for col := reach; col < width+reach; col++ {
			grid[row*stride+col] = uint16(number())
		}
	}
	for distance := 1; distance <= reach; distance++ {
		count := 0
		for row := -distance; row <= distance; row++ {
			col := distance - abs(row)
			rings[distance-1][count] = int16(row*stride + col)
			count++
			if col != 0 {
				rings[distance-1][count] = int16(row*stride - col)
				count++
			}
		}
		ringCounts[distance-1] = count
	}
	for row := reach; row < height+reach; row++ {
		for col := reach; col < width+reach; col++ {
			if col != reach {
				writeByte(' ')
			}
			cell := row*stride + col
			if grid[cell] != 0 {
				writeByte('-')
				writeByte('1')
				continue
			}
			var mask uint16
			for ring := 0; ring < reach; ring++ {
				for _, offset := range rings[ring][:ringCounts[ring]] {
					mask |= grid[cell+int(offset)]
				}
				if mask != 0 {
					break
				}
			}
			writeNumber(int(mask))
		}
		writeByte('\n')
	}
	if outputLength != 0 {
		os.Stdout.Write(output[:outputLength])
	}
}
