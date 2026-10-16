package main

import (
	"bufio"
	"fmt"
	"os"
)

const far = int64(1) << 40

var (
	n, s, size          int
	latest              []int
	leftPart, rightPart []int64
)

// cost of a lane comes from the latest obstacle covering it, as
// min(left[t] + x, right[t] - x), or from the start as |x - s| if none
func cost(x int) int64 {
	t := 0
	for node := x + size; node > 0; node >>= 1 {
		if latest[node] > t {
			t = latest[node]
		}
	}
	if t == 0 {
		if x < s {
			return int64(s - x)
		}
		return int64(x - s)
	}
	a, b := leftPart[t]+int64(x), rightPart[t]-int64(x)
	if a < b {
		return a
	}
	return b
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var k int
	if _, err := fmt.Fscan(reader, &n, &s, &k); err != nil {
		return
	}
	size = 1
	for size <= n {
		size *= 2
	}
	// latest[node]: the last obstacle whose lanes cover the node's whole range
	latest = make([]int, 2*size)
	leftPart = make([]int64, k+1)
	rightPart = make([]int64, k+1)
	for t := 1; t <= k; t++ {
		var lo, hi int
		fmt.Fscan(reader, &lo, &hi)
		// the cost stays one per lane apart, so going round the obstacle
		// only needs the lanes just beside it
		below, above := far, far
		if lo > 1 {
			below = cost(lo - 1)
		}
		if hi < n {
			above = cost(hi + 1)
		}
		leftPart[t] = below - int64(lo-1)
		rightPart[t] = above + int64(hi+1)
		for a, b := lo+size, hi+size+1; a < b; a, b = a>>1, b>>1 {
			if a&1 == 1 {
				latest[a] = t
				a++
			}
			if b&1 == 1 {
				b--
				latest[b] = t
			}
		}
	}
	best := far
	for x := 1; x <= n; x++ {
		if c := cost(x); c < best {
			best = c
		}
	}
	fmt.Println(best)
}
