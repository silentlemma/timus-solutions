package main

import (
	"math"
	"syscall"
)

const inputSize = 64
const decimalBase = 10
const maxDigits = 9
const firstOddPrime uint64 = 3
const firstWheelDivisor uint64 = 5
const wheelPeriod uint64 = 6

var input [inputSize]byte
var position, available int

func readByte() byte {
	for position == available {
		count, err := syscall.Read(syscall.Stdin, input[:])
		if count > 0 {
			position, available = 0, count
			break
		}
		if err != syscall.EINTR {
			return 0
		}
	}
	c := input[position]
	position++
	return c
}

func writeNumber(value uint64) {
	var output [maxDigits + 1]byte
	start := len(output) - 1
	output[start] = '\n'
	for {
		start--
		output[start] = '0' + byte(value%decimalBase)
		value /= decimalBase
		if value == 0 {
			break
		}
	}
	pending := output[start:]
	for len(pending) > 0 {
		written, err := syscall.Write(syscall.Stdout, pending)
		if written > 0 {
			pending = pending[written:]
		}
		if err == syscall.EINTR {
			continue
		}
		if written <= 0 || err != nil {
			return
		}
	}
}

func isqrt(value uint64) uint64 {
	root := uint64(math.Sqrt(float64(value)))
	for root*root > value {
		root--
	}
	for (root+1)*(root+1) <= value {
		root++
	}
	return root
}

func remove(value, divisor uint64, root *uint64) uint64 {
	square := divisor * divisor
	for value%square == 0 {
		value /= square
		*root *= divisor
	}
	if value%divisor == 0 {
		value /= divisor
	}
	return value
}

func answer(value uint64) uint64 {
	root := isqrt(value)
	if root*root == value {
		return root/2 + 1
	}
	root = 1
	value = remove(value, 2, &root)
	value = remove(value, firstOddPrime, &root)
	// No remaining prime factor is below the current wheel divisor.
	for divisor, step := firstWheelDivisor, uint64(2); divisor*divisor*divisor <= value; {
		value = remove(value, divisor, &root)
		divisor += step
		step = wheelPeriod - step
	}
	if tail := isqrt(value); tail*tail == value {
		root *= tail
	}
	return root/2 + 1
}

func main() {
	c := readByte()
	for c != 0 && c <= ' ' {
		c = readByte()
	}
	if c == '+' {
		c = readByte()
	}
	var value uint64
	for c >= '0' && c <= '9' {
		value = value*decimalBase + uint64(c-'0')
		c = readByte()
	}
	writeNumber(answer(value))
}
