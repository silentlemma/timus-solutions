package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var k int
	fmt.Fscan(in, &k)
	sleepers := make([][2]int, k)
	for i := range sleepers {
		fmt.Fscan(in, &sleepers[i][0], &sleepers[i][1])
	}
	sort.Slice(sleepers, func(a, b int) bool { return sleepers[a][0] < sleepers[b][0] })
	// two sleepers cross when their ends come in opposite orders, so the
	// kept ones form an increasing run of right ends
	longest := make([]int, k)
	best := 0
	for i := range sleepers {
		longest[i] = 1
		for j := 0; j < i; j++ {
			if sleepers[j][1] < sleepers[i][1] && longest[j]+1 > longest[i] {
				longest[i] = longest[j] + 1
			}
		}
		if longest[i] > best {
			best = longest[i]
		}
	}
	fmt.Println(k - best)
}
