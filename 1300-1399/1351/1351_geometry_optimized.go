package main

import (
	"bufio"
	"os"
)

const inputSize = 4096
const outputSize = 8192
const wordReserve = 4

type input struct {
	stream           *bufio.Reader
	bytes            [inputSize]byte
	position, length int
}

func (in *input) next() byte {
	if in.position == in.length {
		in.length, _ = in.stream.Read(in.bytes[:])
		in.position = 0
		if in.length == 0 {
			return 0
		}
	}
	c := in.bytes[in.position]
	in.position++
	return c
}

func (in *input) number() int32 {
	c := in.next()
	for c != 0 && c <= ' ' {
		c = in.next()
	}
	negative := c == '-'
	if negative {
		c = in.next()
	}
	value := int32(0)
	for c >= '0' && c <= '9' {
		value = value*10 + int32(c-'0')
		c = in.next()
	}
	if negative {
		return -value
	}
	return value
}

func main() {
	in := input{stream: bufio.NewReaderSize(os.Stdin, inputSize)}
	reach, rx, ry := in.number(), in.number(), in.number()
	lx, ly, n := in.number(), in.number(), in.number()
	radiusSquared := reach * reach
	var output [outputSize]byte
	used := 0
	for i := int32(0); i < n; i++ {
		x, y := in.number(), in.number()
		right, left := rx*y-ry*x, x*ly-y*lx
		behind := (right == 0 && rx*x+ry*y < 0) || (left == 0 && lx*x+ly*y < 0)
		hit := right >= 0 && left >= 0 && !behind && x*x+y*y <= radiusSquared
		word := "NO\n"
		if hit {
			word = "YES\n"
		}
		used += copy(output[used:], word)
		if used+wordReserve > len(output) {
			os.Stdout.Write(output[:used])
			used = 0
		}
	}
	os.Stdout.Write(output[:used])
}
