package main

import (
	"bufio"
	"os"
	"sort"
	"strconv"
)

const shown = 10 // suggestions per query

type entry struct {
	word  string
	count int
}

func main() {
	in := bufio.NewScanner(os.Stdin)
	in.Split(bufio.ScanWords)
	next := func() string {
		in.Scan()
		return in.Text()
	}
	n, _ := strconv.Atoi(next())
	words := make([]entry, n)
	for i := range words {
		words[i].word = next()
		words[i].count, _ = strconv.Atoi(next())
	}
	m, _ := strconv.Atoi(next())
	queries := make([]string, m)
	found := make(map[string][]int, m) // query -> indices of its words
	for j := range queries {
		queries[j] = next()
		found[queries[j]] = nil
	}
	// the best words come first, so every queried prefix simply keeps the
	// first ten words that start with it
	sort.Slice(words, func(a, b int) bool {
		if words[a].count != words[b].count {
			return words[a].count > words[b].count
		}
		return words[a].word < words[b].word
	})
	for i, e := range words {
		for end := 1; end <= len(e.word); end++ {
			prefix := e.word[:end]
			if box, ok := found[prefix]; ok && len(box) < shown {
				found[prefix] = append(box, i)
			}
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for j, q := range queries {
		if j > 0 {
			out.WriteByte('\n')
		}
		for _, i := range found[q] {
			out.WriteString(words[i].word)
			out.WriteByte('\n')
		}
	}
}
