package main

import (
	"sort"
	"syscall"
)

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

const outputSize = 2048

var output [outputSize]byte
var used int

func writeNumber(value int) {
	const maxDigits = 20
	var digits [maxDigits]byte
	first := len(digits)
	for {
		first--
		digits[first] = '0' + byte(value%10)
		value /= 10
		if value == 0 {
			break
		}
	}
	used += copy(output[used:], digits[first:])
}

const maxTeams = 100
const nameCapacity = 11
const alphabet = 26
const shortNames = alphabet + alphabet*alphabet

var names [maxTeams][nameCapacity]byte
var occupied [shortNames]bool

func readName() (name [nameCapacity]byte) {
	c := nextByte()
	for c != 0 && c <= ' ' {
		c = nextByte()
	}
	for i := 0; c > ' '; i++ {
		name[i] = c
		c = nextByte()
	}
	return
}

func less(a, b [nameCapacity]byte) bool {
	for i := range a {
		if a[i] != b[i] {
			return a[i] < b[i]
		}
	}
	return false
}

func writeName(name [nameCapacity]byte) {
	for _, c := range name {
		if c == 0 {
			break
		}
		output[used] = c
		used++
	}
}

func main() {
	n := number()
	for i := 0; i < n; i++ {
		names[i] = readName()
	}
	sort.Slice(names[:n], func(i, j int) bool { return less(names[i], names[j]) })
	duplicate := false
	for i := 1; i < n; i++ {
		duplicate = duplicate || names[i-1] == names[i]
	}
	if duplicate || n == 1 {
		if duplicate && n > 2 {
			writeAll([]byte("Impossible\n"))
		} else {
			writeAll([]byte("0\n"))
		}
		return
	}
	if n == 2 {
		output[used] = '1'
		used++
		output[used] = '\n'
		used++
		writeName(names[0])
		output[used] = '-'
		used++
		writeName(names[1])
		output[used] = '\n'
		used++
		writeAll(output[:used])
		return
	}
	for _, name := range names[:n] {
		if name[1] == 0 {
			occupied[int(name[0]-'a')] = true
		} else if name[2] == 0 {
			occupied[alphabet+int(name[0]-'a')*alphabet+int(name[1]-'a')] = true
		}
	}
	id := 0
	for occupied[id] {
		id++
	}
	var hub [nameCapacity]byte
	if id < alphabet {
		hub[0] = 'a' + byte(id)
	} else {
		id -= alphabet
		hub[0] = 'a' + byte(id/alphabet)
		hub[1] = 'a' + byte(id%alphabet)
	}
	writeNumber(n)
	output[used] = '\n'
	used++
	for _, name := range names[:n] {
		writeName(name)
		output[used] = '-'
		used++
		writeName(hub)
		output[used] = '\n'
		used++
	}
	writeAll(output[:used])
}
