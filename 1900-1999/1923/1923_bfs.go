package main

import (
	"bufio"
	"fmt"
	"os"
)

func territorySizes(board []string, moves []int) (int, int) {
	rows, columns := len(board), len(board[0])
	cells := rows * columns
	colors := make([]byte, 0, cells)
	for _, row := range board {
		colors = append(colors, row...)
	}
	neighbors := make([][]int, cells)
	for row := 0; row < rows; row++ {
		for column := 0; column < columns; column++ {
			cell := row*columns + column
			if row > 0 {
				neighbors[cell] = append(neighbors[cell], cell-columns)
			}
			if row+1 < rows {
				neighbors[cell] = append(neighbors[cell], cell+columns)
			}
			if column > 0 {
				neighbors[cell] = append(neighbors[cell], cell-1)
			}
			if column+1 < columns {
				neighbors[cell] = append(neighbors[cell], cell+1)
			}
		}
	}
	owners := make([]int, cells)
	for index := range owners {
		owners[index] = -1
	}
	territories := [2][]int{}
	expand := func(player int, color byte) {
		for cursor := 0; cursor < len(territories[player]); cursor++ {
			cell := territories[player][cursor]
			for _, adjacent := range neighbors[cell] {
				if owners[adjacent] == -1 && colors[adjacent] == color {
					owners[adjacent] = player
					territories[player] = append(territories[player], adjacent)
				}
			}
		}
	}
	for player, seed := range []int{cells - columns, columns - 1} {
		owners[seed] = player
		territories[player] = append(territories[player], seed)
		expand(player, colors[seed])
	}
	for turn, color := range moves {
		expand(turn%2, '0'+byte(color))
	}
	return len(territories[0]), len(territories[1])
}

func main() {
	input := bufio.NewReader(os.Stdin)
	output := bufio.NewWriter(os.Stdout)
	defer output.Flush()
	var rows, columns int
	fmt.Fscan(input, &rows, &columns)
	board := make([]string, rows)
	for row := range board {
		fmt.Fscan(input, &board[row])
	}
	var count int
	fmt.Fscan(input, &count)
	moves := make([]int, count)
	for index := range moves {
		fmt.Fscan(input, &moves[index])
	}
	first, second := territorySizes(board, moves)
	fmt.Fprintln(output, first)
	fmt.Fprintln(output, second)
}
