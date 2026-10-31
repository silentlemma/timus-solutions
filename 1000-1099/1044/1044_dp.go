package main

import (
	"os"
	"strconv"
)

const bufferSize = 4096
const integerBufferSize = 32

type reader struct {
	data     [bufferSize]byte
	at, size int
}

func (in *reader) read() byte {
	if in.at == in.size {
		in.size, _ = os.Stdin.Read(in.data[:])
		in.at = 0
		if in.size == 0 {
			return 0
		}
	}
	c := in.data[in.at]
	in.at++
	return c
}

func (in *reader) integer() int64 {
	c := in.read()
	for c != 0 && c <= ' ' {
		c = in.read()
	}
	sign := int64(1)
	if c == '-' {
		sign = -1
		c = in.read()
	}
	value := int64(0)
	for c >= '0' && c <= '9' {
		value = value*10 + int64(c-'0')
		c = in.read()
	}
	return sign * value
}

func (in *reader) word() []byte {
	c := in.read()
	for c != 0 && c <= ' ' {
		c = in.read()
	}
	var result []byte
	for c > ' ' {
		result = append(result, c)
		c = in.read()
	}
	return result
}

func printInt(value int64) {
	var data [integerBufferSize]byte
	out := strconv.AppendInt(data[:0], value, 10)
	out = append(out, '\n')
	os.Stdout.Write(out)
}

const digits = 10

func main() {
	in := reader{}
	half := int(in.integer()) / 2
	ways := []int64{1}
	// Appending a digit convolves the counts with a window of ten ones.
	for step := 0; step < half; step++ {
		next := make([]int64, len(ways)+digits-1)
		var window int64
		for sum := range next {
			if sum < len(ways) {
				window += ways[sum]
			}
			if sum >= digits && sum-digits < len(ways) {
				window -= ways[sum-digits]
			}
			next[sum] = window
		}
		ways = next
	}
	var answer int64
	for _, count := range ways {
		answer += count * count
	}
	printInt(answer)
}
