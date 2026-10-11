package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	var n int
	fmt.Scan(&n)
	grid := make([][]int, n)
	for i := range grid {
		grid[i] = make([]int, n)
	}
	number := 1
	// diagonals by column minus row, from the top right corner down
	for shift := n - 1; shift > -n; shift-- {
		for row := 0; row < n; row++ {
			if col := row + shift; col >= 0 && col < n {
				grid[row][col] = number
				number++
			}
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for _, line := range grid {
		for j, v := range line {
			if j > 0 {
				out.WriteByte(' ')
			}
			out.WriteString(strconv.Itoa(v))
		}
		out.WriteByte('\n')
	}
}
