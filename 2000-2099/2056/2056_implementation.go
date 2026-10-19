package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	lowMark          = 3
	topMark          = 5
	doubledThreshold = 9
)

func classify(count, total, lowest int) string {
	if lowest == lowMark {
		return "None"
	}
	if lowest == topMark {
		return "Named"
	}
	if 2*total >= doubledThreshold*count {
		return "High"
	}
	return "Common"
}
func main() {
	input := bufio.NewReader(os.Stdin)
	var count int
	fmt.Fscan(input, &count)
	total, lowest := 0, topMark
	for i := 0; i < count; i++ {
		var grade int
		fmt.Fscan(input, &grade)
		total += grade
		if grade < lowest {
			lowest = grade
		}
	}
	fmt.Println(classify(count, total, lowest))
}
