package main

import (
	"bufio"
	"fmt"
	"os"
)

func reversed(s string) string {
	b := []byte(s)
	for i, j := 0, len(b)-1; i < j; i, j = i+1, j-1 {
		b[i], b[j] = b[j], b[i]
	}
	return string(b)
}

func main() {
	var word string
	fmt.Fscan(bufio.NewReader(os.Stdin), &word)
	// the added part is never empty, so look for the longest palindromic
	// suffix of the word without its first letter
	tail := word[1:]
	text := reversed(tail) + "#" + tail
	border := make([]int, len(text))
	for i := 1; i < len(text); i++ {
		k := border[i-1]
		for k > 0 && text[i] != text[k] {
			k = border[k-1]
		}
		if text[i] == text[k] {
			k++
		}
		border[i] = k
	}
	longest := 0
	if len(tail) > 0 {
		longest = border[len(text)-1]
	}
	fmt.Println(word + reversed(word[:len(word)-longest]))
}
