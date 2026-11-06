package main

import "syscall"

const (
	maxDigits = 2000
	inputSize = 64
	maxDigit  = 9
	noAnswer  = "-1\n"
)

var (
	input         [inputSize]byte
	inputPosition int
	inputLength   int
	digits        [maxDigits + 1]byte
)

// Use standard handles directly; retry interrupts and finish short writes.
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

func nextByte() byte {
	if inputPosition == inputLength {
		inputLength = readInput(input[:])
		inputPosition = 0
		if inputLength == 0 {
			return 0
		}
	}
	value := input[inputPosition]
	inputPosition++
	return value
}

func main() {
	c := nextByte()
	for c != 0 && c <= ' ' {
		c = nextByte()
	}
	size := 0
	for c >= '0' && c <= '9' {
		digits[size] = c
		size++
		c = nextByte()
	}
	tailSum := 0
	for pivot := size - 1; pivot >= 0; pivot-- {
		if digits[pivot] != '9' && tailSum > 0 {
			digits[pivot]++
			tailSum--
			// Fill from the right to make the remaining suffix as small as possible.
			for i := size - 1; i > pivot; i-- {
				digit := tailSum
				if digit > maxDigit {
					digit = maxDigit
				}
				digits[i] = '0' + byte(digit)
				tailSum -= digit
			}
			digits[size] = '\n'
			writeAll(digits[:size+1])
			return
		}
		tailSum += int(digits[pivot] - '0')
	}
	copy(digits[:], noAnswer)
	writeAll(digits[:len(noAnswer)])
}
