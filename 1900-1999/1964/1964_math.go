package main

import (
	"bufio"
	"fmt"
	"os"
)

func minimumCommon(population int64, lowerBounds []int64) int64 {
	answer := population
	for _, lower := range lowerBounds {
		answer -= population - lower
	}
	if answer < 0 {
		return 0
	}
	return answer
}

func main() {
	input := bufio.NewReader(os.Stdin)
	var population int64
	var count int
	fmt.Fscan(input, &population, &count)
	lowerBounds := make([]int64, count)
	for i := range lowerBounds {
		fmt.Fscan(input, &lowerBounds[i])
	}
	fmt.Println(minimumCommon(population, lowerBounds))
}
