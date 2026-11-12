package main

import "syscall"

const inputSize = 64
const outputSize = 8192
const maxDigits = 4 // The largest printed value is 50*50 + 50/2 + 1.

var output [outputSize]byte
var used int

func readBoardSize() int {
	var input [inputSize]byte
	value := 0
	for {
		count, err := syscall.Read(syscall.Stdin, input[:])
		if count <= 0 {
			if err == syscall.EINTR {
				continue
			}
			return value
		}
		for _, character := range input[:count] {
			if character >= '0' && character <= '9' {
				value = value*10 + int(character-'0')
			} else if value != 0 {
				return value
			}
		}
	}
}

func flush() {
	remaining := output[:used]
	for len(remaining) > 0 {
		count, err := syscall.Write(syscall.Stdout, remaining)
		if count > 0 {
			remaining = remaining[count:]
		}
		if err == syscall.EINTR {
			continue
		}
		if count <= 0 || err != nil {
			break
		}
	}
	used = 0
}

func writeNumber(value int, separator byte) {
	if used+maxDigits+1 > len(output) {
		flush()
	}
	var digits [maxDigits]byte
	start := len(digits)
	for {
		start--
		digits[start] = '0' + byte(value%10)
		value /= 10
		if value == 0 {
			break
		}
	}
	used += copy(output[used:], digits[start:])
	output[used] = separator
	used++
}

func main() {
	n := readBoardSize()
	writeNumber(n*n+n/2+1, '\n')
	large, small := n*n, 1
	for row := 0; row < n; row++ {
		for column := 0; column < n; column++ {
			separator := byte(' ')
			if column == n-1 {
				separator = '\n'
			}
			if (row+column)%2 == 0 {
				writeNumber(large, separator)
				large--
			} else {
				writeNumber(small, separator)
				small++
			}
		}
	}
	flush()
}
