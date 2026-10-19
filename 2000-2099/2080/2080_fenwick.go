package main

import (
	"bufio"
	"os"
	"sort"
	"strconv"
)

func main() {
	in := bufio.NewScanner(os.Stdin)
	in.Split(bufio.ScanWords)
	next := func() int {
		in.Scan()
		v, _ := strconv.Atoi(in.Text())
		return v
	}
	n, k := next(), next()
	uses := make([]int, k+1)
	for i := 1; i <= k; i++ {
		uses[i] = next()
	}
	// the stack is kept in order of next use: after a card is used, the cards above
	// it are those used before its next use, the distinct cards in between
	nxt := make([]int, k+1)
	seen := make([]int, n+1)
	for card := range seen {
		seen[card] = k + 1
	}
	for i := k; i >= 1; i-- {
		nxt[i] = seen[uses[i]]
		seen[uses[i]] = i
	}
	// Fenwick tree over moments: a moment j counts once the query time i reaches
	// the previous use of its card, so the counted moments are first uses after i
	tree := make([]int, k+1)
	add := func(j int) {
		for ; j <= k; j += j & -j {
			tree[j]++
		}
	}
	prefix := func(j int) int {
		s := 0
		for ; j > 0; j -= j & -j {
			s += tree[j]
		}
		return s
	}
	for card := 1; card <= n; card++ {
		if seen[card] <= k {
			add(seen[card])
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	order := make([]int, n)
	for i := range order {
		order[i] = i + 1
	}
	sort.SliceStable(order, func(a, b int) bool { return seen[order[a]] < seen[order[b]] })
	for i, card := range order {
		if i > 0 {
			out.WriteByte(' ')
		}
		out.WriteString(strconv.Itoa(card))
	}
	out.WriteByte('\n')
	for i := 1; i <= k; i++ {
		if nxt[i] <= k {
			add(nxt[i])
		}
		out.WriteString(strconv.Itoa(prefix(nxt[i]-1) - prefix(i)))
		out.WriteByte('\n')
	}
}
