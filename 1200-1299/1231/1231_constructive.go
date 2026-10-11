package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	maxN = 200
	// state i (1 to maxN+1) stands on cell i of the minuses; state seek+d
	// still has to move d cells to the left before reaching the survivor
	seek = 300
	// states that cross the minuses to the right of the survivor, walk back
	// over it, cross those to its left and return to it
	right    = 600
	back     = 601
	left     = 602
	returned = 603
)

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var k int
	fmt.Fscan(in, &k)
	var rules []string
	rule := func(state int, read byte, next int, write, move byte) {
		rules = append(rules, fmt.Sprintf("%d %c %d %c %c", state, read, next, write, move))
	}
	// survivor = 0-based position of the minus that stays out of n, by the
	// Josephus recurrence
	survivor := 0
	for n := 1; n <= maxN; n++ {
		survivor = (survivor + k) % n
		rule(n, '-', n+1, '-', '>')
		// the head stands on the # after n minuses and moves onto cell n
		rule(n+1, '#', seek+n-1-survivor, '#', '<')
	}
	for d := 1; d < maxN; d++ {
		rule(seek+d, '-', seek+d-1, '-', '<')
	}
	rule(seek, '-', right, '-', '>')
	rule(right, '-', right, '+', '>')
	rule(right, '+', right, '+', '>')
	rule(right, '#', back, '#', '<')
	rule(back, '+', back, '+', '<')
	rule(back, '-', left, '-', '<')
	rule(left, '-', left, '+', '<')
	rule(left, '+', left, '+', '<')
	rule(left, '#', returned, '#', '>')
	rule(returned, '+', returned, '+', '>')
	fmt.Fprintln(out, len(rules))
	for _, r := range rules {
		fmt.Fprintln(out, r)
	}
}
