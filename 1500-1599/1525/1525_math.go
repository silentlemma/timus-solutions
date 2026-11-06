package main

import (
	"bufio"
	"os"
	"strconv"
	"strings"
)

const (
	dimensions = 3
	bufferSize = 4096
	outputSize = 24
	decimal    = 10
)

type axis struct{ size, position, low, high int }

func (a *axis) move(step int) {
	a.position += step
	if a.position < a.low {
		a.low = a.position
	}
	if a.position > a.high {
		a.high = a.position
	}
}

func main() {
	input := bufio.NewReader(os.Stdin)
	header, _ := input.ReadString('\n')
	fields := strings.Fields(header)
	var axes [dimensions]axis
	for i := range axes {
		axes[i].size, _ = strconv.Atoi(fields[i])
	}
	var buffer [bufferSize]byte
	for {
		size, _ := input.Read(buffer[:])
		if size == 0 {
			break
		}
		for _, ch := range buffer[:size] {
			switch ch {
			case 'l':
				axes[0].move(-1)
			case 'r':
				axes[0].move(1)
			case 'd':
				axes[1].move(-1)
			case 'u':
				axes[1].move(1)
			case 'b':
				axes[2].move(-1)
			case 'f':
				axes[2].move(1)
			}
		}
	}
	total := int64(1)
	for _, a := range axes {
		if count := a.size - (a.high - a.low); count > 1 {
			total *= int64(count)
		}
	}
	var output [outputSize]byte
	line := strconv.AppendInt(output[:0], total, decimal)
	os.Stdout.Write(append(line, '\n'))
}
