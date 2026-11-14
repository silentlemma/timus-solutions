package main

import (
	"bytes"
	"io/ioutil"
	"os"
	"strconv"
)

const alphabet = 26

func solve(pattern []byte, limit int) bool {
	var fixed [alphabet]bool
	var holes [2]int
	for i, letter := range pattern {
		if letter == '?' {
			holes[i%2]++
		} else {
			fixed[letter-'a'] = true
		}
	}
	var missing [alphabet]byte
	absent := 0
	for i, present := range fixed {
		if !present {
			missing[absent] = byte(i)
			absent++
		}
	}
	needed := limit - (alphabet - absent)
	if needed < 0 {
		needed = 0
	}
	if needed > holes[0]+holes[1] {
		return false
	}
	var low, high [alphabet + 1]int
	for i := 0; i < absent; i++ {
		low[i+1] = low[i] + int(missing[i])
		high[i+1] = high[i] + alphabet - 1 - int(missing[absent-1-i])
	}
	lower, upper := needed-holes[1], needed
	if lower < 0 {
		lower = 0
	}
	if upper > holes[0] {
		upper = holes[0]
	}
	positive, bestCost := 0, alphabet*alphabet
	for take := lower; take <= upper; take++ {
		cost := high[take] + low[needed-take]
		if cost < bestCost {
			positive, bestCost = take, cost
		}
	}
	remaining := [2]int{positive, needed - positive}
	left, right := 0, absent
	for i, letter := range pattern {
		if letter != '?' {
			continue
		}
		parity := i % 2
		if remaining[parity] == 0 {
			if parity == 0 {
				pattern[i] = 'z'
			} else {
				pattern[i] = 'a'
			}
			continue
		}
		remaining[parity]--
		if parity == 0 {
			right--
			pattern[i] = 'a' + missing[right]
		} else {
			pattern[i] = 'a' + missing[left]
			left++
		}
	}
	return true
}

func main() {
	input, err := ioutil.ReadAll(os.Stdin)
	if err != nil {
		return
	}
	fields := bytes.Fields(input)
	if len(fields) != 2 {
		return
	}
	pattern := fields[0]
	limit, err := strconv.Atoi(string(fields[1]))
	if err != nil {
		return
	}
	if solve(pattern, limit) {
		os.Stdout.Write(pattern)
		os.Stdout.WriteString("\n")
	} else {
		os.Stdout.WriteString("-1\n")
	}
}
