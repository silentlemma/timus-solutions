package main

import (
	"bufio"
	"fmt"
	"os"
)

const modulus = 1000000007

func distinctParts(rules [][]int, width int) int {
	limit := width - 1
	prefixes, suffixes := make([]string, len(rules)), make([]string, len(rules))
	visited := make([]bool, len(rules))
	parts := make(map[string]struct{})
	var visit func(int)
	visit = func(vertex int) {
		if visited[vertex] {
			return
		}
		if len(rules[vertex]) == 0 {
			prefixes[vertex] = string([]byte{byte(vertex + 1)})
			suffixes[vertex] = prefixes[vertex]
		} else {
			prefix, suffix := "", ""
			for _, child := range rules[vertex] {
				visit(child)
				span := suffix + prefixes[child]
				for start := 0; start+width <= len(span); start++ {
					parts[span[start:start+width]] = struct{}{}
				}
				prefix += prefixes[child]
				if len(prefix) > limit {
					prefix = prefix[:limit]
				}
				suffix += suffixes[child]
				if len(suffix) > limit {
					suffix = suffix[len(suffix)-limit:]
				}
			}
			prefixes[vertex], suffixes[vertex] = prefix, suffix
		}
		visited[vertex] = true
	}
	for vertex := range rules {
		visit(vertex)
	}
	return len(parts) % modulus
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var count, width int
	fmt.Fscan(in, &count, &width)
	rules := make([][]int, count)
	for vertex := range rules {
		var length int
		fmt.Fscan(in, &length)
		if length != -1 {
			rules[vertex] = make([]int, length)
			for index := range rules[vertex] {
				fmt.Fscan(in, &rules[vertex][index])
				rules[vertex][index]--
			}
		}
	}
	fmt.Println(distinctParts(rules, width))
}
