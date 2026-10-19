package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

type point struct{ x, y int }

func draw(points []point) string {
	left, right, lower, upper := 0, 0, 0, 0
	for _, p := range points {
		if p.x < left {
			left = p.x
		}
		if p.x > right {
			right = p.x
		}
		if p.y < lower {
			lower = p.y
		}
		if p.y > upper {
			upper = p.y
		}
	}
	width := right - left + 1
	grid := make([][]byte, upper-lower+1)
	for row := range grid {
		grid[row] = make([]byte, width)
		for column := range grid[row] {
			grid[row][column] = '.'
		}
		grid[row][-left] = '|'
	}
	for column := range grid[upper] {
		grid[upper][column] = '-'
	}
	grid[upper][-left] = '+'
	for _, p := range points {
		grid[upper-p.y][p.x-left] = '*'
	}
	var output strings.Builder
	for _, row := range grid {
		output.Write(row)
		output.WriteByte('\n')
	}
	return output.String()
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var size int
	fmt.Fscan(in, &size)
	points := make([]point, size)
	for index := range points {
		fmt.Fscan(in, &points[index].x, &points[index].y)
	}
	fmt.Fprint(out, draw(points))
}
