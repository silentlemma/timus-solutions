package main

import (
	"bufio"
	"os"
	"strconv"
)

const (
	maxVertex  = 10000
	bufferSize = 4096
	lineSize   = 8
	decimal    = 10
)

func nextInt(input *bufio.Scanner) int {
	input.Scan()
	value, _ := strconv.Atoi(input.Text())
	return value
}

func main() {
	input := bufio.NewScanner(os.Stdin)
	var buffer [bufferSize]byte
	input.Buffer(buffer[:], len(buffer))
	input.Split(bufio.ScanWords)
	chain := make([]uint16, nextInt(input))
	for i := range chain {
		chain[i] = uint16(nextInt(input))
	}
	finish := chain[len(chain)-1]
	var jump []uint32
	if chain[0] != finish {
		jump = make([]uint32, len(chain))
		var best [maxVertex + 1]uint16
		var nextAt [maxVertex + 1]uint32
		for vertex := range best {
			best[vertex] = maxVertex
		}
		var suffixDistance uint16
		for i := len(chain) - 2; i >= 0; i-- {
			vertex := chain[i]
			if suffixDistance < best[vertex] {
				best[vertex], nextAt[vertex] = suffixDistance, uint32(i+1)
			}
			jump[i] = nextAt[vertex]
			if vertex == finish {
				suffixDistance = 0
			} else {
				suffixDistance = best[vertex] + 1
			}
		}
	}
	output := bufio.NewWriter(os.Stdout)
	var digits [lineSize]byte
	for i := uint32(0); ; i = jump[i] {
		output.Write(strconv.AppendUint(digits[:0], uint64(chain[i]), decimal))
		if chain[i] == finish {
			break
		}
		output.WriteByte(' ')
	}
	output.WriteByte('\n')
	output.Flush()
}
