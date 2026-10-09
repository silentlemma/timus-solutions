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
	rating := make([]int, n+1)
	parent := make([]int, n+1)
	for v := 1; v <= n; v++ {
		fmt.Fscan(in, &rating[v])
	}
	// children as linked lists: first[v], then next[c] for the next sibling
	first := make([]int, n+1)
	next := make([]int, n+1)
	for {
		var child, boss int
		if k, _ := fmt.Fscan(in, &child, &boss); k < 2 || child == 0 {
			break
		}
		parent[child] = boss
		next[child] = first[boss]
		first[boss] = child
	}
	// a breadth-first order from the roots puts every boss before the subordinates
	order := make([]int, 0, n)
	for v := 1; v <= n; v++ {
		if parent[v] == 0 {
			order = append(order, v)
		}
	}
	for i := 0; i < len(order); i++ {
		for c := first[order[i]]; c != 0; c = next[c] {
			order = append(order, c)
		}
	}
	// take[v], skip[v]: the best sum in the subtree of v with v invited or not
	take := make([]int, n+1)
	skip := make([]int, n+1)
	total := 0
	for i := len(order) - 1; i >= 0; i-- {
		v := order[i]
		take[v] += rating[v]
		best := take[v]
		if skip[v] > best {
			best = skip[v]
		}
		if parent[v] == 0 {
			total += best
		} else {
			take[parent[v]] += skip[v]
			skip[parent[v]] += best
		}
	}
	fmt.Println(total)
}
