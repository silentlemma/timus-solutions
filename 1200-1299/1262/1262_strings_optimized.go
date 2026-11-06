package main

import "syscall"

const (
	inputSize  = 64
	outputSize = 8
)

var lengths = [10]uint8{0, 1, 2, 3, 2, 1, 2, 3, 4, 2}

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

func main() {
	var input [inputSize]byte
	total := 0
	started, done := false, false
	for !done {
		length := readInput(input[:])
		if length == 0 {
			break
		}
		for _, c := range input[:length] {
			if c >= '0' && c <= '9' {
				started = true
				total += int(lengths[c-'0'])
			} else if started {
				done = true
				break
			}
		}
	}
	var output [outputSize]byte
	position := len(output) - 1
	output[position] = '\n'
	for {
		position--
		output[position] = '0' + byte(total%10)
		total /= 10
		if total == 0 {
			break
		}
	}
	writeAll(output[position:])
}
