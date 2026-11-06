package main

import (
	"bufio"
	"os"
	"strconv"
)

const (
	inputSize = 16384
	lineSize  = 16
	decimal   = 10
)

func nextByte(input *bufio.Reader) byte {
	for {
		ch, err := input.ReadByte()
		if err != nil {
			return 0
		}
		if ch > ' ' {
			return ch
		}
	}
}

func nextInt(input *bufio.Reader) int {
	value := 0
	ch := nextByte(input)
	for ch >= '0' && ch <= '9' {
		value = value*decimal + int(ch-'0')
		ch, _ = input.ReadByte()
	}
	return value
}

func main() {
	input := bufio.NewReaderSize(os.Stdin, inputSize)
	size, start := nextInt(input), nextInt(input)
	incoming := make([][]uint16, size+1)
	missing := 0
	for from := 1; from <= size; from++ {
		for to := 1; to <= size; to++ {
			if nextByte(input) == '0' && from != to {
				incoming[to] = append(incoming[to], uint16(from))
				missing++
			}
		}
	}

	// Traverse reversed channels so Hierholzer's pop order gives the forward route.
	stack := make([]uint16, 1, missing+1)
	stack[0] = uint16(start)
	output := bufio.NewWriter(os.Stdout)
	var buffer [lineSize]byte
	var previous uint16
	for len(stack) != 0 {
		city := stack[len(stack)-1]
		edges := incoming[city]
		if len(edges) != 0 {
			stack = append(stack, edges[len(edges)-1])
			incoming[city] = edges[:len(edges)-1]
			continue
		}
		if previous != 0 {
			line := strconv.AppendUint(buffer[:0], uint64(previous), decimal)
			line = append(line, ' ')
			line = strconv.AppendUint(line, uint64(city), decimal)
			output.Write(append(line, '\n'))
		}
		previous = city
		stack = stack[:len(stack)-1]
	}
	output.Flush()
}
