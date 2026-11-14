package main

import (
	"bufio"
	"os"
	"strconv"
)

const percent = 100
const periodsPerBlock = 80

func main() {
	input := bufio.NewScanner(os.Stdin)
	input.Split(bufio.ScanWords)
	input.Scan()
	count, _ := strconv.Atoi(input.Text())
	input.Scan()
	brightness, _ := strconv.Atoi(input.Text())

	var block [percent * periodsPerBlock]byte
	// The fractional remainder returns to zero after one full period.
	remainder := 0
	for i := 0; i < percent; i++ {
		remainder += brightness
		block[i] = '0'
		if remainder >= percent {
			block[i] = '1'
			remainder -= percent
		}
	}
	for length := percent; length < len(block); {
		length += copy(block[length:], block[:length])
	}
	for count >= len(block) {
		os.Stdout.Write(block[:])
		count -= len(block)
	}
	os.Stdout.Write(block[:count])
	os.Stdout.WriteString("\n")
}
