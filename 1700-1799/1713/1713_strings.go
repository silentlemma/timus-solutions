package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

type suffix struct {
	text string
	word int
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	var n int
	fmt.Fscan(reader, &n)
	words := make([]string, n)
	for i := range words {
		fmt.Fscan(reader, &words[i])
	}
	// every suffix of every command, sorted; a substring starting at some
	// position is in another command exactly when it is a prefix of another
	// command's suffix, and the nearest such suffixes in the order share most
	var suffixes []suffix
	for i, w := range words {
		for p := range w {
			suffixes = append(suffixes, suffix{w[p:], i})
		}
	}
	sort.Slice(suffixes, func(a, b int) bool { return suffixes[a].text < suffixes[b].text })
	total := len(suffixes)
	adjacent := make([]int, total)
	for k := 0; k+1 < total; k++ {
		a, b := suffixes[k].text, suffixes[k+1].text
		l := 0
		for l < len(a) && l < len(b) && a[l] == b[l] {
			l++
		}
		adjacent[k] = l
	}
	shared := make([]int, total) // the longest prefix shared with another command
	run := 0
	for k := 1; k < total; k++ {
		if suffixes[k].word != suffixes[k-1].word || adjacent[k-1] < run {
			run = adjacent[k-1]
		}
		shared[k] = run
	}
	run = 0
	for k := total - 2; k >= 0; k-- {
		if suffixes[k].word != suffixes[k+1].word || adjacent[k] < run {
			run = adjacent[k]
		}
		if run > shared[k] {
			shared[k] = run
		}
	}
	best := make([]string, n)
	for k, s := range suffixes {
		need := shared[k] + 1
		if need <= len(s.text) && (best[s.word] == "" || need < len(best[s.word])) {
			best[s.word] = s.text[:need]
		}
	}
	for _, b := range best {
		fmt.Fprintln(writer, b)
	}
}
