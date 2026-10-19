package main

import (
	"bufio"
	"fmt"
	"os"
)

const cycle = 400
const century = 100
const leapStep = 4
const week = 7
const friday = 4
const targetDay = 13
const months = 12
const buckets = months + 1

var monthLengths = [months]int{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}

func calendarTypes() []int {
	weekday := 0
	types := make([]int, 0, cycle)
	for year := 1; year <= cycle; year++ {
		leap := year%cycle == 0 || (year%leapStep == 0 && year%century != 0)
		count := 0
		for month, days := range monthLengths {
			if (weekday+targetDay-1)%week == friday {
				count++
			}
			if month == 1 && leap {
				days++
			}
			weekday = (weekday + days) % week
		}
		types = append(types, count)
	}
	return types
}

func prefix(year int64, types []int, cycleCounts []int64) []int64 {
	answer := make([]int64, buckets)
	for k, value := range cycleCounts {
		answer[k] = year / cycle * value
	}
	for _, count := range types[:int(year%cycle)] {
		answer[count]++
	}
	return answer
}

func solve(first, last int64, types []int, cycleCounts []int64) []int64 {
	high := prefix(last, types, cycleCounts)
	low := prefix(first-1, types, cycleCounts)
	for k := range high {
		high[k] -= low[k]
	}
	return high
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var first, last int64
	fmt.Fscan(in, &first, &last)
	types := calendarTypes()
	cycleCounts := make([]int64, buckets)
	for _, count := range types {
		cycleCounts[count]++
	}
	for k, value := range solve(first, last, types, cycleCounts) {
		fmt.Fprintf(out, "%d: %d\n", k, value)
	}
}
