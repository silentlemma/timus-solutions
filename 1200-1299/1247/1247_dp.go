package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var s, n int
	fmt.Fscan(in, &s, &n)
	// the sum of A_i - 1 over every segment must stay at most N, so only the
	// largest such sum matters: Kadane's scan keeps the best one ending here
	best, here := 0, 0
	for i := 0; i < s; i++ {
		var a int
		fmt.Fscan(in, &a)
		here = max(here, 0) + a - 1
		best = max(best, here)
	}
	if best <= n {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
