package main

import (
	"bufio"
	"fmt"
	"os"
)

func minInt(a, b int) int {
	if a < b {
		return a
	}
	return b
}
func maxInt(a, b int) int {
	if a > b {
		return a
	}
	return b
}
func build(limit, maximumSpies int) [][]float64 {
	choose := make([][]float64, limit+1)
	for size := 0; size <= limit; size++ {
		choose[size] = make([]float64, size+1)
		choose[size][0] = 1
		choose[size][size] = 1
		for j := 1; j < size; j++ {
			choose[size][j] = choose[size-1][j-1] + choose[size-1][j]
		}
	}
	table := make([][]float64, limit+1)
	for i := range table {
		table[i] = make([]float64, maximumSpies+1)
	}
	for size := 1; size <= limit; size++ {
		table[size][0] = float64(size)
		for spies := 1; spies <= minInt(maximumSpies, size-1); spies++ {
			loyal := size - spies
			best := 0.0
			for retained := 1; retained < size; retained++ {
				lower, upper := maxInt(0, retained-loyal), minInt(spies, (retained-1)/2)
				weighted := 0.0
				for remaining := lower; remaining <= upper; remaining++ {
					weighted += choose[spies][remaining] * choose[loyal][retained-remaining] *
						table[retained-remaining][remaining]
				}
				expected := weighted / choose[size][retained]
				if expected > best {
					best = expected
				}
			}
			table[size][spies] = best
		}
	}
	return table
}
func main() {
	input := bufio.NewReader(os.Stdin)
	var total, spies int
	fmt.Fscan(input, &total, &spies)
	answer := 0.0
	if total > 2*spies {
		answer = build(total-spies, spies)[total-spies][spies]
	}
	fmt.Printf("%.12f\n", answer)
}
