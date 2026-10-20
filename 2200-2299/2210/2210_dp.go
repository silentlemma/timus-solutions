package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

const maxValue = 100

type line struct {
	slope     int64
	intercept int64
}

type option struct {
	cost   int
	income int
}

type richState struct {
	day    int
	income int
	money  int64
}

func makeHull(lines []line) []line {
	sort.Slice(lines, func(i, j int) bool {
		if lines[i].slope != lines[j].slope {
			return lines[i].slope < lines[j].slope
		}
		return lines[i].intercept < lines[j].intercept
	})
	hull := make([]line, 0, len(lines))
	for _, current := range lines {
		if len(hull) > 0 && hull[len(hull)-1].slope == current.slope {
			if hull[len(hull)-1].intercept >= current.intercept {
				continue
			}
			hull = hull[:len(hull)-1]
		}
		for len(hull) >= 2 {
			a, b := hull[len(hull)-2], hull[len(hull)-1]
			left := (a.intercept - b.intercept) * (current.slope - b.slope)
			right := (b.intercept - current.intercept) * (b.slope - a.slope)
			if left < right {
				break
			}
			hull = hull[:len(hull)-1]
		}
		hull = append(hull, current)
	}
	return hull
}

func maximum(hull []line, day int64) int64 {
	left, right := 0, len(hull)-1
	for left < right {
		middle := (left + right) / 2
		a, b := hull[middle], hull[middle+1]
		if a.slope*day+a.intercept <= b.slope*day+b.intercept {
			left = middle + 1
		} else {
			right = middle
		}
	}
	return hull[left].slope*day + hull[left].intercept
}

func emptyStates(count int) []int64 {
	states := make([]int64, count)
	for index := range states {
		states[index] = -1
	}
	return states
}

func hasStates(states []int64) bool {
	for _, money := range states {
		if money >= 0 {
			return true
		}
	}
	return false
}

func update(target *int64, candidate int64) {
	if candidate > *target {
		*target = candidate
	}
}

func main() {
	input := bufio.NewReader(os.Stdin)
	output := bufio.NewWriter(os.Stdout)
	defer output.Flush()
	var count int
	fmt.Fscan(input, &count)
	best := make([]int, maxValue+1)
	for index := 0; index < count; index++ {
		var cost, income int
		fmt.Fscan(input, &cost, &income)
		if income > best[cost] {
			best[cost] = income
		}
	}

	options := make([]option, 0)
	peak := 0
	for cost := 1; cost <= maxValue; cost++ {
		if best[cost] > peak {
			peak = best[cost]
			options = append(options, option{cost, peak})
		}
	}
	cap, topIncome := options[len(options)-1].cost, options[len(options)-1].income
	length := cap + 1
	stateCount := cap + 2*topIncome + 1
	current := emptyStates(stateCount)
	current[0] = 0
	workEvents := make([][]line, 0)
	rich := make([]richState, 0)
	day := 0
	for hasStates(current) {
		following := emptyStates(stateCount)
		events := make([]line, 0)
		greatest := int64(-1)
		for income := stateCount - 1; income >= 0; income-- {
			money := current[income]
			if money <= greatest {
				continue
			}
			greatest = money
			if income >= cap && money >= int64(cap) {
				rich = append(rich, richState{day, income, money})
				continue
			}
			slope := int64(income + 1)
			events = append(events, line{slope, money - slope*int64(day)})
			// Once every price is affordable, move the next purchase before any work.
			if money < int64(cap) {
				update(&following[income], money+int64(income)+1)
			}
			for _, choice := range options {
				if int64(choice.cost) > money {
					break
				}
				target := income + choice.income
				update(&following[target], money-int64(choice.cost)+int64(income))
			}
		}
		workEvents = append(workEvents, events)
		current = following
		day++
	}

	limit := len(workEvents) - 1 + length
	suffix := make([]int64, limit+1)
	for remaining := 0; remaining < limit; remaining++ {
		gain := int64(1)
		for _, choice := range options {
			update(&gain, int64(choice.income)*int64(remaining)-int64(choice.cost))
		}
		suffix[remaining+1] = suffix[remaining] + gain
	}
	correction := suffix[length] - int64(topIncome)*int64(length)*int64(length-1)/2
	correction += int64(cap) * int64(length)

	answers := make([]int64, limit+1)
	workBest := make([]int64, stateCount)
	workSeen := make([]bool, stateCount)
	for horizon := 0; horizon <= limit; horizon++ {
		if horizon < len(workEvents) {
			for _, event := range workEvents[horizon] {
				slope := int(event.slope)
				if !workSeen[slope] || event.intercept > workBest[slope] {
					workSeen[slope] = true
					workBest[slope] = event.intercept
				}
			}
		}
		for slope, intercept := range workBest {
			if workSeen[slope] {
				update(&answers[horizon], int64(slope)*int64(horizon)+intercept)
			}
		}
	}

	lines := make([]line, 0, len(rich))
	for _, state := range rich {
		for remaining := 0; remaining <= limit-state.day; remaining++ {
			horizon := state.day + remaining
			candidate := state.money + int64(state.income)*int64(remaining) + suffix[remaining]
			update(&answers[horizon], candidate)
		}
		start := int64(state.day)
		slope := int64(state.income) - int64(topIncome)*start
		intercept := state.money - int64(state.income)*start
		intercept += int64(topIncome)*start*(start+1)/2 + int64(cap)*start + correction
		lines = append(lines, line{slope, intercept})
	}
	richHull := makeHull(lines)
	lines = make([]line, 0, stateCount)
	for slope, intercept := range workBest {
		if workSeen[slope] {
			lines = append(lines, line{int64(slope), intercept})
		}
	}
	workHull := makeHull(lines)

	fmt.Fscan(input, &count)
	for index := 0; index < count; index++ {
		var horizon int64
		fmt.Fscan(input, &horizon)
		var answer int64
		if horizon <= int64(limit) {
			answer = answers[int(horizon)]
		} else {
			common := int64(topIncome)*horizon*(horizon-1)/2 - int64(cap)*horizon
			answer = maximum(workHull, horizon)
			update(&answer, common+maximum(richHull, horizon))
		}
		fmt.Fprintln(output, answer)
	}
}
