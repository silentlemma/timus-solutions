package main

import (
	"bufio"
	"io"
	"math"
	"os"
	"strconv"
)

const (
	lineBytes      = 24
	roundingOffset = 0.5
	maxInput       = 256 * 1024
	scale          = 10000
)

func main() {
	input := make([]byte, maxInput)
	end, _ := io.ReadFull(os.Stdin, input)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	line := make([]byte, 0, lineBytes)
	// the numbers are parsed from the end of the input backwards, so they come
	// out in the required order without a slice of them
	for end > 0 {
		for end > 0 && input[end-1] <= ' ' {
			end--
		}
		start := end
		for start > 0 && input[start-1] > ' ' {
			start--
		}
		if start == end {
			break
		}
		var value uint64
		for _, digit := range input[start:end] {
			value = value*10 + uint64(digit-'0')
		}
		// four decimals by hand: the root times 10^4, rounded, written as the
		// integer part and the fraction
		scaled := uint64(math.Sqrt(float64(value))*scale + roundingOffset)
		line = strconv.AppendUint(line[:0], scaled/scale, 10)
		line = append(line, '.')
		fraction := scaled % scale
		for divisor := uint64(scale / 10); divisor > 0; divisor /= 10 {
			line = append(line, byte(fraction/divisor)+'0')
			fraction %= divisor
		}
		line = append(line, '\n')
		writer.Write(line)
		end = start
	}
}
