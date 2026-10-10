package main

import (
	"bufio"
	"fmt"
	"os"
)

const none = 1000000000

var black, prev, cur []int

// cost is black times white for horses j..i-1 in one stable
func cost(j, i int) int {
	b := black[i] - black[j]
	return b * (i - j - b)
}

// solve fills cur[lo..hi] knowing that their best last splits lie in
// [optLo, optHi]
func solve(lo, hi, optLo, optHi int) {
	if lo > hi {
		return
	}
	mid := (lo + hi) / 2
	best, arg := -1, optLo
	for j := optLo; j <= mid-1 && j <= optHi; j++ {
		if v := prev[j] + cost(j, mid); best < 0 || v < best {
			best, arg = v, j
		}
	}
	cur[mid] = best
	solve(lo, mid-1, optLo, arg)
	solve(mid+1, hi, arg, optHi)
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, k int
	fmt.Fscan(in, &n, &k)
	black = make([]int, n+1)
	for i := 0; i < n; i++ {
		var c int
		fmt.Fscan(in, &c)
		black[i+1] = black[i] + c
	}
	// prev[j]: the least unhappiness of the first j horses in the stables
	// so far; with no stables only j = 0 is possible
	prev = make([]int, n+1)
	for j := 1; j <= n; j++ {
		prev[j] = none
	}
	for stables := 1; stables <= k; stables++ {
		// the best last split never moves left as i grows (the black-white
		// cost satisfies the quadrangle inequality)
		cur = make([]int, n+1)
		solve(stables, n, stables-1, n-1)
		prev = cur
	}
	fmt.Println(prev[n])
}
