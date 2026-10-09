package main

import (
	"fmt"
	"strconv"
	"strings"
)

// power computes x^n mod m by repeated squaring
func power(x, n, m int) int {
	result := 1 % m
	for x %= m; n > 0; n >>= 1 {
		if n&1 == 1 {
			result = result * x % m
		}
		x = x * x % m
	}
	return result
}

func main() {
	var n, m, y int
	fmt.Scan(&n, &m, &y)
	// only M candidates; a Y of M or more is never a remainder
	var roots []string
	for x := 0; x < m; x++ {
		if power(x, n, m) == y {
			roots = append(roots, strconv.Itoa(x))
		}
	}
	if len(roots) == 0 {
		fmt.Println(-1)
	} else {
		fmt.Println(strings.Join(roots, " "))
	}
}
