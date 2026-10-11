package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	stones := make([]int, n)
	order := make([]int, n)
	for i := range stones {
		fmt.Fscan(in, &stones[i])
		order[i] = i
	}
	sort.Slice(order, func(i, j int) bool { return stones[order[i]] < stones[order[j]] })
	// a swap moves a stone K + 1 places, so K + 1 must divide every stone's
	// distance to its place, in one order or the other; all weights differ
	best := 0
	for _, down := range []bool{false, true} {
		g := 0
		for place, at := range order {
			if down {
				place = n - 1 - place
			}
			d := place - at
			if d < 0 {
				d = -d
			}
			g = gcd(g, d)
		}
		k := n - 1
		if g > 0 {
			k = g - 1
		}
		if k > best {
			best = k
		}
	}
	fmt.Println(best)
}
