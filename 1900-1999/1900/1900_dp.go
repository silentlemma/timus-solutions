package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
)

const infinity = 1000000000

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	position := 0
	next := func() int {
		for position < len(data) && data[position] <= ' ' {
			position++
		}
		value := 0
		for position < len(data) && data[position] >= '0' && data[position] <= '9' {
			value = value*10 + int(data[position]-'0')
			position++
		}
		return value
	}
	n, k := next(), next()
	width := n + 1
	weights, cost := make([][]int, width), make([][]int, width)
	for i := 0; i < width; i++ {
		weights[i], cost[i] = make([]int, width), make([]int, width)
	}
	for left := 1; left < n; left++ {
		for right := left + 1; right <= n; right++ {
			weights[left][right] = next()
		}
	}
	for left := n - 1; left >= 1; left-- {
		prefix := 0
		for right := left + 1; right <= n; right++ {
			prefix += weights[left][right]
			cost[left][right] = cost[left+1][right] + prefix
		}
	}
	groups := k + 1
	previous := make([]int, width)
	for i := range previous {
		previous[i] = infinity
	}
	for end := 1; end <= n-groups+1; end++ {
		previous[end] = cost[1][end]
	}
	parents := make([][]int, groups+1)
	for group := 2; group <= groups; group++ {
		current, parent := make([]int, width), make([]int, width)
		for i := range current {
			current[i] = infinity
		}
		var fill func(int, int, int, int)
		fill = func(left, right, first, last int) {
			if left > right {
				return
			}
			middle := (left + right) / 2
			best, split := infinity, first
			limit := last
			if middle-1 < limit {
				limit = middle - 1
			}
			for cut := first; cut <= limit; cut++ {
				value := previous[cut] + cost[cut+1][middle]
				if value < best {
					best, split = value, cut
				}
			}
			current[middle], parent[middle] = best, split
			fill(left, middle-1, first, split)
			fill(middle+1, right, split, last)
		}
		end := n - groups + group
		fill(group, end, group-1, end-1)
		previous, parents[group] = current, parent
	}
	cuts, end := make([]int, k), n
	for group := groups; group > 1; group-- {
		end = parents[group][end]
		cuts[group-2] = end
	}
	out := bufio.NewWriter(os.Stdout)
	fmt.Fprintln(out, cost[1][n]-previous[n])
	for i, cut := range cuts {
		if i > 0 {
			fmt.Fprint(out, " ")
		}
		fmt.Fprint(out, cut)
	}
	fmt.Fprintln(out)
	out.Flush()
}
