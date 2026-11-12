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

const inputSize = 32

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

const maxLength = 2000
const tailAlphabet = "bcd"
const headerReserve = 16

func main() {
	n := number()
	var prefix, tail [maxLength]byte
	for i := 0; i < n; i++ {
		prefix[i] = 'a'
		tail[i] = tailAlphabet[i%len(tailAlphabet)]
	}
	for count := 1; count <= n; count++ {
		if len(output)-used < n+headerReserve {
			writeAll(output[:used])
			used = 0
		}
		writeNumber(count)
		used += copy(output[used:], " : ")
		if count < n && count < len(tailAlphabet) {
			used += copy(output[used:], "NO")
		} else if n < len(tailAlphabet) {
			used += copy(output[used:], prefix[:n])
		} else {
			run := count - len(tailAlphabet)
			used += copy(output[used:], prefix[:run])
			used += copy(output[used:], tail[:n-run])
		}
		output[used] = '\n'
		used++
	}
	writeAll(output[:used])
}
