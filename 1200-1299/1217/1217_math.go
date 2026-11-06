package main

import "syscall"

const (
	digits     = 10
	bufferSize = 32
)

func choose(n, k int) int64 {
	result := int64(1)
	for i := 1; i <= k; i++ {
		result = result * int64(n-i+1) / int64(i)
	}
	return result
}

func equalSums(size int) int64 {
	if size == 0 {
		return 1
	}
	target, variables := (digits-1)*size, 2*size
	var result int64
	for excluded := 0; excluded <= target/digits; excluded++ {
		remaining := target - digits*excluded
		ways := choose(variables, excluded) * choose(remaining+variables-1, variables-1)
		if excluded%2 == 0 {
			result += ways
		} else {
			result -= ways
		}
	}
	return result
}

// Read and write standard handles without constructing file wrappers.
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
	var storage [bufferSize]byte
	size := 0
	reading := true
	for reading {
		count := readInput(storage[:])
		if count == 0 {
			break
		}
		for _, ch := range storage[:count] {
			if ch >= '0' && ch <= '9' {
				size = size*digits + int(ch-'0')
			} else if size != 0 {
				reading = false
				break
			}
		}
	}
	half := size / 2
	answer := equalSums(half/2) * equalSums((half+1)/2)
	// Reuse the input buffer to write the decimal answer from its right end.
	start := len(storage) - 1
	storage[start] = '\n'
	for {
		start--
		storage[start] = '0' + byte(answer%digits)
		answer /= digits
		if answer == 0 {
			break
		}
	}
	writeAll(storage[start:])
}
