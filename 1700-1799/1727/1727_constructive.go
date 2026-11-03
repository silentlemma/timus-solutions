package main

import (
	"bufio"
	"fmt"
	"os"
)

const limit = 100000
const base = 10
const small = base - 1
const remainder = small * (small + 1) / 2

func digitSum(value int) int {
	sum := 0
	for value > 0 {
		sum += value % base
		value /= base
	}
	return sum
}

func main() {
	var remaining int
	fmt.Scan(&remaining)
	chosen := []int{}
	value := limit - 1
	// The first ten thousand candidates have digit sum 270000 in total.
	// This phase therefore stops before any one-digit number is used.
	for remaining > remainder {
		chosen = append(chosen, value)
		remaining -= digitSum(value)
		value--
	}
	// Distinct digits 1..9 can make every sum from zero through 45.
	for digit := small; digit > 0; digit-- {
		if digit <= remaining {
			chosen = append(chosen, digit)
			remaining -= digit
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	fmt.Fprintln(out, len(chosen))
	for _, number := range chosen {
		fmt.Fprint(out, number, " ")
	}
	fmt.Fprintln(out)
}
