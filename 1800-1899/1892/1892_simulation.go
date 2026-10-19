package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const (
	secondsPerMinute = 60
	secondsPerHour   = secondsPerMinute * secondsPerMinute
	maxInterval      = 500
)

func readTime(in *bufio.Reader) int {
	var text string
	fmt.Fscan(in, &text)
	parts := strings.Split(text, ":")
	hour, _ := strconv.Atoi(parts[0])
	minute, _ := strconv.Atoi(parts[1])
	second, _ := strconv.Atoi(parts[2])
	return hour*secondsPerHour + minute*secondsPerMinute + second
}

func latest(a, b, c int) int {
	if b > a {
		a = b
	}
	if c > a {
		a = c
	}
	return a
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var takeTake, takeLand, landTake, landLand, n, m int
	fmt.Fscan(in, &takeTake, &takeLand, &landTake, &landLand, &n)
	departures, takeResult := make([]int, n), make([]int, 0, n)
	for i := range departures {
		departures[i] = readTime(in)
	}
	fmt.Fscan(in, &m)
	landings, landResult := make([]int, m), make([]int, 0, m)
	for i := range landings {
		landings[i] = readTime(in)
	}
	takeIndex, landIndex := 0, 0
	lastTake, lastLand := -maxInterval, -maxInterval
	for takeIndex < n || landIndex < m {
		ready := 0
		if takeIndex < n {
			ready = latest(departures[takeIndex], lastTake+takeTake, lastLand+landTake)
		}
		if landIndex < m && (takeIndex == n || landings[landIndex] <= ready) {
			lastLand = latest(landings[landIndex], lastTake+takeLand, lastLand+landLand)
			landResult = append(landResult, lastLand)
			landIndex++
		} else {
			lastTake = ready
			takeResult = append(takeResult, lastTake)
			takeIndex++
		}
	}
	for _, seconds := range append(takeResult, landResult...) {
		hour := seconds / secondsPerHour
		minute := seconds / secondsPerMinute % secondsPerMinute
		second := seconds % secondsPerMinute
		fmt.Fprintf(out, "%02d:%02d:%02d\n", hour, minute, second)
	}
}
