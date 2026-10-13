package main

import (
	"fmt"
	"strconv"
)

const (
	half    = 1000
	tickets = 1000000
	base    = 10
)

func digitSum(n int) int {
	s := 0
	for ; n > 0; n /= base {
		s += n % base
	}
	return s
}

func lucky(n int) bool { return digitSum(n/half) == digitSum(n%half) }

func main() {
	// a leading zero must not turn the number octal, so read it as text
	var text string
	fmt.Scan(&text)
	number, _ := strconv.Atoi(text)
	// the sums differ by one, so the ticket is neither 000000 nor 999999
	// and both neighbours are six-digit tickets
	yes := false
	for _, n := range []int{number - 1, number + 1} {
		if n >= 0 && n < tickets && lucky(n) {
			yes = true
		}
	}
	if yes {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
