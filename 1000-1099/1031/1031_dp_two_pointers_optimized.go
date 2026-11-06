package main

import "os"

const (
	outputSize      = 16
	unreachableCost = int32(2_000_000_000)
)

const (
	maxStations = 10000
	bufferSize  = 4096
	kinds       = 3
	decimal     = 10
)

var distance, cost [maxStations]int32

type reader struct {
	buffer [bufferSize]byte
	pos    int
	size   int
}

func (in *reader) nextByte() byte {
	if in.pos == in.size {
		in.size, _ = os.Stdin.Read(in.buffer[:])
		in.pos = 0
		if in.size == 0 {
			return 0
		}
	}
	c := in.buffer[in.pos]
	in.pos++
	return c
}

func (in *reader) number() int32 {
	c := in.nextByte()
	for c != 0 && c <= ' ' {
		c = in.nextByte()
	}
	var value int32
	for c >= '0' && c <= '9' {
		value = decimal*value + int32(c-'0')
		c = in.nextByte()
	}
	return value
}

func main() {
	var input reader
	var reach, price [kinds]int32
	for i := range reach {
		reach[i] = input.number()
	}
	for i := range price {
		price[i] = input.number()
	}
	input.number() // station count
	a, b := input.number(), input.number()
	if a > b {
		a, b = b, a
	}
	var start int32
	for station := int32(2); station <= a; station++ {
		start = input.number()
	}
	distance[0] = start
	count := int(b - a + 1)
	var from [kinds]int
	for i := 1; i < count; i++ {
		distance[i] = input.number()
		// Every prefix costs at most the final answer, bounded by 10^9.
		// Adding one fare therefore still fits in signed 32-bit arithmetic.
		best := unreachableCost
		for k := range from {
			for distance[i]-distance[from[k]] > reach[k] {
				from[k]++
			}
			if from[k] < i {
				candidate := cost[from[k]] + price[k]
				if candidate < best {
					best = candidate
				}
			}
		}
		cost[i] = best
	}
	answer := cost[count-1]
	var output [outputSize]byte
	pos := len(output) - 1
	output[pos] = '\n'
	for {
		pos--
		output[pos] = '0' + byte(answer%decimal)
		answer /= decimal
		if answer == 0 {
			break
		}
	}
	os.Stdout.Write(output[pos:])
}
