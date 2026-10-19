package main

import (
	"bufio"
	"fmt"
	"os"
)

func solve(pattern string, limit int) string {
	const alphabet = 26
	fixed := make([]bool, alphabet+1)
	positive, negative := []int{}, []int{}
	for index := range pattern {
		if pattern[index] != '?' {
			fixed[int(pattern[index]-'a')+1] = true
		} else if index%2 == 0 {
			positive = append(positive, index)
		} else {
			negative = append(negative, index)
		}
	}
	fixedCount := 0
	missing := []int{}
	for value := 1; value <= alphabet; value++ {
		if fixed[value] {
			fixedCount++
		} else {
			missing = append(missing, value)
		}
	}
	needed := limit - fixedCount
	if needed < 0 {
		needed = 0
	}
	if len(positive)+len(negative) < needed {
		return "-1"
	}
	count := len(missing)
	low, high := make([]int, count+1), make([]int, count+1)
	for index := range missing {
		low[index+1] = low[index] + missing[index] - 1
		high[index+1] = high[index] + alphabet - missing[count-1-index]
	}
	lower, upper := needed-len(negative), needed
	if lower < 0 {
		lower = 0
	}
	if upper > len(positive) {
		upper = len(positive)
	}
	bestCost, chosen := alphabet*alphabet, 0
	for take := lower; take <= upper; take++ {
		cost := high[take] + low[needed-take]
		if cost < bestCost {
			bestCost, chosen = cost, take
		}
	}
	answer := []byte(pattern)
	for _, index := range positive {
		answer[index] = 'z'
	}
	for _, index := range negative {
		answer[index] = 'a'
	}
	for index := 0; index < chosen; index++ {
		answer[positive[index]] = 'a' + byte(missing[count-1-index]-1)
	}
	for index := 0; index < needed-chosen; index++ {
		answer[negative[index]] = 'a' + byte(missing[index]-1)
	}
	return string(answer)
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var pattern string
	var limit int
	if _, err := fmt.Fscan(in, &pattern, &limit); err != nil {
		return
	}
	fmt.Println(solve(pattern, limit))
}
