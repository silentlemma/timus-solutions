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

const limit = 200
const period = 34
const take = 3
const grundyBits = 8

func main() {
	n := number()
	var grundy [limit + 1]byte
	for size := 1; size <= limit; size++ {
		var seen [1 << grundyBits]bool
		if size == 1 {
			seen[0] = true
		}
		if size >= 2 {
			seen[grundy[size-2]] = true
		}
		for left := 0; left <= size-take; left++ {
			seen[grundy[left]^grundy[size-take-left]] = true
		}
		value := byte(0)
		for seen[value] {
			value++
		}
		grundy[size] = value
	}
	if n > limit {
		n = limit - period + (n-limit)%period
	}
	if grundy[n] == 0 {
		writeAll([]byte("Black\n"))
	} else {
		writeAll([]byte("White\n"))
	}
}
