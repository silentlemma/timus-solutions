package main

import (
	"fmt"
	"strings"
)

var days = []string{"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}

// days from September 1 to the first day of each month
var months = map[string]int{"September": 0, "October": 30, "November": 61, "December": 91}

func main() {
	var first, month string
	var day, a, b int
	fmt.Scan(&first, &month, &day, &a, &b)
	week, start := len(days), 0
	for days[start] != first {
		start++
	}
	match := months[month] + day - 1 // September 1 is day 0
	count := make([]int, week)       // training days from September 2 to the eve of the match
	for i := 1; i < match; i++ {
		count[(start+i)%week]++
	}
	for mask := 1; mask < 1<<week; mask++ {
		var chosen []string
		total := 0
		for d := 0; d < week; d++ {
			if mask>>d&1 == 1 {
				chosen = append(chosen, days[d])
				total += count[d]
			}
		}
		if a <= total && total <= b {
			fmt.Println(len(chosen))
			fmt.Println(strings.Join(chosen, "\n"))
			return
		}
	}
	fmt.Println("Impossible")
}
