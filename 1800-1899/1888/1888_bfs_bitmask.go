package main

import (
	"math/bits"
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

const outputSize = 512

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

const maxPilots = 50
const maxYears = 50

var adj [maxPilots]uint64

func distances(source int, years *[maxPilots]byte) (uint64, int, bool) {
	frontier, seen, depth := uint64(1)<<uint(source), uint64(0), 0
	for frontier != 0 {
		seen |= frontier
		next := uint64(0)
		for vertices := frontier; vertices != 0; vertices &= vertices - 1 {
			vertex := bits.TrailingZeros64(vertices)
			if adj[vertex]&frontier != 0 {
				return 0, 0, false
			}
			years[vertex] = byte(depth + 1)
			next |= adj[vertex]
		}
		frontier = next &^ seen
		if frontier != 0 {
			depth++
		}
	}
	return seen, depth, true
}

func main() {
	n, p := number(), number()
	for flight := 0; flight < n; flight++ {
		a, b := number()-1, number()-1
		adj[a] |= uint64(1) << uint(b)
		adj[b] |= uint64(1) << uint(a)
	}
	unseen := (uint64(1) << uint(p)) - 1
	first, components := uint64(0), 0
	var years [maxPilots]byte
	for unseen != 0 {
		component, _, ok := distances(bits.TrailingZeros64(unseen), &years)
		if !ok {
			writeAll([]byte("-1\n"))
			return
		}
		if components == 0 {
			first = component
		}
		components++
		unseen &^= component
	}
	spread := maxYears - 1
	if components > 1 {
		for id := 0; id < p; id++ {
			parity := (years[id] - 1) & 1
			if first>>uint(id)&1 != 0 {
				years[id] = 1 + parity
			} else {
				years[id] = maxYears - parity
			}
		}
	} else {
		spread = -1
		var best, trial [maxPilots]byte
		for source := 0; source < p; source++ {
			_, far, _ := distances(source, &trial)
			if far > spread {
				spread, best = far, trial
			}
		}
		years = best
	}
	writeNumber(spread)
	output[used] = '\n'
	used++
	for id := 0; id < p; id++ {
		if id != 0 {
			output[used] = ' '
			used++
		}
		writeNumber(int(years[id]))
	}
	output[used] = '\n'
	used++
	writeAll(output[:used])
}
