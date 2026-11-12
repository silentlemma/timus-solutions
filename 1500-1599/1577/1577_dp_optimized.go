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

const outputSize = 64

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

const maxPassword = 2000
const modulus uint32 = 1000000007

func password(buffer []byte) int {
	c := nextByte()
	for c != 0 && c <= ' ' {
		c = nextByte()
	}
	length := 0
	for c > ' ' {
		buffer[length] = c
		length++
		c = nextByte()
	}
	return length
}

func main() {
	var a, b [maxPassword]byte
	n, m := password(a[:]), password(b[:])
	// Lengths never exceed 4000; counts are reduced modulo modulus at every cell.
	var length [maxPassword + 1]uint16
	var count [maxPassword + 1]uint32
	for j := 0; j <= m; j++ {
		length[j], count[j] = uint16(m-j), 1
	}
	for i := n - 1; i >= 0; i-- {
		diagonalLength, diagonalCount := length[m], count[m]
		length[m], count[m] = uint16(n-i), 1
		for j := m - 1; j >= 0; j-- {
			belowLength, belowCount := length[j], count[j]
			if a[i] == b[j] {
				length[j], count[j] = diagonalLength+1, diagonalCount
			} else if belowLength < length[j+1] {
				length[j], count[j] = belowLength+1, belowCount
			} else if belowLength > length[j+1] {
				length[j], count[j] = length[j+1]+1, count[j+1]
			} else {
				ways := belowCount + count[j+1]
				if ways >= modulus {
					ways -= modulus
				}
				length[j], count[j] = belowLength+1, ways
			}
			// Save the old cell before overwrite: it is the next cell's lower-right diagonal.
			diagonalLength, diagonalCount = belowLength, belowCount
		}
	}
	writeNumber(int(count[0]))
	output[used] = '\n'
	used++
	writeAll(output[:used])
}
