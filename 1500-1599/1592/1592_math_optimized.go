package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	hours  = 12
	minute = 60
	hour   = minute * minute
	dial   = hours * hour
)

func number(input *bufio.Reader) int {
	c, err := input.ReadByte()
	for err == nil && (c <= ' ' || c == ':') {
		c, err = input.ReadByte()
	}
	value := 0
	for err == nil && c >= '0' && c <= '9' {
		value = value*10 + int(c-'0')
		c, err = input.ReadByte()
	}
	return value
}

func main() {
	input := bufio.NewReader(os.Stdin)
	count := number(input)
	var frequency [dial]uint16
	for i := 0; i < count; i++ {
		h, m, s := number(input), number(input), number(input)
		frequency[h%hours*hour+m*minute+s]++
	}
	later := count
	bestTime, bestCost := 0, int64(count)*dial
	for target, clocks := range frequency {
		if clocks == 0 {
			continue
		}
		later -= int(clocks)
		// The sum of the initial readings is the same for every target.
		cost := int64(count)*int64(target) + dial*int64(later)
		if cost < bestCost {
			bestTime, bestCost = target, cost
		}
	}
	h, rest := bestTime/hour, bestTime%hour
	if h == 0 {
		h = hours
	}
	fmt.Printf("%d:%02d:%02d\n", h, rest/minute, rest%minute)
}
