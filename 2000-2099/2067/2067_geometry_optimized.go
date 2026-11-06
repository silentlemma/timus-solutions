package main

import (
	"bufio"
	"os"
	"strconv"
)

const (
	bufferSize = 4096
	outputSize = 24
	decimal    = 10
)

func number(input *bufio.Scanner) int64 {
	input.Scan()
	token := input.Bytes()
	negative := token[0] == '-'
	if negative || token[0] == '+' {
		token = token[1:]
	}
	var value int64
	for _, digit := range token {
		value = value*decimal + int64(digit-'0')
	}
	if negative {
		return -value
	}
	return value
}

func main() {
	input := bufio.NewScanner(os.Stdin)
	var buffer [bufferSize]byte
	input.Buffer(buffer[:], len(buffer))
	input.Split(bufio.ScanWords)
	count := int(number(input))
	x, y := number(input), number(input)
	nextX, nextY := number(input), number(input)
	dx, dy := nextX-x, nextY-y
	vertical := dx == 0
	low := x
	if vertical {
		low = y
	}
	high, lowID, highID := low, 1, 1
	for i := 2; i <= count; i++ {
		currentX, currentY := nextX, nextY
		if i != 2 {
			currentX, currentY = number(input), number(input)
		}
		if dx*(currentY-y) != dy*(currentX-x) {
			os.Stdout.WriteString("0\n")
			return
		}
		coordinate := currentX
		if vertical {
			coordinate = currentY
		}
		if coordinate < low {
			low, lowID = coordinate, i
		}
		if coordinate > high {
			high, highID = coordinate, i
		}
	}
	var storage [outputSize]byte
	line := append(storage[:0], '1', '\n')
	line = strconv.AppendInt(line, int64(lowID), decimal)
	line = append(line, ' ')
	line = strconv.AppendInt(line, int64(highID), decimal)
	os.Stdout.Write(append(line, '\n'))
}
