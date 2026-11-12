package main

import (
	"math/bits"
	"syscall"
)

const (
	digits        = 12
	inputSize     = 32
	primeThree    = 3
	primeFive     = 5
	primeSeven    = 7
	primeEleven   = 11
	primeThirteen = 13
)

var input [inputSize]byte
var position, length int

func nextByte() byte {
	for position == length {
		count, err := syscall.Read(syscall.Stdin, input[:])
		if count > 0 {
			position, length = 0, count
			break
		}
		if err != syscall.EINTR {
			return 0
		}
	}
	value := input[position]
	position++
	return value
}

func digit() byte {
	c := nextByte()
	for c != 0 && c <= ' ' {
		c = nextByte()
	}
	return c - '0'
}

func mulmod(a, b, n uint64) uint64 {
	high, low := bits.Mul64(a, b)
	return bits.Rem64(high, low, n)
}

func powmod(a, exponent, n uint64) uint64 {
	result := uint64(1)
	for exponent > 0 {
		if exponent&1 != 0 {
			result = mulmod(result, a, n)
		}
		a = mulmod(a, a, n)
		exponent >>= 1
	}
	return result
}

func isPrime(n uint64) bool {
	if n < 2 {
		return false
	}
	bases := [...]uint64{2, primeThree, primeFive, primeSeven, primeEleven, primeThirteen}
	for _, prime := range bases {
		if n%prime == 0 {
			return n == prime
		}
	}
	odd, twos := n-1, 0
	for odd&1 == 0 {
		odd >>= 1
		twos++
	}
	// These six bases are deterministic below 3474749660383, above 10^12.
	for _, base := range bases {
		value := powmod(base, odd, n)
		if value == 1 || value == n-1 {
			continue
		}
		round := 1
		for round < twos && value != n-1 {
			value = mulmod(value, value, n)
			round++
		}
		if value != n-1 {
			return false
		}
	}
	return true
}

func main() {
	count := int(digit())
	c := nextByte()
	if '0' <= c && c <= '9' {
		count = count*10 + int(c-'0')
	}
	number := uint64(0)
	for i := 0; i < count; i++ {
		number = number*10 + uint64(digit())
	}
	for i := count; i < digits; i++ {
		number *= 10
	}
	if count < digits {
		if number <= 2 {
			number = 2
		} else {
			number |= 1
			for !isPrime(number) {
				number += 2
			}
		}
	}
	var output [digits + 1]byte
	output[digits] = '\n'
	for i := digits - 1; i >= 0; i-- {
		output[i] = byte(number%10) + '0'
		number /= 10
	}
	buffer := output[:]
	for len(buffer) != 0 {
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
