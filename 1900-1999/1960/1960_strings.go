package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	alphabetSize = 26
	emptyRoot    = 1
	rootCount    = 2
)

type node struct {
	length, link int
	next         [alphabetSize]int
}

func distinctCounts(text string) []int {
	nodes := make([]node, len(text)+rootCount)
	nodes[0].length = -1
	count, last := rootCount, emptyRoot
	answer := make([]int, len(text))
	for position := range text {
		letter := text[position]
		code := int(letter - 'a')
		parent := last
		for {
			left := position - nodes[parent].length - 1
			if left >= 0 && text[left] == letter {
				break
			}
			parent = nodes[parent].link
		}
		current := nodes[parent].next[code]
		if current == 0 {
			current = count
			count++
			nodes[current].length = nodes[parent].length + 2
			nodes[parent].next[code] = current
			if nodes[current].length == 1 {
				nodes[current].link = emptyRoot
			} else {
				candidate := nodes[parent].link
				for {
					left := position - nodes[candidate].length - 1
					if left >= 0 && text[left] == letter {
						break
					}
					candidate = nodes[candidate].link
				}
				nodes[current].link = nodes[candidate].next[code]
			}
		}
		last = current
		answer[position] = count - rootCount
	}
	return answer
}

func printCounts(out *bufio.Writer, values []int) {
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
	var text string
	fmt.Fscan(in, &text)
	printCounts(out, distinctCounts(text))
}
