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

const count = 10
const base = 10
const maxValue = 10000

// Six distinct primes already have product30030>maxValue.
const maxDistinctPerValue = 5

var exponent [maxValue + 1]uint8
var touched [count * maxDistinctPerValue]int
var used int

func addPrime(prime, power int) {
	if exponent[prime] == 0 {
		touched[used] = prime
		used++
	}
	// At most10*floor(log2(10000))=130, so unsigned8bits suffice.
	exponent[prime] += uint8(power)
}

func main() {
	for i := 0; i < count; i++ {
		value := nextInt()
		for prime := 2; prime*prime <= value; {
			power := 0
			for value%prime == 0 {
				power++
				value /= prime
			}
			if power > 0 {
				addPrime(prime, power)
			}
			if prime == 2 {
				prime++
			} else {
				prime += 2
			}
		}
		if value > 1 {
			addPrime(value, 1)
		}
	}
	answer := 1
	for _, prime := range touched[:used] {
		answer = answer * (int(exponent[prime]) + 1) % base
	}
	byteOut(byte(answer) + '0')
	byteOut('\n')
	flush()
}
