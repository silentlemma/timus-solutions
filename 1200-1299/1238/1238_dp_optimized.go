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

const maxLength = 100
const decimalBase = 10
const brackets = 2

var text [maxLength]byte
var best [maxLength][maxLength]uint8
var choice [maxLength][maxLength]int8
var lcp [maxLength + 1][maxLength + 1]uint8
var repeatDigits [maxLength + 1]uint8

func emit(left, right int) {
	decision := int(choice[left][right])
	if decision > 0 {
		emit(left, decision-1)
		emit(decision, right)
	} else if decision < 0 {
		period := -decision
		writeNumber((right - left + 1) / period)
		output[used] = '('
		used++
		emit(left, left+period-1)
		output[used] = ')'
		used++
	} else {
		used += copy(output[used:], text[left:right+1])
	}
}

func main() {
	c := nextByte()
	for c != 0 && c <= ' ' {
		c = nextByte()
	}
	n := 0
	for c > ' ' {
		text[n] = c
		n++
		c = nextByte()
	}
	for value := 1; value <= n; value++ {
		repeatDigits[value] = repeatDigits[value/decimalBase] + 1
	}
	for i := n - 1; i >= 0; i-- {
		for j := n - 1; j >= 0; j-- {
			if text[i] == text[j] {
				lcp[i][j] = lcp[i+1][j+1] + 1
			}
		}
	}
	for size := 1; size <= n; size++ {
		for left := 0; left+size <= n; left++ {
			right := left + size - 1
			best[left][right] = uint8(size)
			for split := left + 1; split <= right; split++ {
				cost := best[left][split-1] + best[split][right]
				if cost < best[left][right] {
					best[left][right] = cost
					choice[left][right] = int8(split)
				}
			}
			for period := 1; period <= size/2; period++ {
				// LCP is at most 100; a folding never needs more bytes than the raw interval.
				if size%period != 0 || int(lcp[left][left+period]) < size-period {
					continue
				}
				cost := repeatDigits[size/period] + brackets + best[left][left+period-1]
				if cost < best[left][right] {
					best[left][right] = cost
					choice[left][right] = -int8(period)
				}
			}
		}
	}
	emit(0, n-1)
	output[used] = '\n'
	used++
	writeAll(output[:used])
}
