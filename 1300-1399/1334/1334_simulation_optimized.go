package main

import "syscall"

const boardSize = 8
const padding = 2
const side = boardSize + 2*padding
const wall byte = 255
const white byte = 1
const black byte = 2
const caseBit byte = 32
const moveLimit = 32
const directionCount = 4
const inputSize = 64
const decimalBase = 10

var input [inputSize]byte
var position, available int

func readByte() byte {
	for position == available {
		count, err := syscall.Read(syscall.Stdin, input[:])
		if count > 0 {
			position, available = 0, count
			break
		}
		if err != syscall.EINTR {
			return 0
		}
	}
	c := input[position]
	position++
	return c
}

func writeOutput(pending []byte) {
	for len(pending) > 0 {
		written, err := syscall.Write(syscall.Stdout, pending)
		if written > 0 {
			pending = pending[written:]
		}
		if err == syscall.EINTR {
			continue
		}
		if written <= 0 || err != nil {
			return
		}
	}
}

func writeMove(number int) {
	output := [...]byte{'0' + byte(number/decimalBase), '0' + byte(number%decimalBase), '\n'}
	start := 0
	if number < decimalBase {
		start = 1
	}
	writeOutput(output[start:])
}

func main() {
	var board [side * side]byte
	for index := range board {
		board[index] = wall
	}
	for x := 0; x < boardSize; x++ {
		for y := 0; y < boardSize; y++ {
			board[(x+padding)*side+y+padding] = 0
		}
	}
	directions := [directionCount]int{side + 1, side - 1, -side + 1, -side - 1}
	color := white
	for number := 1; number <= moveLimit; number++ {
		file := readByte()
		for file != 0 && file <= ' ' {
			file = readByte()
		}
		if file == 0 {
			break
		}
		rank := readByte()
		cell := (int(file|caseBit)-'a'+padding)*side + int(rank-'1') + padding
		board[cell] = color
		opposite := white + black - color
		for _, direction := range directions {
			if board[cell+direction] == opposite &&
				(board[cell+2*direction] == 0 || board[cell-direction] == 0) {
				writeMove(number)
				return
			}
		}
		color = opposite
	}
	writeOutput([]byte("Draw\n"))
}
