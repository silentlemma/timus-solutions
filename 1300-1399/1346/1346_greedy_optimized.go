package main

import (
	"bufio"
	"os"
	"strconv"
)

const (
	inputSize  = 4096
	outputSize = 24
	decimal    = 10
)

func nextInt(input *bufio.Scanner) int {
	input.Scan()
	value, _ := strconv.Atoi(input.Text())
	return value
}

func main() {
	input := bufio.NewScanner(os.Stdin)
	var buffer [inputSize]byte
	input.Buffer(buffer[:], len(buffer))
	input.Split(bufio.ScanWords)
	start, end := nextInt(input), nextInt(input)
	previous := nextInt(input)
	pieces, direction := 1, 0
	for index := start; index < end; index++ {
		value := nextInt(input)
		step := 0
		if value > previous {
			step = 1
		} else if value < previous {
			step = -1
		}
		if direction == 0 {
			direction = step
		} else if step != 0 && step != direction {
			// A step across the cut does not fix the next piece's direction.
			pieces++
			direction = 0
		}
		previous = value
	}
	var output [outputSize]byte
	line := strconv.AppendInt(output[:0], int64(pieces), decimal)
	os.Stdout.Write(append(line, '\n'))
}
