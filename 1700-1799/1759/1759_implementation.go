package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const (
	dates       = 3
	year        = 365
	leap        = 4
	century     = 100
	leapCentury = 400
	march       = 3
	months      = 12
	// the five months from March to July hold 153 days, and so do August
	// to December, which makes the days before a month a simple formula
	spanDays   = 153
	spanMonths = 5
)

// dayNumber counts days from a fixed origin, with years starting in March
// so that the leap day comes last
func dayNumber(text string) int {
	parts := strings.Split(text, ".")
	d, _ := strconv.Atoi(parts[0])
	m, _ := strconv.Atoi(parts[1])
	y, _ := strconv.Atoi(parts[2])
	if m < march {
		y--
		m += months
	}
	leaps := y/leap - y/century + y/leapCentury
	return year*y + leaps + (spanDays*(m-march)+2)/spanMonths + d
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var n int
	if _, err := fmt.Fscan(reader, &n); err != nil {
		return
	}
	best, answer := -1, 0
	for i := 1; i <= n; i++ {
		var row [dates]string
		for j := range row {
			fmt.Fscan(reader, &row[j])
		}
		life := dayNumber(row[dates-1]) - dayNumber(row[0]) + 1
		// the list goes in order of death, so the first record holder died first
		if life > best {
			best, answer = life, i
		}
	}
	fmt.Println(answer)
}
