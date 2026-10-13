package main

import (
	"bufio"
	"fmt"
	"os"
)

const none = -1 // no subordinate yet: a private cannot be cut

func main() {
	reader := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(reader, &n)
	boss, price := make([]int, n+1), make([]int, n+1)
	for i := 2; i <= n; i++ {
		fmt.Fscan(reader, &boss[i], &price[i])
	}
	// cut[v]: the cheapest way to separate v from every private below it
	cut := make([]int64, n+1)
	for i := range cut {
		cut[i] = none
	}
	for v := n; v >= 2; v-- {
		cost := int64(price[v])
		if cut[v] != none && cut[v] < cost {
			cost = cut[v]
		}
		p := boss[v]
		if cut[p] == none {
			cut[p] = cost
		} else {
			cut[p] += cost
		}
	}
	fmt.Printf("%d.00\n", cut[1])
}
