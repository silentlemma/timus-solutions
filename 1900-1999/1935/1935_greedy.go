package main

import (
	"bufio"
	"fmt"
	"os"
)

func minimumSheets(clearances []int) int {
	total, largest := 0, 0
	for _, clearance := range clearances {
		total += clearance
		if clearance > largest {
			largest = clearance
		}
	}
	return total + largest
}

func main() {
	input := bufio.NewReader(os.Stdin)
	var count int
	fmt.Fscan(input, &count)
	clearances := make([]int, count)
	for index := range clearances {
		fmt.Fscan(input, &clearances[index])
	}
	fmt.Println(minimumSheets(clearances))
}
