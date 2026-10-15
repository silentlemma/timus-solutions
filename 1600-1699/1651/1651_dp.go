package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	inf = 1 << 30
	top = 10000 // the largest vertex number
)

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var n int
	if _, err := fmt.Fscan(in, &n); err != nil {
		return
	}
	chain := make([]int, n)
	for i := range chain {
		fmt.Fscan(in, &chain[i])
	}
	end := chain[n-1]
	if chain[0] == end {
		fmt.Fprintln(out, end)
		return
	}
	// dp[i]: fewest edges from position i to the final vertex, taking only
	// edges of p from i on; reaching the final vertex anywhere ends it
	dp, step := make([]int, n), make([]int, n)
	for i := range dp {
		dp[i], step[i] = inf, -1
	}
	// per vertex: the best dp after leaving it and where, latest on ties
	bestValue, bestAt := make([]int, top+1), make([]int, top+1)
	for v := range bestValue {
		bestValue[v] = inf
	}
	dp[n-1] = 0
	for i := n - 2; i >= 0; i-- {
		u := chain[i]
		if dp[i+1] < bestValue[u] {
			bestValue[u], bestAt[u] = dp[i+1], i+1
		}
		if u == end {
			dp[i] = 0
		} else if bestValue[u] < inf {
			dp[i], step[i] = bestValue[u]+1, bestAt[u]
		}
	}
	fmt.Fprint(out, chain[0])
	for i := 0; chain[i] != end; {
		i = step[i]
		fmt.Fprint(out, " ", chain[i])
	}
	fmt.Fprintln(out)
}
