package main

import (
	"fmt"
	"strconv"
)

var (
	s    string
	best [][]int
	cut  [][]int // > 0: split before s[cut]; < 0: -cut is the period
)

// fold writes the shortest folding of s[i..j]
func fold(i, j int) string {
	switch c := cut[i][j]; {
	case c > 0:
		return fold(i, c-1) + fold(c, j)
	case c < 0:
		return strconv.Itoa((j-i+1)/-c) + "(" + fold(i, i-c-1) + ")"
	}
	return s[i : j+1]
}

func main() {
	fmt.Scan(&s)
	n := len(s)
	best, cut = make([][]int, n), make([][]int, n)
	for i := range best {
		best[i], cut[i] = make([]int, n), make([]int, n)
	}
	for size := 1; size <= n; size++ {
		for i := 0; i+size <= n; i++ {
			j := i + size - 1
			best[i][j] = size
			for k := i + 1; k <= j; k++ {
				if l := best[i][k-1] + best[k][j]; l < best[i][j] {
					best[i][j], cut[i][j] = l, k
				}
			}
			// a period p repeats when the segment equals itself shifted by p
			for p := 1; p < size; p++ {
				if size%p != 0 || s[i:j+1-p] != s[i+p:j+1] {
					continue
				}
				l := len(strconv.Itoa(size/p)) + 2 + best[i][i+p-1]
				if l < best[i][j] {
					best[i][j], cut[i][j] = l, -p
				}
			}
		}
	}
	fmt.Println(fold(0, n-1))
}
