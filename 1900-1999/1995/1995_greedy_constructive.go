package main

import (
	"bufio"
	"fmt"
	"os"
)

const percentScale = 100

func construct(size, kept, percentage int) []int {
	weights := make([]int, size)
	for i := range weights {
		weights[i] = 1
	}
	for i := size - kept; i < size; i++ {
		weights[i] = weights[(percentage*i-1)/percentScale] + 1
	}
	return weights
}
func main() {
	input := bufio.NewReader(os.Stdin)
	var size, kept, percentage int
	fmt.Fscan(input, &size, &kept, &percentage)
	weights := construct(size, kept, percentage)
	total := int64(0)
	for _, value := range weights {
		total += int64(value)
	}
	output := bufio.NewWriter(os.Stdout)
	defer output.Flush()
	fmt.Fprintln(output, total)
	for i, value := range weights {
		if i > 0 {
			fmt.Fprint(output, " ")
		}
		fmt.Fprint(output, value)
	}
	fmt.Fprintln(output)
}
