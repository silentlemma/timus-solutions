package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
)

const side = 100

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, m, k int
	fmt.Fscan(in, &n, &m, &k)
	blocks := make([][2]int, k)
	for i := range blocks {
		fmt.Fscan(in, &blocks[i][0], &blocks[i][1])
	}
	sort.Slice(blocks, func(a, b int) bool {
		if blocks[a][0] != blocks[b][0] {
			return blocks[a][0] < blocks[b][0]
		}
		return blocks[a][1] < blocks[b][1]
	})
	// a route can use a chain of diagonal blocks increasing in both
	// coordinates; each one replaces two sides by one diagonal
	chain := make([]int, k)
	best := 0
	for i := range blocks {
		chain[i] = 1
		for j := 0; j < i; j++ {
			if blocks[j][0] < blocks[i][0] && blocks[j][1] < blocks[i][1] && chain[j]+1 > chain[i] {
				chain[i] = chain[j] + 1
			}
		}
		if chain[i] > best {
			best = chain[i]
		}
	}
	length := float64(side*(n+m-2*best)) + side*math.Sqrt2*float64(best)
	fmt.Println(int64(math.Round(length)))
}
