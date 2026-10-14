package main

import (
	"bufio"
	"fmt"
	"os"
)

const letters = 26

func main() {
	in := bufio.NewReader(os.Stdin)
	var s string
	if _, err := fmt.Fscan(in, &s); err != nil {
		return
	}
	most := 2*len(s) + 1
	// suffix automaton: every state is a class of substrings with the same
	// end positions, from link-length + 1 up to length characters long
	length := make([]int, most)
	link := make([]int, most)
	next := make([][letters]int32, most)
	for i := range next {
		link[i] = -1
		for c := range next[i] {
			next[i][c] = -1
		}
	}
	size, last := 1, 0
	for i := 0; i < len(s); i++ {
		c := s[i] - 'a'
		cur := size
		size++
		length[cur] = length[last] + 1
		p := last
		for p != -1 && next[p][c] == -1 {
			next[p][c] = int32(cur)
			p = link[p]
		}
		if p == -1 {
			link[cur] = 0
		} else {
			q := int(next[p][c])
			if length[p]+1 == length[q] {
				link[cur] = q
			} else {
				// split q: the clone keeps the shorter strings
				clone := size
				size++
				length[clone] = length[p] + 1
				link[clone] = link[q]
				next[clone] = next[q]
				for p != -1 && int(next[p][c]) == q {
					next[p][c] = int32(clone)
					p = link[p]
				}
				link[q] = clone
				link[cur] = clone
			}
		}
		last = cur
	}
	total := 0
	for v := 1; v < size; v++ {
		total += length[v] - length[link[v]]
	}
	fmt.Println(total)
}
