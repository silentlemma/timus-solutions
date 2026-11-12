package main

import (
	"sort"
	"syscall"
)

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

const inputSize = 256

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

func word() byte {
	c := nextByte()
	for c != 0 && c <= ' ' {
		c = nextByte()
	}
	first := c
	for c > ' ' {
		c = nextByte()
	}
	return first
}

const cents = 100
const decimalPlaces = 2

func price() int {
	c := nextByte()
	for c != 0 && c <= ' ' {
		c = nextByte()
	}
	whole := 0
	for c >= '0' && c <= '9' {
		whole = whole*10 + int(c-'0')
		c = nextByte()
	}
	fraction, digits := 0, 0
	if c == '.' {
		c = nextByte()
		for c >= '0' && c <= '9' {
			fraction = fraction*10 + int(c-'0')
			digits++
			c = nextByte()
		}
	}
	for ; digits < decimalPlaces; digits++ {
		fraction *= 10
	}
	return whole*cents + fraction
}

const outputSize = 64

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

const maxOperations = 100000
const bid, del = -1, -2

type operation struct{ price, amount int }

func main() {
	operations := make([]operation, 0, maxOperations)
	prices := make([]int, 0, maxOperations)
	for command := word(); command != 'Q' && command != 0; command = word() {
		value := price()
		amount := del
		if command == 'B' {
			amount = bid
			prices = append(prices, value)
		} else if command == 'S' {
			amount = number()
		}
		operations = append(operations, operation{value, amount})
	}
	sort.Ints(prices)
	unique := prices[:0]
	for _, value := range prices {
		if len(unique) == 0 || value != unique[len(unique)-1] {
			unique = append(unique, value)
		}
	}
	prices = unique
	tree := make([]int32, len(prices)+1)
	active := 0
	var revenue int64
	for _, op := range operations {
		index := sort.SearchInts(prices, op.price)
		if op.amount < 0 {
			delta := int32(-1)
			if op.amount == bid {
				delta = 1
			}
			active += int(delta)
			for index++; index < len(tree); index += index & -index {
				tree[index] += delta
			}
		} else {
			// The prefix excludes equal prices: those bids remain eligible.
			cheaper := 0
			for ; index > 0; index -= index & -index {
				cheaper += int(tree[index])
			}
			sold := active - cheaper
			if sold > op.amount {
				sold = op.amount
			}
			revenue += int64(sold)
		}
	}
	writeNumber(int(revenue / cents))
	output[used] = '.'
	used++
	output[used] = '0' + byte(revenue%cents/10)
	used++
	output[used] = '0' + byte(revenue%10)
	used++
	output[used] = '\n'
	used++
	writeAll(output[:used])
}
