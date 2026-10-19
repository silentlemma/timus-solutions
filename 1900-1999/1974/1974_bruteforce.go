package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

const octaveSize = 12
const pitchCount = 96
const naturalScale = "C D EF G A B"

type positions [pitchCount][]int

func parseNote(token string) int {
	pitch := int(token[0]-'1')*octaveSize + strings.IndexByte(naturalScale, token[1])
	if len(token) > 2 {
		if token[2] == '+' {
			pitch++
		} else {
			pitch--
		}
	}
	return pitch
}

func absoluteSimilarity(source *positions, sourceLength int, song []int) int {
	counts := make([]int, sourceLength+len(song)-1)
	for j, pitch := range song {
		offset := len(song) - 1 - j
		for _, i := range source[pitch] {
			counts[i+offset]++
		}
	}
	best := 0
	for _, count := range counts {
		if count > best {
			best = count
		}
	}
	return best
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var n int
	fmt.Fscan(in, &n)
	var source positions
	var token string
	for i := 0; i < n; i++ {
		fmt.Fscan(in, &token)
		pitch := parseNote(token)
		source[pitch] = append(source[pitch], i)
	}
	var melodies int
	fmt.Fscan(in, &melodies)
	for ; melodies > 0; melodies-- {
		var length int
		fmt.Fscan(in, &length)
		song := make([]int, length)
		for i := range song {
			fmt.Fscan(in, &token)
			song[i] = parseNote(token)
		}
		best := absoluteSimilarity(&source, n, song)
		fmt.Fprintf(out, "%.12f\n", float64(best)/float64(length))
	}
}
