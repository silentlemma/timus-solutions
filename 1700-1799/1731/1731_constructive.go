package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	var n, m int
	fmt.Scan(&n, &m)
	// with first boxes 1..n and second boxes spaced n apart above them,
	// every sum a + b names its pair, so no two gifts can weigh the same
	first := make([]string, n)
	for i := range first {
		first[i] = strconv.Itoa(i + 1)
	}
	second := make([]string, m)
	for j := range second {
		second[j] = strconv.Itoa((j+1)*n + 1)
	}
	fmt.Println(strings.Join(first, " "))
	fmt.Println(strings.Join(second, " "))
}
