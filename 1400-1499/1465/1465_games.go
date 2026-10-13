package main

import "fmt"

const (
	limit  = 200 // the values repeat with period from 52 on, well below this
	period = 34
	take   = 3 // a move takes up to three files out of play
)

func main() {
	var n int
	fmt.Scan(&n)
	// Dawson's chess: a row of n files plays like the octal game 0.137, where
	// a move takes one file (only if it is all), two (leaving one row) or three
	// (leaving up to two rows); White, moving first, wins when the value is not 0
	g := make([]int, limit+1)
	for size := 1; size <= limit; size++ {
		seen := map[int]bool{}
		if size == 1 {
			seen[0] = true
		}
		if size >= 2 {
			seen[g[size-2]] = true
		}
		for left := 0; left <= size-take; left++ {
			seen[g[left]^g[size-take-left]] = true
		}
		for seen[g[size]] {
			g[size]++
		}
	}
	if n > limit {
		n = limit - period + (n-limit)%period
	}
	if g[n] != 0 {
		fmt.Println("White")
	} else {
		fmt.Println("Black")
	}
}
