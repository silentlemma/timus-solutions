package main

import (
	"bufio"
	"fmt"
	"os"
)

const alphabet = 26

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	var a, b string
	fmt.Fscan(in, &n, &a, &b)
	// suffix automaton of a: every state is a class of substrings with the
	// same end positions; length is the longest of them, link the suffix link
	empty := [alphabet]int32{}
	for i := range empty {
		empty[i] = -1
	}
	// at most 2 len(a) states: reserve them so that the tables are not copied
	most := 2*len(a) + 1
	next := append(make([][alphabet]int32, 0, most), empty)
	link := append(make([]int32, 0, most), -1)
	length := append(make([]int32, 0, most), 0)
	last := int32(0)
	for i := 0; i < len(a); i++ {
		c := a[i] - 'A'
		cur := int32(len(next))
		next = append(next, empty)
		link = append(link, 0)
		length = append(length, length[last]+1)
		p := last
		for p != -1 && next[p][c] == -1 {
			next[p][c] = cur
			p = link[p]
		}
		if p != -1 {
			q := next[p][c]
			if length[p]+1 == length[q] {
				link[cur] = q
			} else {
				clone := int32(len(next))
				next = append(next, next[q])
				link = append(link, link[q])
				length = append(length, length[p]+1)
				for ; p != -1 && next[p][c] == q; p = link[p] {
					next[p][c] = clone
				}
				link[q], link[cur] = clone, clone
			}
		}
		last = cur
	}
	// walk b through the automaton, keeping the longest suffix of the read
	// part of b that occurs in a
	state, run, best, end := int32(0), int32(0), int32(0), 0
	for i := 0; i < len(b); i++ {
		c := b[i] - 'A'
		for state != 0 && next[state][c] == -1 {
			state = link[state]
			run = length[state]
		}
		if next[state][c] != -1 {
			state = next[state][c]
			run++
		}
		if run > best {
			best, end = run, i+1
		}
	}
	fmt.Println(b[end-int(best) : end])
}
