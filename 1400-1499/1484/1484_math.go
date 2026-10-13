package main

import (
	"fmt"
	"strings"
)

const top = 10 // the highest vote

const halves = 20 // a rating counts in half tenths

func tenths(s string) int64 {
	whole, part := s, "0"
	if i := strings.IndexByte(s, '.'); i >= 0 {
		whole, part = s[:i], s[i+1:]+"0"
	}
	var v int64
	for _, c := range whole {
		v = v*10 + int64(c-'0')
	}
	return v*10 + int64(part[0]-'0')
}

func main() {
	var xs, ys string
	var n int64
	fmt.Scan(&xs, &ys, &n)
	x, y := tenths(xs), tenths(ys)
	// n votes from 1 to 10 show x when (2x - 1) n <= 20 sum < (2x + 1) n,
	// and the worst case is the largest such sum, and there may be none at all
	total := ((2*x+1)*n - 1) / halves
	if top*n < total {
		total = top * n
	}
	least := ((2*x-1)*n + halves - 1) / halves
	if n > least {
		least = n
	}
	// k votes of 1 show at most y when 20 (total + k) < (2y + 1)(n + k)
	excess, step := halves*total-(2*y+1)*n, 2*y+1-halves
	switch {
	case least > total || (excess >= 0 && step <= 0):
		fmt.Println("Impossible")
	case excess < 0:
		fmt.Println(0)
	default:
		fmt.Println(excess/step + 1)
	}
}
