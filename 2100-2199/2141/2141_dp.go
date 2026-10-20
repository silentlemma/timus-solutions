package main

import (
	"bufio"
	"fmt"
	"os"
)

func max(a, b int64) int64 {
	if a > b {
		return a
	}
	return b
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var n int
	var a int64
	fmt.Fscan(reader, &n, &a)
	// plus and minus are the best sums of segments ending at the current dish
	// whose last dish counts with a plus or with a minus; before the second
	// dish no minus segment exists, and 0 there only means "start anew"
	plus, minus, best := a, int64(0), max(0, a)
	for i := 1; i < n; i++ {
		fmt.Fscan(reader, &a)
		nextPlus := a + max(0, minus)
		minus = plus - a
		plus = nextPlus
		best = max(best, max(plus, minus))
	}
	fmt.Println(best)
}
