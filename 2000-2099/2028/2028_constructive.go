package main

import "fmt"

func main() {
	const height = 6
	const width = 11
	grid := [height]string{
		">?v........",
		".>>.......v",
		"..@A+AB+B-<",
		"..B........",
		"..-........",
		".^@A!#.....",
	}
	fmt.Println(height, width)
	for _, row := range grid {
		fmt.Println(row)
	}
}
