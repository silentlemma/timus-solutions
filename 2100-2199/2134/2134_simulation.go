package main

import (
	"fmt"
	"io/ioutil"
	"os"
)

type input struct {
	data []byte
	pos  int
}

func (in *input) integer() int {
	for in.pos < len(in.data) && in.data[in.pos] <= ' ' {
		in.pos++
	}
	value := 0
	for in.pos < len(in.data) && in.data[in.pos] >= '0' && in.data[in.pos] <= '9' {
		value = value*10 + int(in.data[in.pos]-'0')
		in.pos++
	}
	return value
}

func (in *input) token() []byte {
	for in.pos < len(in.data) && in.data[in.pos] <= ' ' {
		in.pos++
	}
	start := in.pos
	for in.pos < len(in.data) && in.data[in.pos] > ' ' {
		in.pos++
	}
	return in.data[start:in.pos]
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	in := input{data: data}
	height, width, limit := in.integer(), in.integer(), in.integer()
	stampHeight, stampWidth := in.integer(), in.integer()
	black := make([]int, 0)
	for row := 0; row < stampHeight; row++ {
		pattern := in.token()
		for column := 0; column < stampWidth; column++ {
			if pattern[column] == '#' {
				black = append(black, row*width+column)
			}
		}
	}

	board := make([]byte, height*width)
	uses := make([]byte, height*width)
	repainted := 0
	operationCount := in.integer()
	for operation := 1; operation <= operationCount; operation++ {
		row, column := in.integer(), in.integer()
		origin := (row-1)*width + column - 1
		if len(black) == 0 || uses[origin] == 2 {
			continue
		}
		uses[origin]++
		// A third use of one placement cannot change any cell state.
		for _, offset := range black {
			index := origin + offset
			if board[index] == 0 {
				board[index] = 1
			} else if board[index] == 1 {
				board[index] = 2
				repainted++
				if repainted == limit {
					fmt.Printf("Wasted after stamp #%d\n", operation)
					return
				}
			}
		}
	}

	output := make([]byte, 0, height*(width+1))
	for row := 0; row < height; row++ {
		for column := 0; column < width; column++ {
			cell := byte('.')
			if board[row*width+column] != 0 {
				cell = '#'
			}
			output = append(output, cell)
		}
		output = append(output, '\n')
	}
	os.Stdout.Write(output)
}
