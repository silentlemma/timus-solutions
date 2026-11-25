package main

import "syscall"

func main() {
	var block [256]byte
	n, marks := 0, 0
	// The only numeric token precedes the consecutive factorial marks.
	complete := false
	for !complete {
		count, err := syscall.Read(syscall.Stdin, block[:])
		for _, ch := range block[:count] {
			if ch >= '0' && ch <= '9' && marks == 0 {
				n = n*10 + int(ch-'0')
			} else if ch == '!' {
				marks++
			} else if marks > 0 {
				complete = true
				break
			}
		}
		if count == 0 || err != nil {
			break
		}
	}
	// multiply n, n - k, ... while the factor stays positive
	product := 1
	for factor := n; factor > 0; factor -= marks {
		product *= factor
	}
	var answer [24]byte
	pos := len(answer) - 1
	answer[pos] = '\n'
	for {
		pos--
		answer[pos] = byte(product%10) + '0'
		product /= 10
		if product == 0 {
			break
		}
	}
	writeBytes(answer[pos:])
	syscall.Exit(0)
}

// Complete writes also handle a pipe that accepts only part of the answer.
func writeBytes(data []byte) {
	for len(data) > 0 {
		n, err := syscall.Write(syscall.Stdout, data)
		if n > 0 {
			data = data[n:]
		}
		if err != nil || n == 0 {
			return
		}
	}
}
