package main

import (
	"os"
	"strconv"
)

const (
	inputSize  = 4096
	outputSize = 16
	decimal    = 10
)

func main() {
	var input [inputSize]byte
	balance, lowest, count := 0, 0, 0
	for {
		size, _ := os.Stdin.Read(input[:])
		if size == 0 {
			break
		}
		for _, ch := range input[:size] {
			switch ch {
			case '(':
				balance++
			case ')':
				balance--
			default:
				continue
			}
			if balance < lowest {
				lowest, count = balance, 1
			} else if balance == lowest {
				count++
			}
		}
	}
	if balance != 0 {
		count = 0
	}
	var output [outputSize]byte
	line := strconv.AppendInt(output[:0], int64(count), decimal)
	os.Stdout.Write(append(line, '\n'))
}
