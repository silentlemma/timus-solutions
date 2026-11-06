package main

import (
	"bufio"
	"os"
	"strconv"
)

const (
	maxPairs   = 100
	maxSize    = 2*maxPairs + 1
	fieldWidth = 4
	decimal    = 10
)

func main() {
	input := bufio.NewScanner(os.Stdin)
	input.Split(bufio.ScanWords)
	if !input.Scan() {
		return
	}
	pairs, _ := strconv.Atoi(input.Text())
	size := 2*pairs + 1
	output := bufio.NewWriter(os.Stdout)
	var buffer [maxSize * fieldWidth]byte
	for row := 0; row < size; row++ {
		line := buffer[:0]
		round := row
		if round == 0 {
			round = size
		}
		for column := 0; column < size; column++ {
			if column != 0 {
				line = append(line, ' ')
			}
			value := round
			if column == row {
				value = 0
			}
			line = strconv.AppendInt(line, int64(value), decimal)
			round++
			if round > size {
				round = 1
			}
		}
		output.Write(append(line, '\n'))
	}
	output.Flush()
}
