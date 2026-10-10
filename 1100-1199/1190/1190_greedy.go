package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	whole = 10000
	none  = -1
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	given := make([]int, n)
	for i := range given {
		var name string
		var shown int
		fmt.Fscan(in, &name, &shown)
		given[i] = none
		if shown == 1 {
			fmt.Fscan(in, &given[i])
		}
	}
	// shares never grow down the list, so an unknown share is at least the
	// next given one (or 1) and at most the last given one before it (or
	// 100%); every total between the two extremes can be reached
	low, high, floor, ceiling := 0, 0, 1, whole
	for i := n - 1; i >= 0; i-- {
		if given[i] != none {
			floor = given[i]
		}
		low += floor
	}
	for i := 0; i < n; i++ {
		if given[i] != none {
			ceiling = given[i]
		}
		high += ceiling
	}
	if low <= whole && whole <= high {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}
}
