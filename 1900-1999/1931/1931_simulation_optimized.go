package main

import (
	"fmt"
	"os"
)

const inputBuffer = 4096

// refills bound storage even when whitespace or tokens cross a buffer boundary.
type reader struct {
	buffer   [inputBuffer]byte
	at, size int
}

func (r *reader) read() byte {
	if r.at == r.size {
		r.size, _ = os.Stdin.Read(r.buffer[:])
		r.at = 0
		if r.size == 0 {
			return 0
		}
	}
	c := r.buffer[r.at]
	r.at++
	return c
}
func (r *reader) next() int {
	c := r.read()
	for c != 0 && c != '-' && (c < '0' || c > '9') {
		c = r.read()
	}
	sign := 1
	if c == '-' {
		sign = -1
		c = r.read()
	}
	value := 0
	for c >= '0' && c <= '9' {
		value = value*10 + int(c-'0')
		c = r.read()
	}
	return sign * value
}

func main() {
	in := reader{}
	n, championValue := in.next(), in.next()
	champion, best, currentCount, bestCount := 0, 0, 0, 0
	// only the incumbent and its comparison count survive each input value.
	for index := 1; index < n; index++ {
		value := in.next()
		currentCount++
		if currentCount > bestCount {
			bestCount, best = currentCount, champion
		}
		if value < championValue {
			championValue, champion, currentCount = value, index, 1
		}
	}
	fmt.Println(best + 1)
}
