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

const inputSize = 256

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

const width = 80

func main() {
	var screen [width + 1]byte
	for i := 0; i < width; i++ {
		screen[i] = ' '
	}
	cursor := 0
	for key := nextByte(); key != 0 && key != '\n' && key != '\r'; key = nextByte() {
		if key == '<' {
			if cursor != 0 {
				cursor--
			}
		} else {
			if key != '>' {
				screen[cursor] = key
			}
			cursor++
			if cursor == width {
				cursor = 0
			}
		}
	}
	screen[width] = '\n'
	writeAll(screen[:])
}
