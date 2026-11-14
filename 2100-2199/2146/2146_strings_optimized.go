package main

import (
	"bufio"
	"io/ioutil"
	"os"
	"strconv"
)

const alphabet = 26
const decimal = 10

func repair(drum, pattern []byte, budget int) bool {
	period := len(pattern)
	perClass := len(drum) / period
	changes := 0
	for start := range pattern {
		var counts [alphabet]int
		best := byte(0)
		for i := start; i < len(drum); i += period {
			letter := drum[i] - 'a'
			counts[letter]++
			if counts[letter] > counts[best] {
				best = letter
			}
		}
		changes += perClass - counts[best]
		if changes > budget {
			return false
		}
		pattern[start] = 'a' + best
	}
	return true
}

func main() {
	input, err := ioutil.ReadAll(os.Stdin)
	if err != nil {
		return
	}
	cursor := 0
	number := func() int {
		for input[cursor] <= ' ' {
			cursor++
		}
		value := 0
		for input[cursor] >= '0' && input[cursor] <= '9' {
			value = value*decimal + int(input[cursor]-'0')
			cursor++
		}
		return value
	}
	size, budget := number(), number()
	for input[cursor] <= ' ' {
		cursor++
	}
	drum := input[cursor : cursor+size]
	pattern := make([]byte, size/2)
	best := drum
	for period := 1; period <= len(pattern); period++ {
		if size%period == 0 && repair(drum, pattern[:period], budget) {
			best = pattern[:period]
			break
		}
	}
	output := bufio.NewWriter(os.Stdout)
	output.WriteString(strconv.Itoa(len(best)) + "\n")
	for remaining := size; remaining > 0; remaining -= len(best) {
		output.Write(best)
	}
	output.WriteByte('\n')
	output.Flush()
}
