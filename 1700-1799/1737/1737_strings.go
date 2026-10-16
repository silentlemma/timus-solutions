package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

const limit = 100000

func main() {
	var n int
	fmt.Scan(&n)
	// a palindrome of two or more letters has one of two or three letters
	// in its middle, so any three letters in a row must differ, and a name
	// is one order of a, b, c repeated
	orders := []string{"abc", "acb", "bac", "bca", "cab", "cba"}
	seen := map[string]bool{}
	var names []string
	for _, order := range orders {
		name := make([]byte, n)
		for i := range name {
			name[i] = order[i%len(order)]
		}
		if !seen[string(name)] {
			seen[string(name)] = true
			names = append(names, string(name))
		}
	}
	if len(names)*n > limit {
		fmt.Println("TOO LONG")
		return
	}
	sort.Strings(names)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for _, name := range names {
		fmt.Fprintln(out, name)
	}
}
