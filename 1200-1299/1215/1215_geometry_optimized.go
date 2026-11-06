package main

import (
	"math"
	"math/bits"
	"syscall"
)

const (
	inputSize     = 64
	outputSize    = 32
	maxDigits     = 20
	scale         = uint64(1000)
	squaredScale  = 4 * scale * scale
	roundingScale = 4
)

type point struct{ x, y int64 }

var input [inputSize]byte
var inputPosition, inputLength int

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

func number() int64 {
	c := nextByte()
	for c != 0 && c <= ' ' {
		c = nextByte()
	}
	negative := c == '-'
	if negative || c == '+' {
		c = nextByte()
	}
	var value int64
	for c >= '0' && c <= '9' {
		value = value*10 + int64(c-'0')
		c = nextByte()
	}
	if negative {
		return -value
	}
	return value
}

func edge(p, a, b point) (bool, uint64, uint64) {
	x, y := p.x-a.x, p.y-a.y
	dx, dy := b.x-a.x, b.y-a.y
	cross := dx*y - dy*x
	dot, length := x*dx+y*dy, dx*dx+dy*dy
	switch {
	case dot <= 0:
		return cross >= 0, uint64(x*x + y*y), 1
	case dot >= length:
		x, y = p.x-b.x, p.y-b.y
		return cross >= 0, uint64(x*x + y*y), 1
	default:
		return cross >= 0, uint64(cross * cross), uint64(length)
	}
}

func less(an, ad, bn, bd uint64) bool {
	ah, al := bits.Mul64(an, bd)
	bh, bl := bits.Mul64(bn, ad)
	return ah < bh || ah == bh && al < bl
}

func roundedDiameter(num, den uint64) uint64 {
	hi, lo := bits.Mul64(num, squaredScale)
	// The quotient is at most 128000000000000 for the coordinate bounds.
	quotient, _ := bits.Div64(hi, lo, den)
	root := uint64(math.Sqrt(float64(quotient)))
	for (root+1)*(root+1) <= quotient {
		root++
	}
	for root*root > quotient {
		root--
	}
	// Compare with the half-unit threshold using exact 128-bit products.
	lh, ll := bits.Mul64(num, roundingScale*squaredScale)
	threshold := 2*root + 1
	rh, rl := bits.Mul64(den, threshold*threshold)
	if lh > rh || lh == rh && ll >= rl {
		root++
	}
	return root
}

func appendNumber(output []byte, value uint64) []byte {
	var digits [maxDigits]byte
	position := len(digits)
	for {
		position--
		digits[position] = '0' + byte(value%10)
		value /= 10
		if value == 0 {
			break
		}
	}
	return append(output, digits[position:]...)
}

func main() {
	p := point{number(), number()}
	n := number()
	first := point{number(), number()}
	previous := first
	x, y := p.x-first.x, p.y-first.y
	bestNum, bestDen := uint64(x*x+y*y), uint64(1)
	inside := true
	for i := int64(1); i <= n; i++ {
		next := first
		if i < n {
			next = point{number(), number()}
		}
		left, num, den := edge(p, previous, next)
		inside = inside && left
		if less(num, den, bestNum, bestDen) {
			bestNum, bestDen = num, den
		}
		previous = next
	}
	if inside {
		bestNum, bestDen = 0, 1
	}
	value := roundedDiameter(bestNum, bestDen)
	var storage [outputSize]byte
	output := appendNumber(storage[:0], value/scale)
	output = append(output, '.')
	for place := scale / 10; place > 0; place /= 10 {
		output = append(output, '0'+byte(value/place%10))
	}
	writeAll(append(output, '\n'))
}
