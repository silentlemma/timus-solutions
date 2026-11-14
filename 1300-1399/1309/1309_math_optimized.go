package main

import (
	"strconv"
	"syscall"
)

const (
	modulus      = 9973
	periodScale  = 5219
	periodShift  = 2283
	xCoefficient = 3
	yCoefficient = 7
	decimalBase  = 10
	inputSize    = 32
)

func main() {
	var input [inputSize]byte
	n := 0
	started := false
read:
	for {
		size, err := syscall.Read(syscall.Stdin, input[:])
		if err == syscall.EINTR {
			continue
		}
		if size <= 0 {
			break
		}
		for _, c := range input[:size] {
			if '0' <= c && c <= '9' {
				started = true
				n = n*decimalBase + int(c-'0')
			} else if started {
				break read
			}
		}
		if err != nil {
			break
		}
	}

	// Composing one period gives y -> 5219*y + 2283 modulo 9973.
	y := 0
	scale, shift := periodScale, periodShift
	for periods := n / modulus; periods > 0; periods >>= 1 {
		if periods&1 != 0 {
			y = (scale*y + shift) % modulus
		}
		shift = (scale + 1) * shift % modulus
		scale = scale * scale % modulus
	}
	for x, rest := 1, n%modulus; x <= rest; x++ {
		x2 := x * x % modulus
		x3 := x2 * x % modulus
		x5 := x3 * x2 % modulus
		y = ((x5-x+yCoefficient)*y + x3 + xCoefficient*x - x5) % modulus
		if y < 0 {
			y += modulus
		}
	}
	output := strconv.AppendInt(input[:0], int64(y), decimalBase)
	for rest := append(output, '\n'); len(rest) > 0; {
		size, err := syscall.Write(syscall.Stdout, rest)
		if err == syscall.EINTR {
			continue
		}
		if size <= 0 {
			return
		}
		rest = rest[size:]
	}
}
