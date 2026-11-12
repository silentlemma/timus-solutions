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

func number() int {
	c := nextByte()
	for c != 0 && c <= ' ' {
		c = nextByte()
	}
	sign := 1
	if c == '-' {
		sign = -1
		c = nextByte()
	}
	value := 0
	for '0' <= c && c <= '9' {
		value = value*10 + int(c-'0')
		c = nextByte()
	}
	return sign * value
}

const maxVertices = 50

func reachesAll(edges *[maxVertices]uint64, n int) bool {
	var pending, seen uint64 = 1, 1
	for pending != 0 {
		bit := pending & -pending
		pending ^= bit
		vertex := 0
		for shifted := bit; shifted > 1; shifted >>= 1 {
			vertex++
		}
		fresh := edges[vertex] & ^seen
		seen |= fresh
		pending |= fresh
	}
	return seen == (uint64(1)<<uint(n))-1
}
func main() {
	n := number()
	var forward, reverse [maxVertices]uint64
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if number() != 0 {
				forward[i] |= uint64(1) << uint(j)
				reverse[j] |= uint64(1) << uint(i)
			}
		}
	}
	// Reachability from one vertex in both directions is strong connectivity.
	if reachesAll(&forward, n) && reachesAll(&reverse, n) {
		writeAll([]byte("Yes\n"))
	} else {
		writeAll([]byte("No\n"))
	}
}
