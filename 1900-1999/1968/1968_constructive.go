package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

const blockSide = 2

func reconstruct(photo [][]int) [][]string {
	rows, columns := len(photo), len(photo[0])
	counts := make([][]int, rows)
	for row := range counts {
		counts[row] = make([]int, columns)
	}
	for row := 0; row < rows; row++ {
		for column := 0; column < columns; column++ {
			value := photo[row][column]
			if row > 0 {
				value -= counts[row-1][column]
			}
			if column > 0 {
				value -= counts[row][column-1]
			}
			if row > 0 && column > 0 {
				value -= counts[row-1][column-1]
			}
			counts[row][column] = value
		}
	}
	height := rows / blockSide
	if columns/blockSide < height {
		height = columns / blockSide
	}
	layers := make([][]string, 0, height)
	for level := 0; level < height; level++ {
		layer := []string{}
		for row := 0; row < rows/blockSide-level; row++ {
			var line strings.Builder
			for column := 0; column < columns/blockSide-level; column++ {
				x, y := level+blockSide*row, level+blockSide*column
				if counts[x][y] > level/blockSide {
					line.WriteByte('R')
				} else {
					line.WriteByte('W')
				}
			}
			layer = append(layer, line.String())
		}
		layers = append(layers, layer)
	}
	return layers
}

func main() {
	input := bufio.NewReader(os.Stdin)
	output := bufio.NewWriter(os.Stdout)
	defer output.Flush()
	var rows, columns int
	fmt.Fscan(input, &rows, &columns)
	photo := make([][]int, rows)
	for row := range photo {
		photo[row] = make([]int, columns)
		for column := range photo[row] {
			fmt.Fscan(input, &photo[row][column])
		}
	}
	layers := reconstruct(photo)
	for level, layer := range layers {
		if level > 0 {
			fmt.Fprintln(output)
		}
		for _, line := range layer {
			fmt.Fprintln(output, line)
		}
	}
}
