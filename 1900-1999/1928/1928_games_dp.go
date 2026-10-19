package main

import (
	"bufio"
	"fmt"
	"os"
)

func optimalTotals(budget, gift, limit int) (int, int) {
	current, opponent := make([]int, budget+1), make([]int, budget+1)
	for remaining := 1; remaining <= budget; remaining++ {
		best, other := -1, 0
		if remaining < limit {
			best = gift
		}
		for request := 1; request <= remaining && request <= limit; request++ {
			rest := remaining - request
			ownTotal, otherTotal := request+opponent[rest], current[rest]
			if ownTotal > best || ownTotal == best && otherTotal < other {
				best, other = ownTotal, otherTotal
			}
		}
		current[remaining], opponent[remaining] = best, other
	}
	return current[budget], opponent[budget]
}

func main() {
	input := bufio.NewReader(os.Stdin)
	var budget, gift, limit int
	fmt.Fscan(input, &budget, &gift, &limit)
	first, second := optimalTotals(budget, gift, limit)
	fmt.Println(first, second)
}
