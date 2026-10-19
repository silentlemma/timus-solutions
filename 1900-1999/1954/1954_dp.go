package main

import (
	"bufio"
	"fmt"
	"os"
)

const alphabet = 26
const target = 5
const unreachable = target + 1
const outerSplit = 3

type node struct {
	next                       [alphabet]int
	length, link, diff, series int
	best, start                [2]int
}

func main() {
	input := bufio.NewReader(os.Stdin)
	output := bufio.NewWriter(os.Stdout)
	defer output.Flush()
	var text string
	fmt.Fscan(input, &text)
	n := len(text)
	data := " " + text
	tree := make([]node, n+2)
	for i := range tree {
		tree[i].best = [2]int{unreachable, unreachable}
	}
	tree[0].length = -1
	best, parent := make([][2]int, n+1), make([][2]int, n+1)
	for i := range best {
		best[i] = [2]int{unreachable, unreachable}
	}
	best[0][0] = 0
	count, last := 2, 1
	for i := 1; i <= n; i++ {
		code, current := int(data[i]-'a'), last
		for data[i-tree[current].length-1] != data[i] {
			current = tree[current].link
		}
		following := tree[current].next[code]
		if following == 0 {
			following = count
			count++
			tree[current].next[code] = following
			item := &tree[following]
			item.length = tree[current].length + 2
			if item.length == 1 {
				item.link = 1
			} else {
				suffix := tree[current].link
				for data[i-tree[suffix].length-1] != data[i] {
					suffix = tree[suffix].link
				}
				item.link = tree[suffix].next[code]
			}
			item.diff = item.length - tree[item.link].length
			if item.diff == tree[item.link].diff {
				item.series = tree[item.link].series
			} else {
				item.series = item.link
			}
		}
		last = following
		for v := last; tree[v].length > 0; v = tree[v].series {
			item := &tree[v]
			base := i - tree[item.series].length - item.diff
			for p := 0; p < 2; p++ {
				item.best[p] = best[base][p]
				item.start[p] = base
				if item.diff == tree[item.link].diff && tree[item.link].best[p] < item.best[p] {
					item.best[p] = tree[item.link].best[p]
					item.start[p] = tree[item.link].start[p]
				}
				if item.best[p]+1 < best[i][p^1] {
					best[i][p^1] = item.best[p] + 1
					parent[i][p^1] = item.start[p]
				}
			}
		}
	}
	if best[n][1] > target {
		fmt.Fprintln(output, "NO")
		return
	}
	result := []string{}
	for i, parity := n, 1; i > 0; parity ^= 1 {
		before := parent[i][parity]
		result = append(result, text[before:i])
		i = before
	}
	for i, j := 0, len(result)-1; i < j; i, j = i+1, j-1 {
		result[i], result[j] = result[j], result[i]
	}
	for len(result) < target {
		long := -1
		for i, part := range result {
			if len(part) >= outerSplit {
				long = i
				break
			}
		}
		next := []string{}
		if long >= 0 {
			for i, part := range result {
				if i == long {
					next = append(next, part[:1], part[1:len(part)-1], part[len(part)-1:])
				} else {
					next = append(next, part)
				}
			}
		} else {
			remaining := 2
			for _, part := range result {
				if len(part) == 2 && remaining > 0 {
					next = append(next, part[:1], part[1:])
					remaining--
				} else {
					next = append(next, part)
				}
			}
		}
		result = next
	}
	fmt.Fprintln(output, "YES")
	for _, part := range result {
		fmt.Fprintln(output, part)
	}
}
