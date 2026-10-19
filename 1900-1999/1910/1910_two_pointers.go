package main

import (
	"bufio"
	"fmt"
	"os"
)

const windowSize = 3

func maximumWindow(values []int) (int, int) {
	current := 0
	for _, value := range values[:windowSize] {
		current += value
	}
	best, position := current, windowSize/2+1
	for start := 1; start+windowSize <= len(values); start++ {
		current += values[start+windowSize-1] - values[start-1]
		if current > best {
			best = current
			position = start + windowSize/2 + 1
		}
	}
	return best, position
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var count int
	fmt.Fscan(in, &count)
	values := make([]int, count)
	for index := range values {
		fmt.Fscan(in, &values[index])
	}
	best, position := maximumWindow(values)
	fmt.Fprintln(out, best, position)
}
