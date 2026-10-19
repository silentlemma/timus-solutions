package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

type interval struct {
	left, right int
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var count int
	fmt.Fscan(in, &count)
	constants := make([]int, count)
	for i := range constants {
		fmt.Fscan(in, &constants[i])
	}
	intervals := []interval{{0, 1}}
	for i := count - 1; i >= 0; i-- {
		candidates := make([]interval, 0, 2*len(intervals))
		for _, item := range intervals {
			if item.right < 0 {
				continue
			}
			left := item.left
			if left < 0 {
				left = 0
			}
			candidates = append(candidates, interval{constants[i] - item.right, constants[i] - left})
			candidates = append(candidates, interval{constants[i] + left, constants[i] + item.right})
		}
		sort.Slice(candidates, func(a, b int) bool {
			if candidates[a].left != candidates[b].left {
				return candidates[a].left < candidates[b].left
			}
			return candidates[a].right < candidates[b].right
		})
		merged := make([]interval, 0, len(candidates))
		for _, item := range candidates {
			last := len(merged) - 1
			if last >= 0 && item.left <= merged[last].right {
				if item.right > merged[last].right {
					merged[last].right = item.right
				}
			} else {
				merged = append(merged, item)
			}
		}
		intervals = merged
	}
	out := bufio.NewWriter(os.Stdout)
	fmt.Fprintln(out, len(intervals))
	for _, item := range intervals {
		fmt.Fprintln(out, item.left, item.right)
	}
	out.Flush()
}
