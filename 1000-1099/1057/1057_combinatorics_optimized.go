package main

import "syscall"

const (
	decimal    = 10
	inputSize  = 64
	numberSize = 12
)

var input [inputSize]byte
var offset, length int

func nextByte() byte {
	if offset == length {
		for {
			size, err := syscall.Read(syscall.Stdin, input[:])
			if err == syscall.EINTR {
				continue
			}
			if size <= 0 || err != nil {
				return 0
			}
			length = size
			break
		}
		offset = 0
		if length == 0 {
			return 0
		}
	}
	value := input[offset]
	offset++
	return value
}

func number() uint64 {
	c := nextByte()
	for c != 0 && c <= ' ' {
		c = nextByte()
	}
	var value uint64
	for c >= '0' && c <= '9' {
		value = decimal*value + uint64(c-'0')
		c = nextByte()
	}
	return value
}

func choose(n, k uint64) uint64 {
	if k > n {
		return 0
	}
	if n-k < k {
		k = n - k
	}
	count := uint64(1)
	for step := uint64(1); step <= k; step++ {
		count = count * (n - k + step) / step
	}
	return count
}

func countAtMost(bound, remaining, base uint64) uint64 {
	place, lower := uint64(1), uint64(0)
	for place <= bound/base {
		place *= base
		lower++
	}
	ways := choose(lower, remaining)
	var total uint64
	for remaining <= lower+1 {
		digit := bound / place
		if digit > 1 {
			if remaining == lower+1 {
				return total + 1
			}
			return total + ways + ways*remaining/(lower-remaining+1)
		}
		if digit == 1 {
			total += ways
			if remaining == 0 {
				return total
			}
		}
		if lower == 0 {
			if remaining == digit {
				total++
			}
			return total
		}

		// Update C(lower, remaining) for the next lower digit.
		if digit == 1 {
			ways = ways * remaining / lower
			remaining--
		} else if remaining <= lower {
			ways = ways * (lower - remaining) / lower
		}
		bound %= place
		place /= base
		lower--
	}
	return total
}

func main() {
	x, y, k, base := number(), number(), number(), number()
	answer := countAtMost(y, k, base) - countAtMost(x-1, k, base)
	var output [numberSize]byte
	end := len(output) - 1
	output[end] = '\n'
	for {
		end--
		output[end] = '0' + byte(answer%decimal)
		answer /= decimal
		if answer == 0 {
			break
		}
	}
	write(output[end:])
}

func write(data []byte) {
	for len(data) != 0 {
		size, err := syscall.Write(syscall.Stdout, data)
		if err == syscall.EINTR {
			continue
		}
		if size <= 0 || err != nil {
			return
		}
		data = data[size:]
	}
}
