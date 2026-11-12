package main

import "syscall"

const (
	bufferSize         = 64
	maxDigits          = 20
	fractionDigits     = 12
	fractionScale      = 1000000000000
	firstFractionPlace = 100000000000
	roundHalf          = 0.5
	diagonalExtra      = 0.41421356237309504880168872420969807857
)

var input [bufferSize]byte
var output [bufferSize]byte
var position, available, used int

func readByte() byte {
	for position == available {
		count, err := syscall.Read(syscall.Stdin, input[:])
		if count > 0 {
			position, available = 0, count
			break
		}
		if err != syscall.EINTR {
			return 0
		}
	}
	c := input[position]
	position++
	return c
}

func readNumber() int {
	c := readByte()
	for c != 0 && (c < '0' || c > '9') {
		c = readByte()
	}
	value := 0
	for c >= '0' && c <= '9' {
		value = value*10 + int(c-'0')
		c = readByte()
	}
	return value
}

func writeNumber(value int64) {
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

func main() {
	m, n := readNumber(), readNumber()
	length := float64(m*n) + float64(m+n+1)*diagonalExtra
	whole := int64(length)
	fraction := int64((length-float64(whole))*fractionScale + roundHalf)
	if fraction == fractionScale {
		whole++
		fraction = 0
	}
	writeNumber(whole)
	output[used] = '.'
	used++
	place := int64(firstFractionPlace)
	for digit := 0; digit < fractionDigits; digit++ {
		output[used] = '0' + byte(fraction/place)
		used++
		fraction %= place
		place /= 10
	}
	output[used] = '\n'
	used++
	remaining := output[:used]
	for len(remaining) > 0 {
		count, err := syscall.Write(syscall.Stdout, remaining)
		if count > 0 {
			remaining = remaining[count:]
		}
		if err == syscall.EINTR {
			continue
		}
		if count <= 0 {
			break
		}
	}
}
