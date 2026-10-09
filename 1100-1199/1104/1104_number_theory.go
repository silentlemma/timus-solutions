package main

import (
	"bufio"
	"fmt"
	"os"
)

const maxBase = 36

func main() {
	var s string
	fmt.Fscan(bufio.NewReader(os.Stdin), &s)
	total, top := 0, 1
	for i := 0; i < len(s); i++ {
		d := int(s[i] - '0')
		if s[i] >= 'A' {
			d = int(s[i]-'A') + 10
		}
		total += d
		if d > top {
			top = d
		}
	}
	// base k is 1 modulo k - 1, so the number is congruent to its digit sum
	for k := top + 1; k <= maxBase; k++ {
		if total%(k-1) == 0 {
			fmt.Println(k)
			return
		}
	}
	fmt.Println("No solution.")
}
