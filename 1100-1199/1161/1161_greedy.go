package main

import (
	"fmt"
	"math"
	"sort"
)

func main() {
	var n int
	fmt.Scan(&n)
	weights := make([]int, n)
	for k := range weights {
		fmt.Scan(&weights[k])
	}
	sort.Sort(sort.Reverse(sort.IntSlice(weights)))
	// each collision takes a square root of the product, so the heaviest
	// stripies should meet first and be rooted the most times
	total := float64(weights[0])
	for _, w := range weights[1:] {
		total = 2 * math.Sqrt(total*float64(w))
	}
	fmt.Printf("%.2f\n", total)
}
