package main

import "syscall"

const (
	teamSize   = 3
	inputSize  = 64
	outputSize = 8
	maxDigits  = 6
)

var (
	input         [inputSize]byte
	inputPosition int
	inputLength   int
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

func nextInt() int {
	c := nextByte()
	for c != 0 && c <= ' ' {
		c = nextByte()
	}
	value := 0
	for c >= '0' && c <= '9' {
		value = value*10 + int(c-'0')
		c = nextByte()
	}
	return value
}

func pairs(count int) int {
	return count * (count - 1) / 2
}

func teams(total, special, firstSpecial int) int {
	// Reserve a special person for each team left after choosing this one.
	maximum := special - total/teamSize + 1
	s := special - firstSpecial
	o := total - 1 - s
	answer := 0
	if firstSpecial == 1 && maximum >= 1 {
		answer += pairs(o)
	}
	if maximum >= firstSpecial+1 {
		answer += s * o
	}
	if maximum >= firstSpecial+2 {
		answer += pairs(s)
	}
	return answer
}

func main() {
	total, special := nextInt(), nextInt()
	firstSpecial := 0
	for i := 0; i < special; i++ {
		if nextInt() == 1 {
			firstSpecial = 1
			break
		}
	}
	answer := teams(total, special, firstSpecial)
	var digits [maxDigits]byte
	position := len(digits)
	for {
		position--
		digits[position] = '0' + byte(answer%10)
		answer /= 10
		if answer == 0 {
			break
		}
	}
	var output [outputSize]byte
	length := copy(output[:], digits[position:])
	output[length] = '\n'
	writeAll(output[:length+1])
}
