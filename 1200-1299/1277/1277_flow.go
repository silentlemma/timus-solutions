package main

import (
	"bufio"
	"fmt"
	"os"
)

var head, to, capacity, next, level, current []int
var sink int

func arc(a, b, c int) {
	to, capacity, next = append(to, b), append(capacity, c), append(next, head[a])
	head[a] = len(to) - 1
	to, capacity, next = append(to, a), append(capacity, 0), append(next, head[b])
	head[b] = len(to) - 1
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func push(u, limit int) int {
	if u == sink {
		return limit
	}
	for ; current[u] >= 0; current[u] = next[current[u]] {
		e := current[u]
		v := to[e]
		if capacity[e] > 0 && level[v] == level[u]+1 {
			if got := push(v, min(limit, capacity[e])); got > 0 {
				capacity[e] -= got
				capacity[e^1] += got
				return got
			}
		}
	}
	return 0
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var k, n, m, s, f int
	fmt.Fscan(in, &k, &n, &m, &s, &f)
	cost := make([]int, n)
	for i := range cost {
		fmt.Fscan(in, &cost[i])
	}
	if s == f {
		fmt.Println("NO")
		return
	}
	// station v enters at 2v and leaves at 2v + 1; the arc between them
	// costs the police needed there. Museum and refuge cannot be taken,
	// and anything above K counts as too much
	big := k + 1
	head = make([]int, 2*n)
	for i := range head {
		head[i] = -1
	}
	for v := 0; v < n; v++ {
		c := min(cost[v], big)
		if v+1 == s || v+1 == f {
			c = big
		}
		arc(2*v, 2*v+1, c)
	}
	for i := 0; i < m; i++ {
		var a, b int
		fmt.Fscan(in, &a, &b)
		a, b = a-1, b-1
		arc(2*a+1, 2*b, big)
		arc(2*b+1, 2*a, big)
	}
	source := 2*(s-1) + 1
	sink = 2 * (f - 1)
	// Dinic's blocking flows until the flow exceeds K or nothing gets through
	flow := 0
	for flow <= k {
		level = make([]int, 2*n)
		for i := range level {
			level[i] = -1
		}
		level[source] = 0
		queue := []int{source}
		for len(queue) > 0 {
			u := queue[0]
			queue = queue[1:]
			for e := head[u]; e >= 0; e = next[e] {
				if capacity[e] > 0 && level[to[e]] < 0 {
					level[to[e]] = level[u] + 1
					queue = append(queue, to[e])
				}
			}
		}
		if level[sink] < 0 {
			break
		}
		current = append([]int(nil), head...)
		for flow <= k {
			got := push(source, big)
			if got == 0 {
				break
			}
			flow += got
		}
	}
	if flow <= k {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}
}
