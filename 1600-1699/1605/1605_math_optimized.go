package main

import "syscall"

const (
	bufferSize   = 16
	decimal      = 10
	logNumerator = 301029995663
	scale        = 1000000000000
)

func main() {
	var buffer [bufferSize]byte
	var n uint64
	started := false
readNumber:
	for {
		count, err := syscall.Read(syscall.Stdin, buffer[:])
		if err == syscall.EINTR {
			continue
		}
		if count <= 0 || err != nil {
			break
		}
		for _, digit := range buffer[:count] {
			if digit >= '0' && digit <= '9' {
				n = n*decimal + uint64(digit-'0')
				started = true
			} else if started {
				break readNumber
			}
		}
	}

	// Truncation at twelve decimals preserves the floor up to n = 100000.
	answer := (n &^ 1) * logNumerator / scale
	start := len(buffer) - 1
	buffer[start] = '\n'
	for {
		start--
		buffer[start] = '0' + byte(answer%decimal)
		answer /= decimal
		if answer == 0 {
			break
		}
	}
	for rest := buffer[start:]; len(rest) > 0; {
		count, err := syscall.Write(syscall.Stdout, rest)
		if err == syscall.EINTR {
			continue
		}
		if count <= 0 || err != nil {
			break
		}
		rest = rest[count:]
	}
}
