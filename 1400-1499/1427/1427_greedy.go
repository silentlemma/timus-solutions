package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

const buffer = 1 << 20 // the text is up to 100 000 characters

func main() {
	in := bufio.NewReaderSize(os.Stdin, buffer)
	first, _ := in.ReadString('\n')
	var n, m int
	fmt.Sscan(first, &n, &m)
	text, _ := in.ReadString('\n') // read whole: the text may start with spaces
	text = strings.TrimRight(text, "\r\n")
	// run[i]: how many letters and spaces start at position i
	run := make([]int, len(text)+1)
	for i := len(text) - 1; i >= 0; i-- {
		c := text[i]
		if c == ' ' || (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') {
			run[i] = run[i+1] + 1
		}
	}
	// the farthest reach never moves back, so the longest message each time is best
	pos, count := 0, 0
	for pos < len(text) {
		step := run[pos]
		if step > m {
			step = m
		}
		if step < n {
			step = n
		}
		pos += step
		count++
	}
	fmt.Println(count)
}
