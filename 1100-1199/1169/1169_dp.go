package main

import (
	"bufio"
	"fmt"
	"os"
)

const smallestCycle = 3

func pairs(size int) int { return size * (size - 1) / 2 }

func cycles(n, target int) ([]int, bool) {
	if target < 0 || target > pairs(n) {
		return nil, false
	}
	minimum := make([]uint8, target+1)
	last := make([]uint8, target+1)
	for total := 1; total <= target; total++ {
		minimum[total] = uint8(n + 1)
	}
	// Minimize the number of vertices in cycles. Singletons fill any leftover places.
	for size := smallestCycle; size <= n; size++ {
		weight := pairs(size)
		for total := weight; total <= target; total++ {
			count := minimum[total-weight] + uint8(size)
			if count < minimum[total] {
				minimum[total], last[total] = count, uint8(size)
			}
		}
	}
	if int(minimum[target]) > n {
		return nil, false
	}
	var sizes []int
	for target > 0 {
		size := int(last[target])
		sizes = append(sizes, size)
		target -= pairs(size)
	}
	return sizes, true
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var n, k int
	fmt.Fscan(in, &n, &k)
	sizes, ok := cycles(n, pairs(n)-k)
	if !ok {
		fmt.Fprintln(out, -1)
		return
	}
	first, previous := 1, 0
	for _, size := range sizes {
		if previous != 0 {
			fmt.Fprintln(out, previous, first)
		}
		for i := first; i+1 < first+size; i++ {
			fmt.Fprintln(out, i, i+1)
		}
		fmt.Fprintln(out, first+size-1, first)
		previous, first = first, first+size
	}
	for vertex := first; vertex <= n; vertex++ {
		if previous != 0 {
			fmt.Fprintln(out, previous, vertex)
		}
		previous = vertex
	}
}
