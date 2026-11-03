package main

import (
	"fmt"
	"sort"
)

func main() {
	var text string
	fmt.Scan(&text)
	suffixes := make([]string, len(text))
	for i := range text {
		suffixes[i] = text[i:]
	}
	sort.Strings(suffixes)
	answer := int64(len(text)) * int64(len(text)+1) / 2
	// Only the previous suffix is needed in lexicographic order: its shared
	// prefixes include every prefix already seen before the current suffix.
	for i := 1; i < len(suffixes); i++ {
		previous, current := suffixes[i-1], suffixes[i]
		common := 0
		for common < len(previous) && common < len(current) && previous[common] == current[common] {
			common++
		}
		answer -= int64(common)
	}
	fmt.Println(answer)
}
