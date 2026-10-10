package main

import (
	"bufio"
	"fmt"
	"math/bits"
	"os"
)

const size = 3

func main() {
	in := bufio.NewReader(os.Stdin)
	var k int
	fmt.Fscan(in, &k)
	teams := make([]map[string]bool, k)
	for i := range teams {
		teams[i] = map[string]bool{}
		for j := 0; j < size; j++ {
			var name string
			fmt.Fscan(in, &name)
			teams[i][name] = true
		}
	}
	// clash[i]: the teams sharing a member with team i, i itself included
	clash := make([]int, k)
	for i := 0; i < k; i++ {
		for j := 0; j < k; j++ {
			for name := range teams[i] {
				if teams[j][name] {
					clash[i] |= 1 << uint(j)
				}
			}
		}
	}
	// the lowest team of a set is either skipped or taken with its clashes
	// out; both smaller sets come earlier in this order
	best := make([]int, 1<<uint(k))
	for mask := 1; mask < len(best); mask++ {
		i := bits.TrailingZeros(uint(mask))
		best[mask] = best[mask&(mask-1)]
		if take := 1 + best[mask&^clash[i]]; take > best[mask] {
			best[mask] = take
		}
	}
	fmt.Println(best[len(best)-1])
}
