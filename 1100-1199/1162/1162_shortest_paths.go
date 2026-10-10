package main

import (
	"bufio"
	"fmt"
	"os"
)

// eps: sums closer than this count as equal
const eps = 1e-9

type exchange struct {
	from, to  int
	rate, fee float64
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, m, s int
	var v float64
	fmt.Fscan(in, &n, &m, &s, &v)
	var edges []exchange
	for k := 0; k < m; k++ {
		var a, b int
		var rab, cab, rba, cba float64
		fmt.Fscan(in, &a, &b, &rab, &cab, &rba, &cba)
		edges = append(edges, exchange{a, b, rab, cab}, exchange{b, a, rba, cba})
	}
	// best[c] is the most money of currency c that can be held; a pass that
	// still improves something after n passes has found a gaining cycle
	best := make([]float64, n+1)
	for c := range best {
		best[c] = -1
	}
	best[s] = v
	changed := false
	for pass := 0; pass < n; pass++ {
		changed = false
		for _, e := range edges {
			if best[e.from]-e.fee >= 0 {
				if got := (best[e.from] - e.fee) * e.rate; got > best[e.to]+eps {
					best[e.to] = got
					changed = true
				}
			}
		}
		if best[s] > v+eps || !changed {
			break
		}
	}
	if best[s] > v+eps || changed {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}
}
