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

const outputSize = 10000

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

const maxPlayers = 1000
const scores = 7
const teams = 2

var head [teams][scores]uint16
var nextID [teams][maxPlayers + 1]uint16

func take(team int, score *int, step int) int {
	for head[team][*score] == 0 {
		*score += step
	}
	id := head[team][*score]
	head[team][*score] = nextID[team][id]
	return int(id)
}

func main() {
	n := number()
	var totals [teams]int
	for team := 0; team < teams; team++ {
		for id := 1; id <= n; id++ {
			score := number()
			totals[team] += score
			nextID[team][id] = head[team][score]
			head[team][score] = uint16(id)
		}
	}
	step, score := [teams]int{1, 1}, [teams]int{}
	if totals[0] > totals[1] {
		step[1], score[1] = -1, scores-1
	} else if totals[0] < totals[1] {
		step[0], score[0] = -1, scores-1
	}
	for round := 0; round < n; round++ {
		first, second := take(0, &score[0], step[0]), take(1, &score[1], step[1])
		writeNumber(first)
		output[used] = ' '
		used++
		writeNumber(second)
		output[used] = '\n'
		used++
	}
	writeAll(output[:used])
}
