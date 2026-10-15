package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const (
	limit = 100000
	base  = 10
)

func main() {
	var n int
	fmt.Scan(&n)
	digits := make([]int, limit)
	for i := 1; i < limit; i++ {
		digits[i] = digits[i/base] + i%base
	}
	// take numbers from the top whenever their digits still fit; the small
	// ones at the end fill any remainder, so the sum always comes out
	var chosen []string
	for i := limit - 1; i >= 1 && n > 0; i-- {
		if digits[i] <= n {
			chosen = append(chosen, strconv.Itoa(i))
			n -= digits[i]
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	fmt.Fprintln(out, len(chosen))
	fmt.Fprintln(out, strings.Join(chosen, " "))
}
