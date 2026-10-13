package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func flip(side byte) byte {
	if side == 'L' {
		return 'R'
	}
	return 'L'
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	var n int
	fmt.Fscan(reader, &n)
	weights := make([]int, n)
	for i := range weights {
		fmt.Fscan(reader, &weights[i])
	}
	sort.Ints(weights)
	var record string
	fmt.Fscan(reader, &record)
	// the weights in use always form a block of the sorted list whose
	// neighbours stand on opposite pans, so the pan of the largest one wins,
	// and a change adds a new largest weight, any other step a new smallest
	changes := 0
	for i := 1; i < n; i++ {
		if record[i] != record[i-1] {
			changes++
		}
	}
	low := n - 1 - changes
	high := low
	lowSide, highSide := record[0], record[0]
	fmt.Fprintf(writer, "%d %c\n", weights[low], record[0])
	for i := 1; i < n; i++ {
		if record[i] != record[i-1] {
			high++
			highSide = flip(highSide)
			fmt.Fprintf(writer, "%d %c\n", weights[high], highSide)
		} else {
			low--
			lowSide = flip(lowSide)
			fmt.Fprintf(writer, "%d %c\n", weights[low], lowSide)
		}
	}
}
