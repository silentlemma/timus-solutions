package main

import (
	"os"
	"strconv"
)

const outputSize = 8192
const numberReserve = 16

var output = make([]byte, 0, outputSize)
var first = true

func flush() {
	remaining := output
	for len(remaining) > 0 {
		count, err := os.Stdout.Write(remaining)
		remaining = remaining[count:]
		if err != nil || count == 0 {
			break
		}
	}
	output = output[:0]
}

func number(value int) {
	if len(output)+numberReserve >= cap(output) {
		flush()
	}
	if !first {
		output = append(output, ' ')
	}
	first = false
	output = strconv.AppendInt(output, int64(value), 10)
}

func line() {
	output = append(output, '\n')
	first = true
}

const inputSize = 4096

type input struct {
	bytes            [inputSize]byte
	position, length int
}

func (in *input) next() byte {
	if in.position == in.length {
		in.length, _ = os.Stdin.Read(in.bytes[:])
		in.position = 0
		if in.length == 0 {
			return 0
		}
	}
	c := in.bytes[in.position]
	in.position++
	return c
}

func (in *input) number() int {
	c, value := in.next(), 0
	for c != 0 && c <= ' ' {
		c = in.next()
	}
	for c >= '0' && c <= '9' {
		value = value*10 + int(c-'0')
		c = in.next()
	}
	return value
}

func main() {
	var in input
	n, r := in.number(), uint32(in.number())
	sizes := make([]uint32, n)
	for i := range sizes {
		sizes[i] = uint32(in.number())
	}
	trips, left := 0, 0
	for right := range sizes {
		for sizes[right]-sizes[left] > r {
			left++
		}
		if right-left+1 > trips {
			trips = right - left + 1
		}
	}
	number(trips)
	line()
	// A width-r window contains at most trips coats, so stride trips separates every pair.
	for trip := 0; trip < trips; trip++ {
		number((n - trip + trips - 1) / trips)
		for coat := trip + 1; coat <= n; coat += trips {
			number(coat)
		}
		line()
	}
	flush()
}
