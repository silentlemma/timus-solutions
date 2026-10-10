package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

// stride: counts are kept only for every stride-th height, so that the table
// fits in the memory limit; the heights between are recomputed by recursion
const stride = 4

var offset [][]int // -1 where nothing is stored
var memo []int64

// most is the largest number of bricks of a tower with h levels whose lowest
// has m bricks
func most(h, m int) int { return m*h + h*(h-1)/2 }

// count is the number of towers of h levels starting with m bricks that use
// at most n bricks
func count(n, h, m int) int64 {
	if m == 0 || n < m {
		return 0
	}
	if h == 1 {
		return 1
	}
	if top := most(h, m); n > top {
		n = top
	}
	key := -1
	if h < len(offset) && m < len(offset[h]) {
		key = offset[h][m]
	}
	if key >= 0 && memo[key+n] >= 0 {
		return memo[key+n]
	}
	ways := count(n-m, h-1, m-1) + count(n-m, h-1, m+1)
	if key >= 0 {
		memo[key+n] = ways
	}
	return ways
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var total, height, base int
	fmt.Fscan(in, &total, &height, &base)
	// offset[h][m] starts the stored counts for h levels and m bricks below,
	// kept only for the widths that a tower can reach at that height
	offset = make([][]int, height+1)
	size := 0
	for h := range offset {
		offset[h] = make([]int, base+height+2)
		for m := range offset[h] {
			offset[h][m] = -1
		}
		if h == 0 || h%stride != 0 {
			continue
		}
		depth := height - h
		low := base - depth
		for low < 1 {
			low += 2
		}
		for m := low; m <= base+depth; m += 2 {
			offset[h][m] = size
			size += most(h, m) + 1
		}
	}
	memo = make([]int64, size)
	for k := range memo {
		memo[k] = -1
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	fmt.Fprintln(out, count(total, height, base))
	for {
		var k int64
		if _, err := fmt.Fscan(in, &k); err != nil || k < 0 {
			break
		}
		// lexicographic order: the narrower next level comes first
		n, m := total, base
		out.WriteString(strconv.Itoa(m))
		for h := height; h > 1; h-- {
			fewer := count(n-m, h-1, m-1)
			n -= m
			if k <= fewer {
				m--
			} else {
				k -= fewer
				m++
			}
			out.WriteString(" " + strconv.Itoa(m))
		}
		out.WriteString("\n")
	}
}
