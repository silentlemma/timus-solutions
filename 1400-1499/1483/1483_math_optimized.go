package main

import "syscall"

const (
	bufferSize = 24
	maxDigits  = 20
)

const win = 3

func appendNumber(output []byte, value int64) []byte {
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
	return append(output, digits[first:]...)
}

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

func main() {
	var buffer [bufferSize]byte
	teams := 0
	reading := true
	for reading {
		count := readInput(buffer[:])
		if count == 0 {
			break
		}
		for _, c := range buffer[:count] {
			if c >= '0' && c <= '9' {
				teams = 10*teams + int(c-'0')
			} else if teams != 0 {
				reading = false
				break
			}
		}
	}
	if teams == 0 {
		return
	}
	// The extrema are the average of all draws and the rounded-down average of all wins.
	others := int64(teams - 1)
	output := appendNumber(buffer[:0], others)
	output = appendNumber(append(output, ' '), win*others/2)
	writeAll(append(output, '\n'))
}
