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

const inputSize = 8192

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

const maxFigures = 1000
const maxRules = 4000
const wordBits = 64
const figureWords = (maxFigures + wordBits - 1) / wordBits
const ruleWords = (maxRules + wordBits - 1) / wordBits

var needs [maxFigures][ruleWords]uint64
var added [maxRules][figureWords]uint64
var owned [figureWords]uint64
var remaining [maxRules]uint16
var queue [maxFigures]uint16
var tail, words int

func digit() bool {
	c := nextByte()
	for c != 0 && c <= ' ' {
		c = nextByte()
	}
	return c == '1'
}

func give(word int, figures uint64) {
	fresh := figures &^ owned[word]
	owned[word] |= figures
	for fresh != 0 {
		queue[tail] = uint16(word*wordBits + bits.TrailingZeros64(fresh))
		tail++
		fresh &= fresh - 1
	}
}

func fire(rule int) {
	for word := 0; word < words; word++ {
		give(word, added[rule][word])
	}
}

func main() {
	n, m := number(), number()
	words = (n + wordBits - 1) / wordBits
	ruleCount := (m + wordBits - 1) / wordBits
	for rule := 0; rule < m; rule++ {
		for figure := 0; figure < n; figure++ {
			if digit() {
				needs[figure][rule/wordBits] |= uint64(1) << uint(rule%wordBits)
				remaining[rule]++
			}
		}
		for figure := 0; figure < n; figure++ {
			if digit() {
				added[rule][figure/wordBits] |= uint64(1) << uint(figure%wordBits)
			}
		}
	}
	for figure := 0; figure < n; figure++ {
		if digit() {
			give(figure/wordBits, uint64(1)<<uint(figure%wordBits))
		}
	}
	for rule := 0; rule < m; rule++ {
		if remaining[rule] == 0 {
			fire(rule)
		}
	}
	for head := 0; head < tail; head++ {
		figure := queue[head]
		for word := 0; word < ruleCount; word++ {
			rules := needs[figure][word]
			for rules != 0 {
				rule := word*wordBits + bits.TrailingZeros64(rules)
				remaining[rule]--
				if remaining[rule] == 0 {
					fire(rule)
				}
				rules &= rules - 1
			}
		}
	}
	var output [maxFigures + 1]byte
	for figure := 0; figure < n; figure++ {
		output[figure] = '0' + byte(owned[figure/wordBits]>>uint(figure%wordBits)&1)
	}
	output[n] = '\n'
	writeAll(output[:n+1])
}
