package main

import (
	"fmt"
	"sort"
)

func main() {
	var piles []int64
	for {
		var v int64
		if _, err := fmt.Scan(&v); err != nil {
			break
		}
		piles = append(piles, v)
	}
	asked := 0
	for {
		asked++
		// the closest two piles differ least among neighbours in sorted order
		sort.Slice(piles, func(i, j int) bool { return piles[i] < piles[j] })
		gap := piles[1] - piles[0]
		for i := 2; i < len(piles); i++ {
			if d := piles[i] - piles[i-1]; d < gap {
				gap = d
			}
		}
		if gap == 0 {
			break
		}
		piles = append(piles, gap)
	}
	fmt.Println(asked)
}
