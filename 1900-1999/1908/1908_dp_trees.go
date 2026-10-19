package main

import (
	"bufio"
	"fmt"
	"os"
)

type trieNode struct {
	first, next, leaves, normal, supplied int
	label                                 byte
}

func minimumClicks(words []string) int {
	capacity := 1
	for _, word := range words {
		capacity += len(word)
	}
	nodes := make([]trieNode, 1, capacity)
	for _, word := range words {
		node := 0
		for index := 0; index < len(word); index++ {
			letter := word[index]
			child := nodes[node].first
			for child != 0 && nodes[child].label != letter {
				child = nodes[child].next
			}
			if child == 0 {
				child = len(nodes)
				nodes = append(nodes, trieNode{next: nodes[node].first, label: letter})
				nodes[node].first = child
			}
			node = child
		}
	}
	for node := len(nodes) - 1; node >= 0; node-- {
		child := nodes[node].first
		if child == 0 {
			nodes[node].leaves = 1
			continue
		}
		total, bestNormal, bestSupplied := 0, 0, 0
		for child != 0 {
			count := nodes[child].leaves
			nodes[node].leaves += count
			total += nodes[child].normal + count
			saving := nodes[child].normal - nodes[child].supplied
			if saving > bestNormal {
				bestNormal = saving
			}
			if count+saving > bestSupplied {
				bestSupplied = count + saving
			}
			child = nodes[child].next
		}
		nodes[node].normal = total - bestNormal
		nodes[node].supplied = total - bestSupplied
	}
	return nodes[0].normal
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var count int
	fmt.Fscan(in, &count)
	words := make([]string, count)
	for index := range words {
		fmt.Fscan(in, &words[index])
	}
	fmt.Fprintln(out, minimumClicks(words))
}
