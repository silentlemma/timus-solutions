package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

func abs(x int64) int64 {
	if x < 0 {
		return -x
	}
	return x
}

func min(a, b int64) int64 {
	if a < b {
		return a
	}
	return b
}

func main() {
	sc := bufio.NewScanner(os.Stdin)
	sc.Split(bufio.ScanWords)
	sc.Scan()
	n, _ := strconv.Atoi(sc.Text())
	dryness := make([]int, n)
	order := make([]int, n)
	for i := range dryness {
		sc.Scan()
		dryness[i], _ = strconv.Atoi(sc.Text())
		order[i] = i
	}
	sort.Slice(order, func(a, b int) bool {
		if dryness[order[a]] != dryness[order[b]] {
			return dryness[order[a]] < dryness[order[b]]
		}
		return order[a] < order[b]
	})
	// a group of equal dryness is a segment of positions, watered by walking it once.
	// The walk ends at its left or right end, and those two states carry over
	var atLeft, atRight int64
	var left, right int64 // the previous group, starting from the leftmost flower
	for i := 0; i < n; {
		j := i
		for j < n && dryness[order[j]] == dryness[order[i]] {
			j++
		}
		l, r := int64(order[i]), int64(order[j-1])
		toLeft := min(atLeft+abs(left-r), atRight+abs(right-r)) + r - l
		toRight := min(atLeft+abs(left-l), atRight+abs(right-l)) + r - l
		atLeft, atRight, left, right = toLeft, toRight, l, r
		i = j
	}
	fmt.Println(min(atLeft, atRight) + int64(n))
}
