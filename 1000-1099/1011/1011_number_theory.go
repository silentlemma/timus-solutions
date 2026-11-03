package main

import (
	"syscall"
)

const rawInputSize = 256
const rawOutputSize = 128
const decimalSize = 32
const radix = 10

var rawInput [rawInputSize]byte
var rawPosition, rawLength int
var rawOutput [rawOutputSize]byte
var rawUsed int

func byteIn() byte {
	if rawPosition == rawLength {
		// Global arrays stay live and never move across the raw system call.
		n, failure := syscall.Read(syscall.Stdin, rawInput[:])
		if failure != nil || n == 0 {
			return 0
		}
		rawPosition, rawLength = 0, int(n)
	}
	ch := rawInput[rawPosition]
	rawPosition++
	return ch
}
func nextInt() int {
	ch := byteIn()
	for ch != 0 && ch <= ' ' {
		ch = byteIn()
	}
	value := 0
	for ch >= '0' && ch <= '9' {
		value = value*radix + int(ch-'0')
		ch = byteIn()
	}
	return value
}
func flush() {
	at := 0
	for at < rawUsed {
		n, failure := syscall.Write(syscall.Stdout, rawOutput[at:rawUsed])
		if failure != nil || n == 0 {
			break
		}
		at += int(n)
	}
	rawUsed = 0
}
func byteOut(ch byte) {
	if rawUsed == len(rawOutput) {
		flush()
	}
	rawOutput[rawUsed] = ch
	rawUsed++
}
func numberOut(value int64) {
	var digits [decimalSize]byte
	at := len(digits)
	for {
		at--
		digits[at] = byte(value%radix) + '0'
		value /= radix
		if value == 0 {
			break
		}
	}
	for ; at < len(digits); at++ {
		byteOut(digits[at])
	}
}

const hundredthsPerPercent int64 = 100
const whole int64 = 100 * hundredthsPerPercent

func percentage() int64 {
	ch := byteIn()
	for ch != 0 && ch <= ' ' {
		ch = byteIn()
	}
	value := int64(0)
	for ch >= '0' && ch <= '9' {
		value = value*radix + int64(ch-'0')
		ch = byteIn()
	}
	value *= hundredthsPerPercent
	if ch == '.' {
		scale := hundredthsPerPercent
		ch = byteIn()
		for ch >= '0' && ch <= '9' {
			scale /= radix
			value += int64(ch-'0') * scale
			ch = byteIn()
		}
	}
	return value
}
func main() {
	p, q := percentage(), percentage()
	a, b, c, d := int64(0), int64(1), int64(1), int64(0)
	for {
		numerator, denominator := a+c, b+d
		if whole*numerator <= p*denominator {
			steps := (p*b - whole*a) / (whole*c - p*d)
			a += steps * c
			b += steps * d
		} else if whole*numerator >= q*denominator {
			steps := (whole*c - q*d) / (q*b - whole*a)
			c += steps * a
			d += steps * b
		} else {
			numberOut(denominator)
			byteOut('\n')
			flush()
			return
		}
	}
}
