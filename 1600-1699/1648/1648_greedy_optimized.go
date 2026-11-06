package main

import "os"

const (
	outputSize = 32
)

const (
	maxMonths  = 20000
	bufferSize = 4096
	decimal    = 10
)

var sales [maxMonths]int32

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

func digits(output []byte, end int, value int64) int {
	for {
		end--
		output[end] = '0' + byte(value%decimal)
		value /= decimal
		if value == 0 {
			return end
		}
	}
}

func main() {
	var input reader
	n, capacity := int(input.number()), input.number()
	var total, limit int32
	for i := 0; i < n; i++ {
		limit += capacity
		next := total + input.number()
		if next > limit {
			next = limit
		}
		sales[i] = next - total
		total = next
	}
	// The cumulative storage cost can exceed 32 bits even though sales cannot.
	var carry, storage int64
	for i := n - 1; i >= 0; i-- {
		storage += carry
		carry += int64(sales[i] - capacity)
		if carry < 0 {
			carry = 0
		}
	}
	var output [outputSize]byte
	end := len(output) - 1
	output[end] = '\n'
	end = digits(output[:], end, storage)
	end--
	output[end] = ' '
	end = digits(output[:], end, int64(total))
	os.Stdout.Write(output[end:])
}
