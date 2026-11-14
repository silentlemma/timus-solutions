package main

import "syscall"

const (
	decimal     = 10
	inputSize   = 32
	maxDegree   = 1000
	indexDigits = 4
	stepSize    = len("X\n*\n\n+\n") + indexDigits
)

func readDegree() int {
	var input [inputSize]byte
	degree, started := 0, false
	for {
		n, err := syscall.Read(syscall.Stdin, input[:])
		if err == syscall.EINTR {
			continue
		}
		if n <= 0 {
			return degree
		}
		for _, c := range input[:n] {
			if c >= '0' && c <= '9' {
				degree = degree*decimal + int(c-'0')
				started = true
			} else if started {
				return degree
			}
		}
	}
}

func main() {
	degree := readDegree()
	var buffer [len("0\n") + maxDegree*stepSize]byte
	output := append(buffer[:0], "0\n"...)
	digits := [indexDigits]byte{'0', '0', '0', '0'}
	first := len(digits) - 1
	for i := 1; i <= degree; i++ {
		// Advance the coefficient's decimal representation in place.
		pos := len(digits) - 1
		for digits[pos] == '9' {
			digits[pos] = '0'
			pos--
		}
		digits[pos]++
		if pos < first {
			first = pos
		}
		output = append(output, "X\n*\n"...)
		output = append(output, digits[first:]...)
		output = append(output, "\n+\n"...)
	}
	for len(output) > 0 {
		n, err := syscall.Write(syscall.Stdout, output)
		if err == syscall.EINTR {
			continue
		}
		if n <= 0 {
			return
		}
		output = output[n:]
	}
}
