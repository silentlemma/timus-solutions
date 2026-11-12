package main

import (
	"bufio"
	"os"
	"strconv"
)

const bufferSize = 8192
const decimalBase = 10
const numberReserve = 16
const alphabet = 26
const valueLimit = 100000
const tickLimit = 1000000
const directions = 4
const directionMask = directions - 1

const (
	opOutside byte = iota
	opRight
	opDown
	opLeft
	opUp
	opNop
	opHalt
	opInput
	opOutput
	opIncrement
	opDecrement
	opTurn
	opRegister
)

func character(in *bufio.Reader) byte {
	c, _ := in.ReadByte()
	for c != 0 && c <= ' ' {
		c, _ = in.ReadByte()
	}
	return c
}

func number(in *bufio.Reader) int32 {
	c := character(in)
	negative := c == '-'
	if c == '-' || c == '+' {
		c, _ = in.ReadByte()
	}
	value := int32(0)
	for c >= '0' && c <= '9' {
		value = value*decimalBase + int32(c-'0')
		c, _ = in.ReadByte()
	}
	if negative {
		return -value
	}
	return value
}

func instruction(c byte) byte {
	switch c {
	case '>':
		return opRight
	case 'v':
		return opDown
	case '<':
		return opLeft
	case '^':
		return opUp
	case '#':
		return opHalt
	case '?':
		return opInput
	case '!':
		return opOutput
	case '+':
		return opIncrement
	case '-':
		return opDecrement
	case '@':
		return opTurn
	}
	if c >= 'A' && c <= 'Z' {
		return opRegister + c - 'A'
	}
	return opNop
}

func main() {
	in := bufio.NewReaderSize(os.Stdin, bufferSize)
	height, width := int(number(in)), int(number(in))
	stride := width + 2
	program := make([]byte, (height+2)*stride)
	for row := 1; row <= height; row++ {
		for col := 1; col <= width; col++ {
			program[row*stride+col] = instruction(character(in))
		}
	}
	remaining := number(in)
	var memory [alphabet]int32
	last, current := int32(0), int32(0)
	position, direction := stride+1, 0
	moves := [directions]int{1, stride, -1, -stride}
	output := make([]byte, 0, bufferSize)
	finish := func(message string) { os.Stdout.Write(output); os.Stdout.WriteString(message) }
	for tick := 0; tick < tickLimit; tick++ {
		op := program[position]
		if op == opHalt {
			finish("")
			return
		}
		if op <= opUp {
			direction = int(op - opRight)
		} else if op >= opRegister {
			index := op - opRegister
			current, memory[index] = memory[index], current
		} else {
			switch op {
			case opInput:
				if remaining > 0 {
					last = number(in)
					remaining--
				}
				current = last
			case opOutput:
				if len(output)+numberReserve > cap(output) {
					os.Stdout.Write(output)
					output = output[:0]
				}
				output = strconv.AppendInt(output, int64(current), decimalBase)
				output = append(output, '\n')
				current = 0
			case opIncrement:
				current++
			case opDecrement:
				current--
			case opTurn:
				turn := 1
				if current == 0 {
					turn = directionMask
				}
				direction = (direction + turn) & directionMask
			}
		}
		if current < -valueLimit || current > valueLimit {
			finish("OVERFLOW ERROR\n")
			return
		}
		position += moves[direction]
		if program[position] == opOutside {
			finish("RUNTIME ERROR\n")
			return
		}
	}
	finish("TIME LIMIT EXCEEDED\n")
}
