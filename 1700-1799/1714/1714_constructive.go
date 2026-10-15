package main

import (
	"fmt"
	"strings"
)

const (
	head  = "aabab"
	block = "bbaaba" // each block forces two more palindromes
)

// the end after the blocks for each remainder of n mod 6
var tails = map[int]string{5: "", 0: "b", 1: "bb", 2: "bbaaababb", 3: "bbaa", 4: "bbaab"}

// short lengths where the pattern is not yet the best, found by search
var special = map[int]string{2: "ab", 8: "aababbaa", 11: "aababbaabab"}

func main() {
	var n int
	fmt.Scan(&n)
	if word, ok := special[n]; ok {
		fmt.Println(word)
	} else if n <= len(head) {
		fmt.Println(head[:n])
	} else {
		tail := tails[n%len(block)]
		fmt.Println(head + strings.Repeat(block, (n-len(head)-len(tail))/len(block)) + tail)
	}
}
