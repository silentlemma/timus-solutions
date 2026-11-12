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

const inputSize = 4096
const outputSize = 64

var input [inputSize]byte
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

func main() {
	errors := 0
	newSentence, inWord := true, false
	for {
		count := readInput(input[:])
		if count == 0 {
			break
		}
		for _, c := range input[:count] {
			lower, upper := c >= 'a' && c <= 'z', c >= 'A' && c <= 'Z'
			if lower || upper {
				if lower && newSentence {
					errors++
				}
				if upper && inWord {
					errors++
				}
				newSentence, inWord = false, true
			} else {
				inWord = false
				if c == '.' || c == '?' || c == '!' {
					newSentence = true
				}
			}
		}
	}
	writeNumber(errors)
	output[used] = '\n'
	used++
	writeAll(output[:used])
}
