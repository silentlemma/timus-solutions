package main

import "fmt"

const (
	digits = 9 // numbers below 10^9 have at most nine digits
	base   = 10
)

func main() {
	var target int
	fmt.Scan(&target)
	// ways[s]: digit strings of the current length with digit sum s
	ways := []int64{1}
	for l := 0; l < digits; l++ {
		next := make([]int64, len(ways)+base-1)
		for s, w := range ways {
			for d := 0; d < base; d++ {
				next[s+d] += w
			}
		}
		ways = next
	}
	answer := ways[target]
	if target == 1 {
		answer++ // 10^9 itself; zero is not counted since S >= 1
	}
	fmt.Println(answer)
}
