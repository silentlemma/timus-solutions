package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func sum(values []int) int {
	total := 0
	for _, v := range values {
		total += v
	}
	return total
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var n, m int
	if _, err := fmt.Fscan(reader, &n, &m); err != nil {
		return
	}
	girls := make([]int, n)
	for i := range girls {
		fmt.Fscan(reader, &girls[i])
	}
	boys := make([]int, m)
	for i := range boys {
		fmt.Fscan(reader, &boys[i])
	}
	// with k pairs the k most sensitive girls stay dry, and the k most
	// sensitive boys walk with them
	sort.Ints(girls)
	sort.Ints(boys)
	best := -1
	for k := 0; k <= n && k <= m; k++ {
		total := sum(girls[:n-k]) + sum(boys[:m-k])*k
		if best < 0 || total < best {
			best = total
		}
	}
	fmt.Println(best)
}
