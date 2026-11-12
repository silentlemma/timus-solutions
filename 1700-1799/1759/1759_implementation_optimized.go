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

const yearDays = 365
const leapPeriod = 4
const century = 100
const leapCentury = 400
const february = 2

var beforeMonth = [...]int{0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334}

func dayNumber() int {
	day, month, year := number(), number(), number()
	previous := year - 1
	days := previous*yearDays + previous/leapPeriod - previous/century + previous/leapCentury
	days += beforeMonth[month-1] + day
	if month > february && year%leapPeriod == 0 &&
		(year%century != 0 || year%leapCentury == 0) {
		days++
	}
	return days
}

func main() {
	n := number()
	best, answer := -1, 0
	for id := 1; id <= n; id++ {
		born := dayNumber()
		dayNumber()
		died := dayNumber()
		life := died - born + 1
		if life > best {
			best, answer = life, id
		}
	}
	writeNumber(answer)
	output[used] = '\n'
	used++
	writeAll(output[:used])
}
