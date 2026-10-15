package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var g, w, b, p, n int
	fmt.Fscan(in, &g, &w, &b, &p, &n)
	last := g - b // the barbell starts at s = 0 .. g - b
	diff := make([]int, last+2)
	add := func(lo, hi, value int) {
		if lo < 0 {
			lo = 0
		}
		if hi > last {
			hi = last
		}
		if lo <= hi {
			diff[lo] += value
			diff[hi+1] -= value
		}
	}
	for i := 0; i < n; i++ {
		var x int
		fmt.Fscan(in, &x)
		// a plate [a, a + p] hurts the worm [x, x + w] when they overlap by a
		// positive length, that is for whole a from x - p + 1 to x + w - 1.
		// The left plate starts at s, the right one at s + b - p
		lo1, hi1 := x-p+1, x+w-1
		lo2, hi2 := x-b+1, x+w-1-b+p
		add(lo1, hi1, 1)
		add(lo2, hi2, 1)
		// a worm under both plates is hurt once
		lo, hi := lo1, hi1
		if lo2 > lo {
			lo = lo2
		}
		if hi2 < hi {
			hi = hi2
		}
		add(lo, hi, -1)
	}
	best, bestHurt, hurt := 0, 0, 0
	for s := 0; s <= last; s++ {
		hurt += diff[s]
		if s == 0 || hurt < bestHurt {
			best, bestHurt = s, hurt
		}
	}
	fmt.Println(best)
}
