package main

import (
	"fmt"
	"strings"
)

const base = 10

func main() {
	var n int64
	fmt.Scan(&n)
	// a zero digit makes the product zero: 10 is the smallest such number
	if n == 0 {
		fmt.Println(base)
		return
	}
	if n == 1 {
		fmt.Println(1)
		return
	}
	// the largest digits first give the fewest digits; then sort them up
	var digits []string
	for d := int64(base - 1); d >= 2; d-- {
		for n%d == 0 {
			digits = append([]string{fmt.Sprint(d)}, digits...)
			n /= d
		}
	}
	if n != 1 {
		fmt.Println(-1)
		return
	}
	fmt.Println(strings.Join(digits, ""))
}
