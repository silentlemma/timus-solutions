package main

import (
	"bufio"
	"fmt"
	"os"
)

func fixedDirections(values []int, firstDirection, secondDirection int) [][]int {
	size := len(values)
	direction := [2]int{firstDirection, secondDirection}
	other := [2]int{0, 0}
	if secondDirection < 0 {
		other[0] = size + 1
	}
	if firstDirection < 0 {
		other[1] = size + 1
	}
	parent := [2][]byte{make([]byte, size), make([]byte, size)}
	previous := values[0]
	for index := 1; index < size; index++ {
		value := values[index]
		next := [2]int{-1, -1}
		for owner := 0; owner < 2; owner++ {
			if other[owner] >= 0 && direction[owner]*(value-previous) > 0 {
				next[owner] = other[owner]
				parent[owner][index] = byte(owner)
			}
			if other[1-owner] >= 0 && direction[owner]*(value-other[1-owner]) > 0 {
				if next[owner] < 0 || direction[1-owner]*(previous-next[owner]) < 0 {
					next[owner] = previous
					parent[owner][index] = byte(1 - owner)
				}
			}
		}
		if next[0] < 0 && next[1] < 0 {
			return nil
		}
		other = next
		previous = value
	}
	owner := 0
	if other[0] < 0 {
		owner = 1
	}
	assignment := make([]int, size)
	counts := [2]int{}
	for index := size - 1; index >= 0; index-- {
		assignment[index] = owner
		counts[owner]++
		owner = int(parent[owner][index])
	}
	if counts[0] == 0 {
		assignment[size-1] = 0
	}
	if counts[1] == 0 {
		assignment[size-1] = 1
	}
	groups := make([][]int, 2)
	for index, value := range values {
		groups[assignment[index]] = append(groups[assignment[index]], value)
	}
	return groups
}

func partition(values []int) [][]int {
	for _, direction := range [][2]int{{1, 1}, {-1, -1}, {1, -1}, {-1, 1}} {
		if groups := fixedDirections(values, direction[0], direction[1]); groups != nil {
			return groups
		}
	}
	return nil
}

func main() {
	input := bufio.NewReader(os.Stdin)
	output := bufio.NewWriter(os.Stdout)
	defer output.Flush()
	var size int
	fmt.Fscan(input, &size)
	values := make([]int, size)
	for i := range values {
		fmt.Fscan(input, &values[i])
	}
	groups := partition(values)
	if groups == nil {
		fmt.Fprintln(output, "Fail")
		return
	}
	fmt.Fprintln(output, len(groups[0]), len(groups[1]))
	for _, group := range groups {
		for _, value := range group {
			fmt.Fprint(output, value, " ")
		}
		fmt.Fprintln(output)
	}
}
