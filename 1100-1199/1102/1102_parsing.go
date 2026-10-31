package main

import (
	"bufio"
	"fmt"
	"os"
)

const alphabet = 26

var words = []string{"out", "output", "puton", "in", "input", "one"}

func empty() [alphabet]int {
	var row [alphabet]int
	for i := range row {
		row[i] = -1
	}
	return row
}

// a buffered reader keeps input memory bounded while integers are parsed once.
func nextInt(in *bufio.Reader) int {
	c, err := in.ReadByte()
	for err == nil && c <= ' ' {
		c, err = in.ReadByte()
	}
	sign, value := 1, 0
	if c == '-' {
		sign = -1
		c, err = in.ReadByte()
	}
	for err == nil && c >= '0' && c <= '9' {
		value = value*10 + int(c-'0')
		c, err = in.ReadByte()
	}
	return sign * value
}

func main() {
	trie, terminal := [][alphabet]int{empty()}, []bool{false}
	for _, word := range words {
		node := 0
		for _, letter := range word {
			c := letter - 'a'
			if trie[node][c] < 0 {
				trie[node][c] = len(trie)
				trie = append(trie, empty())
				terminal = append(terminal, false)
			}
			node = trie[node][c]
		}
		terminal[node] = true
	}
	// the six words have 24 letters in total, so all trie nodes fit in 32 bits.
	// bit zero permits a new word; other bits are unfinished matching prefixes.
	masks, ids := []uint32{1}, map[uint32]int{1: 0}
	var table [][alphabet]int
	for s := 0; s < len(masks); s++ {
		var row [alphabet]int
		for c := 0; c < alphabet; c++ {
			mask := uint32(0)
			for node := range trie {
				to := trie[node][c]
				if masks[s]&(uint32(1)<<uint(node)) != 0 && to >= 0 {
					mask |= uint32(1) << uint(to)
					if terminal[to] {
						mask |= 1
					}
				}
			}
			if _, ok := ids[mask]; !ok {
				ids[mask] = len(masks)
				masks = append(masks, mask)
			}
			row[c] = ids[mask]
		}
		table = append(table, row)
	}
	in, out := bufio.NewReader(os.Stdin), bufio.NewWriter(os.Stdout)
	defer out.Flush()
	n, state, lines, started := nextInt(in), 0, 0, false
	emit := func() {
		if masks[state]&1 != 0 {
			fmt.Fprintln(out, "YES")
		} else {
			fmt.Fprintln(out, "NO")
		}
	}
	// each byte makes one transition; even a rejected line is consumed fully.
	for {
		c, err := in.ReadByte()
		if err != nil {
			break
		}
		if c >= 'a' && c <= 'z' {
			state = table[state][c-'a']
			started = true
		} else if started {
			emit()
			state, started = 0, false
			lines++
		}
	}
	if started && lines < n {
		emit()
	}
}
