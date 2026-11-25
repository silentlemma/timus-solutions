package main

import "syscall"

func main() {
	var block [256]byte
	n := 0
	started, done := false, false
	for !done {
		count, err := syscall.Read(syscall.Stdin, block[:])
		for _, ch := range block[:count] {
			if ch >= '0' && ch <= '9' {
				n = n*10 + int(ch-'0')
				started = true
			} else if started {
				done = true
				break
			}
		}
		if count == 0 || err != nil {
			break
		}
	}
	// The parity depends only on n modulo four, regardless of the signs.
	if residue := n & 3; residue == 0 || residue == 3 {
		writeBytes([]byte("black\n"))
	} else {
		writeBytes([]byte("grimy\n"))
	}
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
