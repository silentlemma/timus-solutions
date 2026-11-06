package main

import "syscall"

const (
	bufferSize = 16
)

// Contests played by players 0 to 13, counted from the story.
var contests = [...]uint8{5, 21, 12, 2, 1, 4, 6, 1, 4, 4, 1, 0, 1, 1}

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
	var buffer [bufferSize]byte
	player := 0
	seen := false
	reading := true
	for reading {
		count := readInput(buffer[:])
		if count == 0 {
			break
		}
		for _, c := range buffer[:count] {
			if c >= '0' && c <= '9' {
				player = 10*player + int(c-'0')
				seen = true
			} else if seen {
				reading = false
				break
			}
		}
	}
	if seen {
		answer := contests[player]
		used := 0
		if answer >= 10 {
			buffer[used] = '0' + answer/10
			used++
		}
		buffer[used] = '0' + answer%10
		used++
		buffer[used] = '\n'
		used++
		writeAll(buffer[:used])
	}
}
