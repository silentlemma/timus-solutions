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

const frames, pins, maxLastRolls, states = 10, 10, 3, 4
const infinity = frames*pins*maxLastRolls + 1

func put(low, high *[states]int, state, a, b int) {
	if a < low[state] {
		low[state] = a
	}
	if b > high[state] {
		high[state] = b
	}
}
func main() {
	var low, high [states]int
	for s := 1; s < states; s++ {
		low[s] = infinity
		high[s] = -1
	}
	for f := 0; f < frames-1; f++ {
		total := nextInt()
		var nextLow, nextHigh [states]int
		for s := 0; s < states; s++ {
			nextLow[s] = infinity
			nextHigh[s] = -1
		}
		for state := 0; state < states; state++ {
			if high[state] < 0 {
				continue
			}
			a, b := (state+1)/2, state/2
			if total < pins {
				put(&nextLow, &nextHigh, 0, low[state]+total*(1+b), high[state]+total*(1+a))
			} else {
				put(&nextLow, &nextHigh, 1, low[state]+pins*(1+b), high[state]+pins+(pins-1)*a+b)
				// A strike shifts old pending bonuses and adds its own two.
				target, bonus := 2+b, pins*(1+a)
				put(&nextLow, &nextHigh, target, low[state]+bonus, high[state]+bonus)
			}
		}
		low, high = nextLow, nextHigh
	}
	last := nextInt()
	answerLow, answerHigh := infinity, -1
	for state := 0; state < states; state++ {
		if high[state] < 0 {
			continue
		}
		a, b := (state+1)/2, state/2
		lower, upper := 0, 0
		if last < pins {
			lower, upper = b*last, a*last
		} else if last <= 2*pins {
			lower, upper = pins*b, pins*a+b*(last-pins)
		} else {
			lower = pins * (a + b)
			upper = lower
		}
		if value := low[state] + last + lower; value < answerLow {
			answerLow = value
		}
		if value := high[state] + last + upper; value > answerHigh {
			answerHigh = value
		}
	}
	numberOut(int64(answerLow))
	byteOut(' ')
	numberOut(int64(answerHigh))
	byteOut('\n')
	flush()
}
