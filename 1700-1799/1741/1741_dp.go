package main

import (
	"bufio"
	"fmt"
	"os"
)

const inf = int64(1) << 62

type update struct {
	to   int
	size int64
	kind byte // 'P'irated, 'C'racked or 'L'icensed
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, m int
	fmt.Fscan(in, &n, &m)
	updates := make([][]update, n+1)
	for i := 0; i < m; i++ {
		var x, y int
		var d int64
		var kind string
		fmt.Fscan(in, &x, &y, &d, &kind)
		updates[x] = append(updates[x], update{y, d, kind[0]})
	}
	// updates only go up, so the versions can be taken in order; the
	// client is either still licensed (0) or already pirated (1)
	best := make([][2]int64, n+1)
	for i := range best {
		best[i] = [2]int64{inf, inf}
	}
	best[1][0] = 0
	for v := 1; v <= n; v++ {
		for _, u := range updates[v] {
			for state := 0; state < 2; state++ {
				if best[v][state] == inf || (u.kind == 'L' && state == 1) {
					continue
				}
				cost := best[v][state] + u.size
				target := &best[u.to][state]
				if u.kind == 'P' {
					target = &best[u.to][1]
				}
				if cost < *target {
					*target = cost
				}
			}
		}
	}
	answer := best[n][0]
	if best[n][1] < answer {
		answer = best[n][1]
	}
	if answer == inf {
		fmt.Println("Offline")
	} else {
		fmt.Printf("Online\n%d\n", answer)
	}
}
