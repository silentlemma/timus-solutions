package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func min2(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max2(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	sc := bufio.NewScanner(os.Stdin)
	sc.Split(bufio.ScanWords)
	next := func() int {
		sc.Scan()
		x, _ := strconv.Atoi(sc.Text())
		return x
	}
	n, m := next(), next()
	v, h := make([]int, n), make([]int, m)
	maxV, maxH := 0, 0
	for i := range v {
		v[i] = next()
		maxV = max2(maxV, v[i])
	}
	for i := range h {
		h[i] = next()
		maxH = max2(maxH, h[i])
	}
	// one turn: down the left street and along the bottom, or along the top and down the right
	best := max2(min2(v[0], h[m-1]), min2(h[0], v[n-1]))
	// two turns: the middle street is the best one of its kind
	best = max2(best, min2(min2(h[0], maxV), h[m-1]))
	best = max2(best, min2(min2(v[0], maxH), v[n-1]))
	fmt.Println(best)
}
