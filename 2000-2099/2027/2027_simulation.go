package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func solve(grid []string, inputs []int) string {
	const alphabet = 26
	const valueLimit = 100000
	const ticks = 1000000
	const directions = 4
	const up = 3
	dr, dc := [directions]int{0, 1, 0, -1}, [directions]int{1, 0, -1, 0}
	memory := [alphabet]int{}
	row, column, direction, current, cursor := 0, 0, 0, 0, 0
	var output strings.Builder
	for tick := 0; tick < ticks; tick++ {
		op := grid[row][column]
		switch op {
		case '#':
			return output.String()
		case '>':
			direction = 0
		case 'v':
			direction = 1
		case '<':
			direction = 2
		case '^':
			direction = up
		case '?':
			current = inputs[cursor]
			if cursor+1 < len(inputs) {
				cursor++
			}
		case '!':
			output.WriteString(strconv.Itoa(current))
			output.WriteByte('\n')
			current = 0
		case '+':
			current++
		case '-':
			current--
		case '@':
			turn := 1
			if current == 0 {
				turn = directions - 1
			}
			direction = (direction + turn) % directions
		default:
			if op >= 'A' && op <= 'Z' {
				index := op - 'A'
				current, memory[index] = memory[index], current
			}
		}
		if current < -valueLimit || current > valueLimit {
			output.WriteString("OVERFLOW ERROR\n")
			return output.String()
		}
		row += dr[direction]
		column += dc[direction]
		if row < 0 || row >= len(grid) || column < 0 || column >= len(grid[0]) {
			output.WriteString("RUNTIME ERROR\n")
			return output.String()
		}
	}
	output.WriteString("TIME LIMIT EXCEEDED\n")
	return output.String()
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var height, width int
	if _, err := fmt.Fscan(in, &height, &width); err != nil {
		return
	}
	grid := make([]string, height)
	for index := range grid {
		fmt.Fscan(in, &grid[index])
	}
	var count int
	fmt.Fscan(in, &count)
	inputs := make([]int, count)
	for index := range inputs {
		fmt.Fscan(in, &inputs[index])
	}
	fmt.Print(solve(grid, inputs))
}
