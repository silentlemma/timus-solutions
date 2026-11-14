package main

import "syscall"

const (
	decimal        = 10
	lengthDigits   = 4
	inputCapacity  = 64
	outputCapacity = 8
)

func digit(c byte) bool {
	return c >= '0' && c <= '9'
}

// Read a nonnegative decimal and scale it to the requested precision.
func number(input []byte, pos *int, places int) int {
	at := *pos
	for at < len(input) && input[at] <= ' ' {
		at++
	}
	value := 0
	for at < len(input) && digit(input[at]) {
		value = value*decimal + int(input[at]-'0')
		at++
	}
	if at < len(input) && input[at] == '.' {
		at++
		for at < len(input) && places > 0 && digit(input[at]) {
			value = value*decimal + int(input[at]-'0')
			places--
			at++
		}
	}
	for ; places > 0; places-- {
		value *= decimal
	}
	*pos = at
	return value
}

func main() {
	var input [inputCapacity]byte
	size := 0
	for size < len(input) {
		n, err := syscall.Read(syscall.Stdin, input[size:])
		if err == syscall.EINTR {
			continue
		}
		if n <= 0 {
			break
		}
		size += n
	}
	pos := 0
	lines := number(input[:size], &pos, 0)
	length := number(input[:size], &pos, lengthDigits)
	rail := number(input[:size], &pos, lengthDigits)

	answer := lines * (length / rail)
	if rest := length % rail; rest != 0 {
		answer += 1 + (lines-1)/(rail/rest)
	}

	var output [outputCapacity]byte
	start := len(output) - 1
	output[start] = '\n'
	for {
		start--
		output[start] = '0' + byte(answer%decimal)
		answer /= decimal
		if answer == 0 {
			break
		}
	}
	for rest := output[start:]; len(rest) > 0; {
		size, err := syscall.Write(syscall.Stdout, rest)
		if err == syscall.EINTR {
			continue
		}
		if size <= 0 {
			return
		}
		rest = rest[size:]
	}
}
