package main

import (
	"fmt"
	"strings"
)

// the counts for N = 1 and N = 2; from N = 3 on, 1575 and N - 3 zeros
var small = []string{"", "14", "155"}

const short = 3
const base = "1575"

func main() {
	var n int
	fmt.Scan(&n)
	if n < short {
		fmt.Println(small[n])
	} else {
		fmt.Println(base + strings.Repeat("0", n-short))
	}
}
