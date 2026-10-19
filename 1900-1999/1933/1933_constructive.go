package main

import (
	"bufio"
	"fmt"
	"os"
)

func buildSchedule(cannons int) [][]int {
	size := 2*cannons + 1
	schedule := make([][]int, size)
	for row := range schedule {
		schedule[row] = make([]int, size)
		for column := range schedule[row] {
			if row != column {
				schedule[row][column] = (row+column+size-1)%size + 1
			}
		}
	}
	return schedule
}

func main() {
	input, output := bufio.NewReader(os.Stdin), bufio.NewWriter(os.Stdout)
	defer output.Flush()
	var cannons int
	fmt.Fscan(input, &cannons)
	for _, row := range buildSchedule(cannons) {
		for column, value := range row {
			if column > 0 {
				fmt.Fprint(output, " ")
			}
			fmt.Fprint(output, value)
		}
		fmt.Fprintln(output)
	}
}
