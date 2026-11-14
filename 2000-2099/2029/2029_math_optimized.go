package main

import (
	"io"
	"os"
)

const (
	maxDisks  = 50
	maxInput  = 2*maxDisks + 16
	maxOutput = 17 // 2^50 - 1 occupies 16 digits, plus a newline.
	decimal   = 10
	pegSum    = 'A' + 'B' + 'C'
)

func main() {
	var input [maxInput]byte
	n, _ := io.ReadFull(os.Stdin, input[:])
	// The count is redundant: only the peg labels determine the distance.
	source := byte('A')
	var answer uint64
	for i := n - 1; i >= 0; i-- {
		target := input[i]
		if target < 'A' || target > 'C' {
			continue
		}
		answer <<= 1
		if target != source {
			answer++
			source = byte(pegSum - int(source) - int(target))
		}
	}
	var output [maxOutput]byte
	start := len(output) - 1
	output[start] = '\n'
	for {
		start--
		output[start] = '0' + byte(answer%decimal)
		answer /= decimal
		if answer == 0 {
			break
		}
	}
	os.Stdout.Write(output[start:])
}
