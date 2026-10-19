package main

import (
	"bufio"
	"fmt"
	"os"
)

func mostCompared(values []int) int {
	championValue := values[0]
	champion, best := 0, 0
	currentCount, bestCount := 0, 0
	for index := 1; index < len(values); index++ {
		currentCount++
		if currentCount > bestCount {
			bestCount, best = currentCount, champion
		}
		if values[index] < championValue {
			championValue, champion = values[index], index
			currentCount = 1
		}
	}
	return best + 1
}

func main() {
	input := bufio.NewReader(os.Stdin)
	var count int
	fmt.Fscan(input, &count)
	values := make([]int, count)
	for i := range values {
		fmt.Fscan(input, &values[i])
	}
	fmt.Println(mostCompared(values))
}
