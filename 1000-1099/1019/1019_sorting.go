package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

const end = 1000000000

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	a, b := make([]int, n), make([]int, n)
	colour := make([]string, n)
	xs := []int{0, end}
	for i := 0; i < n; i++ {
		fmt.Fscan(in, &a[i], &b[i], &colour[i])
		xs = append(xs, a[i], b[i])
	}
	sort.Ints(xs)
	unique := xs[:1]
	for _, x := range xs[1:] {
		if x != unique[len(unique)-1] {
			unique = append(unique, x)
		}
	}
	xs = unique

	// piece i is [xs[i], xs[i + 1]); repaint the pieces of every segment
	piece := make([]byte, len(xs)-1)
	for i := range piece {
		piece[i] = 'w'
	}
	for i := 0; i < n; i++ {
		lo, hi := sort.SearchInts(xs, a[i]), sort.SearchInts(xs, b[i])
		for p := lo; p < hi; p++ {
			piece[p] = colour[i][0]
		}
	}

	// the longest run of white pieces; a strict comparison keeps the leftmost
	bestX, bestY := 0, 0
	for i := 0; i < len(piece); {
		j := i
		for j < len(piece) && piece[j] == piece[i] {
			j++
		}
		if piece[i] == 'w' && xs[j]-xs[i] > bestY-bestX {
			bestX, bestY = xs[i], xs[j]
		}
		i = j
	}
	fmt.Println(bestX, bestY)
}
