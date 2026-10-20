package main

import (
	"bufio"
	"fmt"
	"os"
)

const alphabet = 26

type suffixLcp struct {
	length int
	size   int
	rank   []int
	tree   []int
}

type candidate struct {
	start int
	cost  int
}

func minimum(first, second int) int {
	if first < second {
		return first
	}
	return second
}

func maximum(first, second int) int {
	if first > second {
		return first
	}
	return second
}

func newSuffixLcp(text string) suffixLcp {
	length := len(text)
	total := length + 1
	symbol := make([]int, total)
	order := make([]int, total)
	group := make([]int, total)
	shifted := make([]int, total)
	next := make([]int, total)
	count := make([]int, maximum(total, alphabet+1))
	for i := 0; i < length; i++ {
		symbol[i] = int(text[i]-'a') + 1
	}
	for _, value := range symbol {
		count[value]++
	}
	for i := 1; i <= alphabet; i++ {
		count[i] += count[i-1]
	}
	for i := total - 1; i >= 0; i-- {
		count[symbol[i]]--
		order[count[symbol[i]]] = i
	}
	classes := 1
	for i := 1; i < total; i++ {
		if symbol[order[i]] != symbol[order[i-1]] {
			classes++
		}
		group[order[i]] = classes - 1
	}
	for width := 1; width < total && classes < total; width *= 2 {
		for i := 0; i < classes; i++ {
			count[i] = 0
		}
		for i := 0; i < total; i++ {
			shifted[i] = order[i] - width
			if shifted[i] < 0 {
				shifted[i] += total
			}
			count[group[shifted[i]]]++
		}
		for i := 1; i < classes; i++ {
			count[i] += count[i-1]
		}
		for i := total - 1; i >= 0; i-- {
			value := group[shifted[i]]
			count[value]--
			order[count[value]] = shifted[i]
		}
		classes = 1
		next[order[0]] = 0
		for i := 1; i < total; i++ {
			current, previous := order[i], order[i-1]
			if group[current] != group[previous] ||
				group[(current+width)%total] != group[(previous+width)%total] {
				classes++
			}
			next[current] = classes - 1
		}
		group, next = next, group
	}
	rank := make([]int, length)
	for i := 0; i < length; i++ {
		rank[order[i+1]] = i
	}
	lcp := make([]int, length)
	matched := 0
	for i := 0; i < length; i++ {
		position := rank[i]
		if position == 0 {
			matched = 0
			continue
		}
		previous := order[position]
		for i+matched < length && previous+matched < length &&
			text[i+matched] == text[previous+matched] {
			matched++
		}
		lcp[position] = matched
		if matched > 0 {
			matched--
		}
	}
	size := 1
	for size < length {
		size *= 2
	}
	tree := make([]int, size*2)
	for i := range tree {
		tree[i] = length
	}
	copy(tree[size:], lcp)
	for i := size - 1; i > 0; i-- {
		tree[i] = minimum(tree[i*2], tree[i*2+1])
	}
	return suffixLcp{length, size, rank, tree}
}

func (lcp suffixLcp) query(first, second int) int {
	left, right := lcp.rank[first], lcp.rank[second]
	if left > right {
		left, right = right, left
	}
	left += lcp.size + 1
	right += lcp.size + 1
	answer := lcp.length
	for left < right {
		if left%2 == 1 {
			answer = minimum(answer, lcp.tree[left])
			left++
		}
		if right%2 == 1 {
			right--
			answer = minimum(answer, lcp.tree[right])
		}
		left /= 2
		right /= 2
	}
	return answer
}

func main() {
	input := bufio.NewReader(os.Stdin)
	output := bufio.NewWriter(os.Stdout)
	defer output.Flush()
	var length int
	var text string
	fmt.Fscan(input, &length, &text)
	lcp := newSuffixLcp(text)
	var starts [alphabet][]candidate
	var reach [alphabet + 1]int
	for i := range reach {
		reach[i] = -1
	}
	active := alphabet + 1
	skipped := 0
	// An optimal choice leaves at most one occurrence of each letter.
	for position := 0; position <= length; position++ {
		for active <= alphabet && reach[active] < position {
			active++
		}
		if position > 0 {
			skipped = minimum(skipped+1, active)
		}
		if position == length {
			break
		}
		letter := int(text[position] - 'a')
		farthest := position
		for index := len(starts[letter]) - 1; index >= 0; index-- {
			previous := starts[letter][index]
			if text[previous.start+farthest-position] != text[farthest] {
				continue
			}
			end := position + lcp.query(previous.start, position)
			if end > farthest {
				reach[previous.cost] = maximum(reach[previous.cost], end)
				active = minimum(active, previous.cost)
				farthest = end
			}
			if farthest == length {
				break
			}
		}
		// Keep each strict improvement over all earlier starts with this letter.
		if len(starts[letter]) == 0 || skipped < starts[letter][len(starts[letter])-1].cost {
			starts[letter] = append(starts[letter], candidate{position, skipped})
		}
	}
	fmt.Fprintln(output, length-skipped)
}
