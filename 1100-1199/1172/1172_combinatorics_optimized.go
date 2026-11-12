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

const outputSize = 128

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

const maxCities = 30
const islands = 3
const patternLimbs = 3
const outputLimbs = 14
const limbDigits = 9
const base = 1000000000

// A fixed starting island leaves at most 2^89 patterns, fewer than base^3.
type pattern [patternLimbs]uint32
type plane [maxCities + 1][maxCities + 1][islands]pattern

func add(left, right pattern) pattern {
	var result pattern
	carry := uint32(0)
	for i := range result {
		value := left[i] + right[i] + carry
		carry = 0
		if value >= base {
			value -= base
			carry = 1
		}
		result[i] = value
	}
	return result
}

func main() {
	n := number()
	var planes [2]plane
	for a := 1; a <= n; a++ {
		current, previous := a%2, 1-a%2
		planes[current] = plane{}
		for b := 0; b <= n; b++ {
			for c := 0; c <= n; c++ {
				cell := &planes[current][b][c]
				if a == 1 && b == 0 && c == 0 {
					cell[0][0] = 1
				}
				if a > 1 {
					cell[0] = add(planes[previous][b][c][1], planes[previous][b][c][2])
				}
				if b > 0 {
					cell[1] = add(planes[current][b-1][c][0], planes[current][b-1][c][2])
				}
				if c > 0 {
					cell[2] = add(planes[current][b][c-1][0], planes[current][b][c-1][1])
				}
			}
		}
	}
	patterns := add(planes[n%2][n][n][1], planes[n%2][n][n][2])
	var total [outputLimbs]uint32
	copy(total[:], patterns[:])
	// Multiplying by (n-1)! n!^2 needs at most 122 digits before halving; 14 limbs fit 126.
	for k := 2; k <= n; k++ {
		factor := uint64(k * k * (k - 1))
		carry := uint64(0)
		for i := range total {
			value := uint64(total[i])*factor + carry
			total[i] = uint32(value % base)
			carry = value / base
		}
	}
	remainder := uint64(0)
	for i := len(total) - 1; i >= 0; i-- {
		value := remainder*base + uint64(total[i])
		total[i] = uint32(value / 2)
		remainder = value % 2
	}
	highest := len(total) - 1
	for highest > 0 && total[highest] == 0 {
		highest--
	}
	writeNumber(int(total[highest]))
	for i := highest - 1; i >= 0; i-- {
		divisor := uint32(base / 10)
		for digit := 0; digit < limbDigits; digit++ {
			output[used] = '0' + byte(total[i]/divisor%10)
			used++
			divisor /= 10
		}
	}
	output[used] = '\n'
	used++
	writeAll(output[:used])
}
