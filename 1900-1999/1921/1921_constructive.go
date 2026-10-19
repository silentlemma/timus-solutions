package main

import (
	"bufio"
	"fmt"
	"os"
)

func constructBoard(rows, columns, palette, level int) []string {
	target := level - 1
	longest := rows
	if columns > longest {
		longest = columns
	}
	rowColors, columnColors := rows, columns
	if rowColors > 2 {
		rowColors = 2
	}
	if columnColors > 2 {
		columnColors = 2
	}
	if longest < target || palette == 1 && longest != target ||
		palette > 1 && target == 1 && palette < rowColors*columnColors {
		return nil
	}
	board := make([]string, rows)
	for row := 0; row < rows; row++ {
		line := make([]byte, columns)
		for column := 0; column < columns; column++ {
			color := 0
			if palette > 1 {
				if target == 1 {
					color = (row%2)*columnColors + column%2
				} else if columns >= target {
					color = (row + column/target) % 2
				} else {
					color = (column + row/target) % 2
				}
			}
			line[column] = 'A' + byte(color)
		}
		board[row] = string(line)
	}
	return board
}

func main() {
	input := bufio.NewReader(os.Stdin)
	output := bufio.NewWriter(os.Stdout)
	defer output.Flush()
	var rows, columns, palette, level int
	fmt.Fscan(input, &rows, &columns, &palette, &level)
	board := constructBoard(rows, columns, palette, level)
	if board == nil {
		fmt.Fprintln(output, "NO")
	} else {
		fmt.Fprintln(output, "YES")
		for _, row := range board {
			fmt.Fprintln(output, row)
		}
	}
}
