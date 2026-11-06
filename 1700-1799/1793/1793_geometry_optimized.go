package main

import "syscall"

const inputSize = 64

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

func nextInt() int64 {
	c := nextByte()
	for c != 0 && c <= ' ' {
		c = nextByte()
	}
	var value int64
	for c >= '0' && c <= '9' {
		value = value*10 + int64(c-'0')
		c = nextByte()
	}
	return value
}

func min(a, b int64) int64 {
	if a < b {
		return a
	}
	return b
}

func fits(a, b, border, r1, top1, r2, top2, height int64) bool {
	level := min(border, height)
	w1 := r1*height + (top1-r1)*level
	w2 := r2*height + (top2-r2)*level
	width := min(a, b) * height
	if 2*w1 > width || 2*w2 > width {
		return false
	}
	// Opposite corners maximise the separation between the allowed centres.
	dx, dy := a*height-w1-w2, b*height-w1-w2
	separation := (top1 + top2) * height
	return dx*dx+dy*dy >= separation*separation
}

func main() {
	a, b, border := nextInt(), nextInt(), nextInt()
	r1, top1, r2, top2, height := nextInt(), nextInt(), nextInt(), nextInt(), nextInt()
	if fits(a, b, border, r1, top1, r2, top2, height) {
		writeAll([]byte("YES\n"))
	} else {
		writeAll([]byte("NO\n"))
	}
}
