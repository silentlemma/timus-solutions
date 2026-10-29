package main

import (
	"bufio"
	"os"
)

const bufferSize = 4096

var input = bufio.NewReaderSize(os.Stdin, bufferSize)

// the balls are parsed by hand from a buffered reader, faster than fmt.Fscan
func nextInt() int {
	value := 0
	c, err := input.ReadByte()
	for err == nil && c <= ' ' {
		c, err = input.ReadByte()
	}
	for err == nil && c >= '0' && c <= '9' {
		value = value*10 + int(c-'0')
		c, err = input.ReadByte()
	}
	return value
}

func main() {
	n := nextInt()
	// the pocket is a stack: roll the balls in order, and whenever the top
	// one is the next ball the inspector took out, take it out; the ball
	// numbers are at most 100 000 and fit int32
	pocket := make([]int32, n)
	top, next := 0, 1
	// the balls are checked as they are read: roll in every ball up to this one,
	// then it must be on top; the list of taken balls is never stored
	for i := 0; i < n; i++ {
		ball := nextInt()
		for next <= ball {
			pocket[top] = int32(next)
			top++
			next++
		}
		if top == 0 || pocket[top-1] != int32(ball) {
			os.Stdout.WriteString("Cheater\n")
			return
		}
		top--
	}
	os.Stdout.WriteString("Not a proof\n")
}
