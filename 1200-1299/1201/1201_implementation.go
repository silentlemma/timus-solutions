package main

import (
	"fmt"
	"strings"
)

const (
	week    = 7
	year    = 365
	cell    = 5
	leap    = 4
	century = 100
	era     = 400
)

var names = [week]string{"mon", "tue", "wed", "thu", "fri", "sat", "sun"}

var monthLengths = [...]int{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}

func main() {
	lengths := monthLengths
	var d, m, y int
	fmt.Scan(&d, &m, &y)
	if y%leap == 0 && (y%century != 0 || y%era == 0) {
		lengths[1]++
	}
	// days from 1 January of year 1, a Monday, to the first of the month
	past := y - 1
	before := year*past + past/leap - past/century + past/era
	for _, l := range lengths[:m-1] {
		before += l
	}
	first, days := before%week, lengths[m-1]
	cols := (first + days + week - 1) / week
	for row, name := range names {
		var line strings.Builder
		line.WriteString(name)
		for col := 0; col < cols; col++ {
			day := col*week + row - first + 1
			last := col == cols-1
			// every column is five characters wide, the last one four,
			// unless the bracketed date sits in it
			switch {
			case day == d:
				fmt.Fprintf(&line, " [%2d]", day)
			case day >= 1 && day <= days && last:
				fmt.Fprintf(&line, "  %2d", day)
			case day >= 1 && day <= days:
				fmt.Fprintf(&line, "  %2d ", day)
			case last:
				line.WriteString(strings.Repeat(" ", cell-1))
			default:
				line.WriteString(strings.Repeat(" ", cell))
			}
		}
		fmt.Println(line.String())
	}
}
