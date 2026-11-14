package main

import "syscall"

const (
	decimal    = 10
	places     = 8
	scale      = 100000000
	maxCases   = 2004
	inputSize  = 4096
	resultSize = len("0.") + places + len("\n")
)

type input struct {
	data       [inputSize]byte
	start, end int
}

func (in *input) nextByte() byte {
	for in.start == in.end {
		n, err := syscall.Read(syscall.Stdin, in.data[:])
		if err == syscall.EINTR {
			continue
		}
		if n <= 0 {
			return 0
		}
		in.start, in.end = 0, n
	}
	c := in.data[in.start]
	in.start++
	return c
}

func (in *input) number() int64 {
	c := in.nextByte()
	for c != 0 && c <= ' ' {
		c = in.nextByte()
	}
	var value int64
	for c >= '0' && c <= '9' {
		value = decimal*value + int64(c-'0')
		c = in.nextByte()
	}
	return value
}

func main() {
	var input input
	var storage [maxCases * resultSize]byte
	output := storage[:0]
	for remaining := input.number(); remaining > 0; remaining-- {
		k, m := input.number(), input.number()
		switch {
		case m > k:
			output = append(output, "0\n"...)
		case m == 0:
			output = append(output, "1\n"...)
		default:
			// Truncating to eight decimal places gives absolute error below 10^-8.
			fraction := (k - m + 1) * scale / (k + 1)
			output = append(output, "0."...)
			start := len(output)
			output = output[:start+places]
			for pos := len(output) - 1; pos >= start; pos-- {
				output[pos] = '0' + byte(fraction%decimal)
				fraction /= decimal
			}
			output = append(output, '\n')
		}
	}
	for len(output) > 0 {
		n, err := syscall.Write(syscall.Stdout, output)
		if err == syscall.EINTR {
			continue
		}
		if n <= 0 {
			return
		}
		output = output[n:]
	}
}
