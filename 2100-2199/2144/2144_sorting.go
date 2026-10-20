package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(reader, &n)
	firsts := make([]int, n)
	lasts := make([]int, n)
	ok := true
	for i := 0; i < n; i++ {
		var k int
		fmt.Fscan(reader, &k)
		prev := 0
		for j := 0; j < k; j++ {
			var value int
			fmt.Fscan(reader, &value)
			if j == 0 {
				firsts[i] = value
			}
			if value < prev {
				ok = false
			}
			prev = value
		}
		lasts[i] = prev
	}
	// Sorting by the first size, and then by the last, gives a valid order if any exists.
	order := make([]int, n)
	for i := range order {
		order[i] = i
	}
	sort.Slice(order, func(x, y int) bool {
		a, b := order[x], order[y]
		if firsts[a] != firsts[b] {
			return firsts[a] < firsts[b]
		}
		return lasts[a] < lasts[b]
	})
	for i := 1; i < n; i++ {
		if lasts[order[i-1]] > firsts[order[i]] {
			ok = false
		}
	}
	if ok {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}
}
