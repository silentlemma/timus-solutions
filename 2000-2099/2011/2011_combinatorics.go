package main

import (
	"bufio"
	"fmt"
	"os"
)

const alphabet = 3
const target = 6

func solve(values []int) bool {
	counts := [alphabet]int{}
	ways := 1
	for index, value := range values {
		counts[value-1]++
		ways = ways * (index + 1) / counts[value-1]
		if ways >= target {
			return true
		}
	}
	return false
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	values := make([]int, n)
	for i := range values {
		fmt.Fscan(in, &values[i])
	}
	if solve(values) {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
