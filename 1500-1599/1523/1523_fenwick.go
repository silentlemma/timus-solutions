package main

import (
	"bufio"
	"fmt"
	"os"
)

const mod = 1000000000

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, k int
	fmt.Fscan(in, &n, &k)
	// count values from the top, so that "larger" becomes a prefix
	flipped := make([]int, n)
	for i := range flipped {
		fmt.Fscan(in, &flipped[i])
		flipped[i] = n + 1 - flipped[i]
	}
	// ends[i]: decreasing runs of the current length that end at position i
	ends := make([]int64, n)
	for i := range ends {
		ends[i] = 1
	}
	for length := 2; length <= k; length++ {
		tree := make([]int64, n+1)
		next := make([]int64, n)
		for i, v := range flipped {
			// the runs one shorter that end earlier at a larger value
			s := int64(0)
			for j := v - 1; j > 0; j &= j - 1 {
				s += tree[j]
			}
			next[i] = s % mod
			for j := v; j <= n; j += j & -j {
				tree[j] = (tree[j] + ends[i]) % mod
			}
		}
		ends = next
	}
	total := int64(0)
	for _, e := range ends {
		total = (total + e) % mod
	}
	fmt.Println(total)
}
