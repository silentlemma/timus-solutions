package main

import (
	"bufio"
	"fmt"
	"os"
)

func insertEar(successor []int, first, second, outerFirst, outerSecond int) {
	if successor[first] != second {
		first, second = second, first
		outerFirst, outerSecond = outerSecond, outerFirst
	}
	successor[first] = outerFirst
	successor[outerFirst] = outerSecond
	successor[outerSecond] = second
}

func constructCycle(size, length int) []int {
	if length%2 != 0 || length > size*size-size%2 {
		return nil
	}
	successor := make([]int, size*size)
	initial := []int{0, 1, size + 1, size}
	for index, vertex := range initial {
		successor[vertex] = initial[(index+1)%len(initial)]
	}
	used := len(initial)
	width := size - size%2
	for column := 2; column < width && used < length; column++ {
		insertEar(successor, column-1, size+column-1, column, size+column)
		used += 2
	}
	for row := 2; row < size && used < length; row++ {
		for column := 0; column < width && used < length; column += 2 {
			upper := (row-1)*size + column
			lower := row*size + column
			insertEar(successor, upper, upper+1, lower, lower+1)
			used += 2
		}
	}
	if size%2 != 0 {
		for row := 0; row < size-1 && used < length; row += 2 {
			left := row*size + width - 1
			insertEar(successor, left, left+size, left+1, left+size+1)
			used += 2
		}
	}
	result := make([]int, length)
	current := 0
	for index := range result {
		result[index] = current
		current = successor[current]
	}
	return result
}

func main() {
	input := bufio.NewReader(os.Stdin)
	output := bufio.NewWriter(os.Stdout)
	defer output.Flush()
	var size, length int
	fmt.Fscan(input, &size, &length)
	cycle := constructCycle(size, length)
	if cycle == nil {
		fmt.Fprintln(output, "Unsuitable device")
	} else {
		fmt.Fprintln(output, "Overwhelming power of magic")
		for _, vertex := range cycle {
			fmt.Fprintln(output, vertex/size+1, vertex%size+1)
		}
	}
}
