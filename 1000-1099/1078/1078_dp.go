package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	left := make([]int, n)
	right := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(in, &left[i], &right[i])
		if left[i] > right[i] {
			left[i], right[i] = right[i], left[i]
		}
	}
	// a segment inside another is strictly shorter, so by length the inner
	// one always comes first
	order := make([]int, n)
	for i := range order {
		order[i] = i
	}
	sort.Slice(order, func(a, b int) bool {
		return right[order[a]]-left[order[a]] < right[order[b]]-left[order[b]]
	})
	best := make([]int, n)
	prev := make([]int, n)
	for p, i := range order {
		best[i], prev[i] = 1, -1
		for _, j := range order[:p] {
			if left[i] < left[j] && right[j] < right[i] && best[j]+1 > best[i] {
				best[i], prev[i] = best[j]+1, j
			}
		}
	}
	end := 0
	for i := range best {
		if best[i] > best[end] {
			end = i
		}
	}
	var chain []string
	for ; end >= 0; end = prev[end] {
		chain = append([]string{strconv.Itoa(end + 1)}, chain...)
	}
	fmt.Println(len(chain))
	fmt.Println(strings.Join(chain, " "))
}
