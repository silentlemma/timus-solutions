package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	step = 10 // every tenth person is fined
	inf  = 1 << 30
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, k int
	if _, err := fmt.Fscan(in, &n, &k); err != nil {
		return
	}
	var good string
	fmt.Fscan(in, &good)
	b2i := func(b bool) int {
		if b {
			return 1
		}
		return 0
	}
	// cost[i][j] holds the least fines once i conductors and j friends stand
	// in line, and the next person then stands at place i + j + 1
	cost := make([][]int, n+1)
	for i := range cost {
		cost[i] = make([]int, k+1)
		for j := range cost[i] {
			cost[i][j] = inf
		}
	}
	cost[0][0] = 0
	for i := 0; i <= n; i++ {
		for j := 0; j <= k; j++ {
			here := cost[i][j]
			if here == inf {
				continue
			}
			fined := (i+j+1)%step == 0
			if j < k && here+b2i(fined) < cost[i][j+1] {
				cost[i][j+1] = here + b2i(fined) // a friend steps in
			}
			if i < n {
				if v := here + b2i(fined && good[i] == '1'); v < cost[i+1][j] {
					cost[i+1][j] = v
				}
			}
		}
	}
	j := 0
	for t := range cost[n] {
		if cost[n][t] < cost[n][j] {
			j = t
		}
	}
	best := cost[n][j]
	// walk back: a friend was added wherever the cost came from the left
	var places []int
	for i := n; i > 0 || j > 0; {
		fined := (i+j)%step == 0
		if i > 0 && cost[i-1][j]+b2i(fined && good[i-1] == '1') == cost[i][j] {
			i--
		} else {
			places = append(places, i+j)
			j--
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	fmt.Fprintf(out, "%d\n%d", best, len(places))
	for t := len(places) - 1; t >= 0; t-- {
		fmt.Fprintf(out, " %d", places[t])
	}
	fmt.Fprintln(out)
}
