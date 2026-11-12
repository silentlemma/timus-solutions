package main

import "syscall"

func readInput(buffer []byte) int {
	for {
		count, err := syscall.Read(syscall.Stdin, buffer)
		if count > 0 {
			return count
		}
		if err != syscall.EINTR {
			return 0
		}
	}
}

func writeAll(buffer []byte) {
	for len(buffer) > 0 {
		count, err := syscall.Write(syscall.Stdout, buffer)
		if count > 0 {
			buffer = buffer[count:]
		}
		if err == syscall.EINTR {
			continue
		}
		if count <= 0 {
			return
		}
	}
}

const inputSize = 8192

var input [inputSize]byte
var position, length int

func nextByte() byte {
	if position == length {
		length = readInput(input[:])
		position = 0
		if length == 0 {
			return 0
		}
	}
	value := input[position]
	position++
	return value
}

func number() int {
	c := nextByte()
	for c != 0 && c <= ' ' {
		c = nextByte()
	}
	sign := 1
	if c == '-' {
		sign = -1
		c = nextByte()
	}
	value := 0
	for '0' <= c && c <= '9' {
		value = value*10 + int(c-'0')
		c = nextByte()
	}
	return sign * value
}

const outputSize = 8192

var output [outputSize]byte
var used int

func writeNumber(value int) {
	const maxDigits = 20
	var digits [maxDigits]byte
	first := len(digits)
	for {
		first--
		digits[first] = '0' + byte(value%10)
		value /= 10
		if value == 0 {
			break
		}
	}
	used += copy(output[used:], digits[first:])
}

const maxWindow = 50
const outputReserve = 8

var plans [maxWindow]int

func main() {
	n, m := number(), number()
	for i := 0; i < m; i++ {
		plans[i] = number()
	}
	head, stock := 0, 0
	for month := 0; month < n; month++ {
		best, index := plans[head]-stock, head
		for t := 2; t <= m; t++ {
			index++
			if index == m {
				index = 0
			}
			delta := plans[index] - stock
			change := delta / t
			if delta >= 0 {
				change = (delta + t - 1) / t
			}
			if change > best {
				best = change
			}
		}
		stock += best
		if len(output)-used < outputReserve {
			writeAll(output[:used])
			used = 0
		}
		value := best
		if value < 0 {
			output[used] = '-'
			used++
			value = -value
		}
		writeNumber(value)
		if month+1 == n {
			output[used] = '\n'
		} else {
			output[used] = ' '
		}
		used++
		if month+1 < n {
			plans[head] = number()
			head++
			if head == m {
				head = 0
			}
		}
	}
	writeAll(output[:used])
}
