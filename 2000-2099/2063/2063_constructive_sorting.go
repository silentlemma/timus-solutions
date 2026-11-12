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

const inputSize = 8192
const outputSize = 8192
const lineReserve = 16

var input [inputSize]byte
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

func writePair(kind byte, first, second int) {
	if len(output)-used < lineReserve {
		writeAll(output[:used])
		used = 0
	}
	output[used] = kind
	used++
	output[used] = ' '
	used++
	writeNumber(first)
	output[used] = ' '
	used++
	writeNumber(second)
	output[used] = '\n'
	used++
}

// FNV-1a of the whole input seeds splitmix64; the arrangements are never
// decoded, they only make the seed differ between tests
const (
	fnvOffset uint64 = 0xcbf29ce484222325
	fnvPrime  uint64 = 0x100000001b3
	golden    uint64 = 0x9e3779b97f4a7c15
	mixA      uint64 = 0xbf58476d1ce4e5b9
	mixB      uint64 = 0x94d049bb133111eb
	shiftA           = 30
	shiftB           = 27
	shiftC           = 31
)

var state uint64

func nextRandom() uint64 {
	state += golden
	z := state
	z = (z ^ (z >> shiftA)) * mixA
	z = (z ^ (z >> shiftB)) * mixB
	return z ^ (z >> shiftC)
}

func compare(first, second, real int) {
	// Ascending comparisons never change black virtual padding to the right of real balls.
	if second < real {
		writePair('?', first+1, second+1)
	}
}

func mergeNetwork(start, size, stride, real int) {
	step := 2 * stride
	if step < size {
		mergeNetwork(start, size, step, real)
		mergeNetwork(start+stride, size, step, real)
		for first := start + stride; first+stride < start+size; first += step {
			compare(first, first+stride, real)
		}
	} else {
		compare(start, start+stride, real)
	}
}

func sortNetwork(start, size, real int) {
	if size > 1 {
		half := size / 2
		sortNetwork(start, half, real)
		sortNetwork(start+half, half, real)
		mergeNetwork(start, size, 1, real)
	}
}

func main() {
	state = fnvOffset
	games, started, finished := 0, false, false
	for {
		count := readInput(input[:])
		if count == 0 {
			break
		}
		for _, c := range input[:count] {
			state = (state ^ uint64(c)) * fnvPrime
			if !finished {
				if c >= '0' && c <= '9' {
					games = games*10 + int(c-'0')
					started = true
				} else if started {
					finished = true
				}
			}
		}
	}
	for game := 0; game < games; game++ {
		n, padded := game+2, 1
		for padded < n {
			padded *= 2
		}
		sortNetwork(0, padded, n)
		j := 1 + int(nextRandom()%uint64(n-1))
		writePair('!', j, j+1)
	}
	writeAll(output[:used])
}
