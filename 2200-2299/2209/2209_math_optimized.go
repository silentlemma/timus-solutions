package main

import (
	"os"
	"strconv"
)

const (
	inputSize  = 64
	outputSize = 48
	decimal    = 10
)

func main() {
	var input [inputSize]byte
	var numbers [2]uint64
	index, reading := 0, false
	for index < len(numbers) {
		size, err := os.Stdin.Read(input[:])
		for _, c := range input[:size] {
			if '0' <= c && c <= '9' {
				numbers[index] = decimal*numbers[index] + uint64(c-'0')
				reading = true
			} else if reading {
				index++
				if index == len(numbers) {
					break
				}
				reading = false
			}
		}
		if err != nil || size == 0 {
			break
		}
	}
	left, right := uint64(1), uint64(1)
	leadingLeft := numbers[0] - 1
	// Follow the path backwards, tracking the coefficients of the two bounds.
	for path := numbers[1] - 1; path != 0; path >>= 1 {
		if path&1 == 0 {
			left += right
		} else {
			right += left
		}
		leadingLeft--
	}
	var buffer [outputSize]byte
	answer := strconv.AppendUint(buffer[:0], right, decimal)
	answer = append(answer, ' ')
	answer = strconv.AppendUint(answer, left+leadingLeft*right, decimal)
	answer = append(answer, '\n')
	os.Stdout.Write(answer)
}
