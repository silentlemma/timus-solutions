package main

import (
	"bufio"
	"fmt"
	"os"
)

const chars = 128

func main() {
	in := bufio.NewReader(os.Stdin)
	var k int
	var last string
	fmt.Fscan(in, &k, &last)
	n := len(last)
	// a stable counting sort of the last column: row order[j] ends with
	// the j-th character of the sorted column, the first one of row j
	start := make([]int, chars+1)
	for i := 0; i < n; i++ {
		start[last[i]+1]++
	}
	for c := 0; c < chars; c++ {
		start[c+1] += start[c]
	}
	order := make([]int, n)
	for i := 0; i < n; i++ {
		order[start[last[i]]] = i
		start[last[i]]++
	}
	text := make([]byte, n)
	row := k - 1
	for i := range text {
		row = order[row]
		text[i] = last[row]
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	out.Write(text)
	out.WriteByte('\n')
}
