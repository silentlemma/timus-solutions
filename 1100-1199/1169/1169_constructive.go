package main

import (
	"bufio"
	"fmt"
	"os"
)

const smallestCycle = 3

func pairs(s int) int {
	return s * (s - 1) / 2
}

func main() {
	var n, k int
	fmt.Scan(&n, &k)
	// a pair is not critical exactly when both computers lie in the same
	// 2-edge-connected part; such a part has one computer or at least three,
	// so the sizes must split n with pairs(size) adding up to pairs(n) - k
	target := pairs(n) - k
	sizes := []int{1}
	for s := smallestCycle; s <= n; s++ {
		sizes = append(sizes, s)
	}
	// reach[m][t] tells whether m computers can be split with t inner pairs
	reach := make([][]bool, n+1)
	for m := range reach {
		reach[m] = make([]bool, pairs(n)+1)
	}
	reach[0][0] = true
	for m := 1; m <= n; m++ {
		for _, s := range sizes {
			if s <= m {
				for t := pairs(s); t <= pairs(n); t++ {
					reach[m][t] = reach[m][t] || reach[m-s][t-pairs(s)]
				}
			}
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	if target < 0 || !reach[n][target] {
		fmt.Fprintln(out, -1)
		return
	}
	var parts []int
	for m, t := n, target; m > 0; {
		for _, s := range sizes {
			if s <= m && pairs(s) <= t && reach[m-s][t-pairs(s)] {
				parts = append(parts, s)
				m -= s
				t -= pairs(s)
				break
			}
		}
	}
	// each part is a cycle (or a single computer), and bridges join the first
	// computers of consecutive parts
	first, prev := 1, 0
	for _, s := range parts {
		if s > 1 {
			for j := 0; j < s; j++ {
				fmt.Fprintln(out, first+j, first+(j+1)%s)
			}
		}
		if prev > 0 {
			fmt.Fprintln(out, prev, first)
		}
		prev = first
		first += s
	}
}
