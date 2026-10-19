package main

import (
	"bufio"
	"fmt"
	"os"
)

const secondsPerMinute = 60
const minutesPerHour = 60
const secondsPerHour = secondsPerMinute * minutesPerHour

type schedule struct {
	duration, trips int
	departures      []int
}

func recover(first int, passages []int) schedule {
	count := len(passages)
	offset, last := passages[0]-first, passages[len(passages)-1]
	totalSpan := last - first + offset
	present := make([]bool, last+1)
	marked := make([]int, last+1)
	for _, time := range passages {
		present[time] = true
	}
	epoch := 0
	for index := 1; index <= count/2; index++ {
		period := passages[index] - first + offset
		if period%2 != 0 || period <= 2*offset {
			continue
		}
		trips := totalSpan / period
		if trips == 0 || count%(2*trips) != 0 {
			continue
		}
		tramCount, gap := count/(2*trips), period-2*offset
		epoch++
		departures := []int{}
		failed := false
		for _, time := range passages {
			if marked[time] == epoch {
				continue
			}
			departure := time - offset
			if departure >= first+period || len(departures) == tramCount {
				failed = true
				break
			}
			outward := time
			for trip := 0; trip < trips; trip++ {
				returning := outward + gap
				if outward > last || returning > last || !present[outward] || !present[returning] ||
					marked[outward] == epoch || marked[returning] == epoch {
					failed = true
					break
				}
				marked[outward] = epoch
				marked[returning] = epoch
				outward += period
			}
			if failed {
				break
			}
			departures = append(departures, departure)
		}
		if !failed && len(departures) == tramCount {
			return schedule{period / 2, trips, departures}
		}
	}
	panic("The guaranteed schedule was not found")
}

func parseTime(text string) int {
	var hours, minutes, seconds int
	fmt.Sscanf(text, "%d:%d:%d", &hours, &minutes, &seconds)
	return hours*secondsPerHour + minutes*secondsPerMinute + seconds
}
func formatTime(value int) string {
	return fmt.Sprintf("%02d:%02d:%02d", value/secondsPerHour,
		value/secondsPerMinute%minutesPerHour, value%secondsPerMinute)
}

func main() {
	input := bufio.NewReader(os.Stdin)
	output := bufio.NewWriter(os.Stdout)
	defer output.Flush()
	var text string
	fmt.Fscan(input, &text)
	first := parseTime(text)
	passages := []int{}
	for {
		if _, err := fmt.Fscan(input, &text); err != nil {
			break
		}
		passages = append(passages, parseTime(text))
	}
	answer := recover(first, passages)
	for _, departure := range answer.departures {
		for step := 0; step <= 2*answer.trips; step++ {
			if step > 0 {
				fmt.Fprint(output, " ")
			}
			fmt.Fprint(output, formatTime(departure+step*answer.duration))
		}
		fmt.Fprintln(output)
	}
}
