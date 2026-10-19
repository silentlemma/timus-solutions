package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const width = 10
const rows = 4

var days = []string{"Tuesday", "Thursday", "Saturday"}

func wrap(name string) []string {
	lines := []string{""}
	for _, word := range strings.Fields(name) {
		last := len(lines) - 1
		if lines[last] == "" {
			lines[last] = word
		} else if len(lines[last])+1+len(word) <= width {
			lines[last] += " " + word
		} else {
			lines = append(lines, word)
		}
	}
	return lines
}

func main() {
	in := bufio.NewScanner(os.Stdin)
	in.Scan()
	n, _ := strconv.Atoi(in.Text())
	grid := make([][][]string, rows)
	for i := range grid {
		grid[i] = make([][]string, len(days))
	}
	for i := 0; i < n; i++ {
		in.Scan()
		name := in.Text()
		in.Scan()
		var day string
		var lesson int
		fmt.Sscan(in.Text(), &day, &lesson)
		for column, value := range days {
			if day == value {
				grid[lesson-1][column] = wrap(name)
			}
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	border := "+" + strings.Repeat(strings.Repeat("-", width)+"+", len(days))
	fmt.Fprintln(out, border)
	for _, row := range grid {
		height := 1
		for _, cell := range row {
			if len(cell) > height {
				height = len(cell)
			}
		}
		for level := 0; level < height; level++ {
			fmt.Fprint(out, "|")
			for _, cell := range row {
				line := ""
				if level < len(cell) {
					line = cell[level]
				}
				fmt.Fprint(out, line, strings.Repeat(" ", width-len(line)), "|")
			}
			fmt.Fprintln(out)
		}
		fmt.Fprintln(out, border)
	}
}
