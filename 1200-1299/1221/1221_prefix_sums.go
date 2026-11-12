package main

import "syscall"

const maxSide = 100
const rotatedSide = 2 * maxSide
const inputSize = 8192
const outputSize = 32

var input [inputSize]byte
var position, length int
var square [maxSide + 1][maxSide + 1]uint16
var rotated [rotatedSide][rotatedSide]uint16

func nextByte() byte {
	for position == length {
		count, err := syscall.Read(syscall.Stdin, input[:])
		if count > 0 {
			position, length = 0, count
			break
		}
		if err != syscall.EINTR {
			return 0
		}
	}
	value := input[position]
	position++
	return value
}

func firstByte() byte {
	c := nextByte()
	for c != 0 && c <= ' ' {
		c = nextByte()
	}
	return c
}

func number() int {
	c := firstByte()
	value := 0
	for '0' <= c && c <= '9' {
		value = value*10 + int(c-'0')
		c = nextByte()
	}
	return value
}

func squareCount(top, left, bottom, right int) int {
	return int(square[bottom][right]) - int(square[top][right]) -
		int(square[bottom][left]) + int(square[top][left])
}

func rotatedCount(top, left, bottom, right int) int {
	return int(rotated[bottom][right]) - int(rotated[top][right]) -
		int(rotated[bottom][left]) + int(rotated[top][left])
}

func largest(n int) int {
	for radius := (n - 1) / 2; radius >= 1; radius-- {
		area := 2*radius*(radius+1) + 1
		for row := radius; row+radius < n; row++ {
			for column := radius; column+radius < n; column++ {
				if squareCount(row-radius, column-radius, row+radius+1, column+radius+1) != area {
					continue
				}
				u, v := row+column, row-column+n-1
				// The diamond becomes a rectangle; parity holes contribute zero cells.
				if rotatedCount(u-radius, v-radius, u+radius+1, v+radius+1) == area {
					return 2*radius + 1
				}
			}
		}
	}
	return 0
}

func writeAnswer(value int) {
	var output [outputSize]byte
	first := len(output) - 1
	output[first] = '\n'
	if value == 0 {
		first -= len("No solution")
		copy(output[first:], "No solution")
	} else {
		for value > 0 {
			first--
			output[first] = byte(value%10) + '0'
			value /= 10
		}
	}
	buffer := output[first:]
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

func main() {
	for {
		n := number()
		if n == 0 {
			return
		}
		square = [maxSide + 1][maxSide + 1]uint16{}
		rotated = [rotatedSide][rotatedSide]uint16{}
		for row := 0; row < n; row++ {
			for column := 0; column < n; column++ {
				white := uint16(0)
				if firstByte() == '0' {
					white = 1
				}
				square[row+1][column+1] = square[row][column+1] +
					square[row+1][column] - square[row][column] + white
				rotated[row+column+1][row-column+n] = white
			}
		}
		for u := 1; u < 2*n; u++ {
			for v := 1; v < 2*n; v++ {
				rotated[u][v] += rotated[u-1][v] + rotated[u][v-1] - rotated[u-1][v-1]
			}
		}
		writeAnswer(largest(n))
	}
}
