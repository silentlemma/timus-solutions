package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	children := make([][]int, n+1)
	value := make([]int, n+1)
	depth := make([]int, n+1)
	for v := 2; v <= n; v++ {
		var kind string
		var parent int
		fmt.Fscan(in, &kind, &parent)
		children[parent] = append(children[parent], v)
		if kind == "L" {
			fmt.Fscan(in, &value[v])
		}
	}
	// breadth-first order from the root, then values from the leaves up:
	// the first player moves at even depths and takes the largest result
	order := []int{1}
	for i := 0; i < len(order); i++ {
		for _, c := range children[order[i]] {
			depth[c] = depth[order[i]] + 1
			order = append(order, c)
		}
	}
	for i := len(order) - 1; i >= 0; i-- {
		v := order[i]
		if len(children[v]) == 0 {
			continue
		}
		best := value[children[v][0]]
		for _, c := range children[v] {
			if (depth[v]%2 == 0) == (value[c] > best) {
				best = value[c]
			}
		}
		value[v] = best
	}
	switch {
	case value[1] > 0:
		fmt.Println("+1")
	case value[1] < 0:
		fmt.Println("-1")
	default:
		fmt.Println("0")
	}
}
