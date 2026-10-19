package main

import (
	"bufio"
	"fmt"
	"os"
)

func solve(values []int64, first, second int) (int64, int64) {
	total, score := int64(0), int64(0)
	for _, value := range values {
		total += value
	}
	if first == second {
		left := int64(0)
		for i := 0; i < first; i++ {
			left += values[i]
		}
		right := total - left - values[first]
		score = values[first] + left
		if right > left {
			score = values[first] + right
		}
	} else if first < second {
		boundary := (first + second) / 2
		for i := 0; i <= boundary; i++ {
			score += values[i]
		}
	} else {
		boundary := (first + second + 1) / 2
		for i := boundary; i < len(values); i++ {
			score += values[i]
		}
	}
	return score, total - score
}

func main() {
	input := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(input, &n)
	values := make([]int64, n)
	for i := range values {
		fmt.Fscan(input, &values[i])
	}
	var first, second int
	fmt.Fscan(input, &first, &second)
	a, b := solve(values, first-1, second-1)
	fmt.Println(a, b)
}
