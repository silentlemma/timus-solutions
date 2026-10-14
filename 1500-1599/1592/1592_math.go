package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

const (
	minute = 60
	hour   = 60 * minute
	cycle  = 12 * hour // the dial shows the same after 12 hours
	twelve = 12
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	if _, err := fmt.Fscan(in, &n); err != nil {
		return
	}
	times := make([]int64, n)
	total := int64(0)
	for i := range times {
		var word string
		fmt.Fscan(in, &word)
		parts := strings.Split(word, ":")
		h, _ := strconv.Atoi(parts[0])
		m, _ := strconv.Atoi(parts[1])
		s, _ := strconv.Atoi(parts[2])
		times[i] = int64(h%twelve*hour + m*minute + s) // 12 o'clock is 0
		total += times[i]
	}
	sort.Slice(times, func(a, b int) bool { return times[a] < times[b] })
	// winding clock i forward to t costs t - time_i, plus a full cycle when
	// the clock shows a later time than t; moving t back to the nearest
	// clock time only helps, so only the clock times are tried
	best, bestCost := int64(0), int64(-1)
	j := 0 // clocks showing at most t
	for _, t := range times {
		for j < n && times[j] <= t {
			j++
		}
		cost := int64(n)*t - total + cycle*int64(n-j)
		if bestCost < 0 || cost < bestCost {
			best, bestCost = t, cost
		}
	}
	h, rest := best/hour, best%hour
	if h == 0 {
		h = twelve
	}
	fmt.Printf("%d:%02d:%02d\n", h, rest/minute, rest%minute)
}
