package main

import (
	"bufio"
	"os"
	"strconv"
)

const (
	bufferSize = 4096
	outputSize = 16
	base       = 10
)

func extend(packed, color uint16) uint16 {
	if packed&1 == color {
		return packed + 2
	}
	return 2 + color
}

func main() {
	input := bufio.NewScanner(os.Stdin)
	var buffer [bufferSize]byte
	input.Buffer(buffer[:], len(buffer))
	input.Split(bufio.ScanWords)
	if !input.Scan() {
		return
	}
	width, _ := strconv.Atoi(input.Text())
	down, right, left := make([]uint16, width), make([]uint16, width), make([]uint16, width+1)
	var best [2]uint16
	for y := 0; y < width && input.Scan(); y++ {
		row := input.Bytes()
		var across, previousRight uint16
		for x, grain := range row {
			var color uint16
			if grain == 'S' {
				color = 1
			}
			across = extend(across, color)
			down[x] = extend(down[x], color)
			left[x] = extend(left[x+1], color)
			right[x], previousRight = extend(previousRight, color), right[x]
			for _, run := range [...]uint16{across, down[x], left[x], right[x]} {
				if run > best[color] {
					best[color] = run
				}
			}
		}
	}
	lower, upper := best[0]>>1, best[1]>>1
	winner, longest := byte('?'), lower
	if lower > upper {
		winner = 's'
	} else if upper > lower {
		winner, longest = 'S', upper
	}
	var output [outputSize]byte
	line := append(output[:0], winner, '\n')
	line = strconv.AppendUint(line, uint64(longest), base)
	os.Stdout.Write(append(line, '\n'))
}
