package main

import (
	"bufio"
	"os"
	"strconv"
)

const (
	decimal        = 10
	outputCapacity = 128
)

func number(input *bufio.Reader) int {
	ch, err := input.ReadByte()
	for err == nil && ch <= ' ' {
		ch, err = input.ReadByte()
	}
	value := 0
	for err == nil && ch >= '0' && ch <= '9' {
		value = decimal*value + int(ch-'0')
		ch, err = input.ReadByte()
	}
	return value
}

type bounds struct{ low, high int }

func (b *bounds) include(value int) {
	if value < b.low {
		b.low = value
	}
	if value > b.high {
		b.high = value
	}
}

func main() {
	input := bufio.NewReader(os.Stdin)
	n := number(input)
	x, y := number(input), number(input)
	xs, ys := bounds{x, x}, bounds{y, y}
	sums, diffs := bounds{x + y, x + y}, bounds{x - y, x - y}
	for i := 1; i < n; i++ {
		x, y = number(input), number(input)
		xs.include(x)
		ys.include(y)
		sums.include(x + y)
		diffs.include(x - y)
	}
	type point struct{ x, y int }
	corners := [...]point{
		{sums.low - ys.low, ys.low}, {diffs.high + ys.low, ys.low},
		{xs.high, xs.high - diffs.high}, {xs.high, sums.high - xs.high},
		{sums.high - ys.high, ys.high}, {diffs.low + ys.high, ys.high},
		{xs.low, xs.low - diffs.low}, {xs.low, sums.low - xs.low},
	}
	var storage [outputCapacity]byte
	output := storage[:0]
	previous := corners[len(corners)-1]
	for _, p := range corners {
		if p != previous {
			output = strconv.AppendInt(output, int64(p.x), decimal)
			output = append(output, ' ')
			output = strconv.AppendInt(output, int64(p.y), decimal)
			output = append(output, '\n')
		}
		previous = p
	}
	if len(output) == 0 {
		output = strconv.AppendInt(output, int64(previous.x), decimal)
		output = append(output, ' ')
		output = strconv.AppendInt(output, int64(previous.y), decimal)
		output = append(output, '\n')
	}
	os.Stdout.Write(output)
}
