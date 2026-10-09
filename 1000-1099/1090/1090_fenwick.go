package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	sc := bufio.NewScanner(os.Stdin)
	sc.Split(bufio.ScanWords)
	next := func() int {
		sc.Scan()
		v, _ := strconv.Atoi(sc.Text())
		return v
	}
	n, k := next(), next()
	best, bestRow := int64(-1), 0
	tree := make([]int, n+1)
	for r := 1; r <= k; r++ {
		for i := range tree {
			tree[i] = 0
		}
		var jumps int64
		for i := 0; i < n; i++ {
			x := next()
			// each recruit jumps once for every earlier recruit with a larger
			// number: earlier minus those not larger, counted by the tree
			smaller := 0
			for j := x; j > 0; j &= j - 1 {
				smaller += tree[j]
			}
			jumps += int64(i - smaller)
			for j := x; j <= n; j += j & -j {
				tree[j]++
			}
		}
		if jumps > best {
			best, bestRow = jumps, r
		}
	}
	fmt.Println(bestRow)
}
