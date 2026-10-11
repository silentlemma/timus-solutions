package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	floors = 1000
	// ten eggs already allow a binary search over all the floors
	eggs = 10
)

func main() {
	// best[k][n]: the fewest drops that settle n floors with k eggs; with d
	// drops and k eggs one can tell apart reach(d, k) floors, where
	// reach(d, k) = reach(d - 1, k - 1) + reach(d - 1, k) + 1
	var best [eggs + 1][floors + 1]int
	var reach, next [eggs + 1]int
	for d := 1; reach[1] < floors; d++ {
		for k := 1; k <= eggs; k++ {
			next[k] = reach[k-1] + reach[k] + 1
			if next[k] > floors {
				next[k] = floors
			}
			for n := reach[k] + 1; n <= next[k]; n++ {
				best[k][n] = d
			}
		}
		reach = next
	}
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for {
		var e, f int
		if _, err := fmt.Fscan(in, &e, &f); err != nil || (e == 0 && f == 0) {
			break
		}
		if e > eggs {
			e = eggs
		}
		fmt.Fprintln(out, best[e][f])
	}
}
