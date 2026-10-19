package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func solve(text string, limit int) (int, int64) {
	const alphabet = 26
	counts := make([]int, alphabet)
	for index := range text {
		counts[text[index]-'a']++
	}
	sort.Sort(sort.Reverse(sort.IntSlice(counts)))
	size := 0
	for _, count := range counts[:limit] {
		size += count
	}
	boundary := counts[limit-1]
	if boundary == 0 {
		return size, 1
	}
	greater, tied := 0, 0
	for _, count := range counts {
		if count > boundary {
			greater++
		}
		if count == boundary {
			tied++
		}
	}
	chosen := limit - greater
	if tied-chosen < chosen {
		chosen = tied - chosen
	}
	ways := int64(1)
	for index := 1; index <= chosen; index++ {
		ways = ways * int64(tied-index+1) / int64(index)
	}
	return size, ways
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var text string
	var limit int
	if _, err := fmt.Fscan(in, &text, &limit); err != nil {
		return
	}
	size, ways := solve(text, limit)
	fmt.Println(size, ways)
}
