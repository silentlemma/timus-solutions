package main

import (
	"bufio"
	"fmt"
	"os"
)

type modes struct {
	frequency, previous, following, head []int
	maximum                              int
}

func newModes(alphabet, capacity int) *modes {
	return &modes{frequency: make([]int, alphabet+1), previous: make([]int, alphabet+1),
		following: make([]int, alphabet+1), head: make([]int, capacity+1)}
}

func (c *modes) change(value, delta int) {
	old := c.frequency[value]
	if old != 0 {
		left, right := c.previous[value], c.following[value]
		if left != 0 {
			c.following[left] = right
		} else {
			c.head[old] = right
		}
		if right != 0 {
			c.previous[right] = left
		}
	}
	count := old + delta
	c.frequency[value] = count
	if count != 0 {
		first := c.head[count]
		c.previous[value] = 0
		c.following[value] = first
		if first != 0 {
			c.previous[first] = value
		}
		c.head[count] = value
	} else {
		c.previous[value] = 0
		c.following[value] = 0
	}
	if count > c.maximum {
		c.maximum = count
	}
	for c.maximum > 0 && c.head[c.maximum] == 0 {
		c.maximum--
	}
}

func (c *modes) mode() int { return c.head[c.maximum] }

func restore(text, pattern []int) {
	n, m := len(text), len(pattern)
	gap := n - m
	alphabet := 0
	textHoles, patternHoles := false, false
	for _, v := range text {
		if v > alphabet {
			alphabet = v
		}
		textHoles = textHoles || v == 0
	}
	for _, v := range pattern {
		if v > alphabet {
			alphabet = v
		}
		patternHoles = patternHoles || v == 0
	}
	if textHoles {
		counter := newModes(alphabet, m)
		for index := range text {
			if index < m {
				counter.change(pattern[index], 1)
			}
			if index > gap {
				counter.change(pattern[index-gap-1], -1)
			}
			if text[index] == 0 {
				text[index] = counter.mode()
			}
		}
	} else if patternHoles {
		width := gap + 1
		counter := newModes(alphabet, width)
		for _, v := range text[:width] {
			counter.change(v, 1)
		}
		for index := range pattern {
			if pattern[index] == 0 {
				pattern[index] = counter.mode()
			}
			if index+1 < m {
				counter.change(text[index], -1)
				counter.change(text[index+width], 1)
			}
		}
	}
}

func printRow(out *bufio.Writer, values []int) {
	for i, value := range values {
		if i > 0 {
			fmt.Fprint(out, " ")
		}
		fmt.Fprint(out, value)
	}
	fmt.Fprintln(out)
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var n int
	fmt.Fscan(in, &n)
	text := make([]int, n)
	for i := range text {
		fmt.Fscan(in, &text[i])
	}
	var m int
	fmt.Fscan(in, &m)
	pattern := make([]int, m)
	for i := range pattern {
		fmt.Fscan(in, &pattern[i])
	}
	restore(text, pattern)
	printRow(out, text)
	printRow(out, pattern)
}
