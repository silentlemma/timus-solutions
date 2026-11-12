package main

import "syscall"

const capacity = 10000
const maxS = 50
const decimalBase = 10

func count(k, s int) int {
	if k > s/2 {
		return 0
	}
	var choose, exact [maxS/2 + 1]int
	coefficient := 1
	choose[k] = coefficient
	for m := k + 1; m <= s/2; m++ {
		coefficient = coefficient * m / (m - k)
		if coefficient >= capacity {
			return capacity
		}
		choose[m] = coefficient
	}
	limit, total := s/k, 0
	for divisor := limit; divisor >= 2; divisor-- {
		value := choose[s/divisor]
		for multiple := 2 * divisor; multiple <= limit; multiple += divisor {
			value -= exact[multiple]
		}
		exact[divisor] = value
		total += value
		if total >= capacity {
			return capacity
		}
	}
	return total
}

const inputSize = 64
const maxDigits = 5

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

func number() int {
	c := readByte()
	for c != 0 && c <= ' ' {
		c = readByte()
	}
	value := 0
	for c >= '0' && c <= '9' {
		value = value*decimalBase + int(c-'0')
		c = readByte()
	}
	return value
}

func main() {
	k, s := number(), number()
	value := count(k, s)
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
