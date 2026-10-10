package main

import (
	"bufio"
	"fmt"
	"os"
)

// among three vectors no longer than L, some sum or difference of two of them
// is no longer than L, so they can be merged into one
const keep = 3

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	var length int64
	fmt.Fscan(in, &n, &length)
	// nodes 0..n-1 are the input vectors, later nodes are merged pairs
	x := make([]int64, 2*n)
	y := make([]int64, 2*n)
	parent := make([]int, 2*n)
	rel := make([]int64, 2*n)
	for k := range parent {
		parent[k], rel[k] = -1, 1
	}
	nodes := n
	join := func(a, b int, s int64) int {
		x[nodes] = x[a] + s*x[b]
		y[nodes] = y[a] + s*y[b]
		parent[a], parent[b] = nodes, nodes
		rel[b] = s
		nodes++
		return nodes - 1
	}
	var active []int
	for i := 0; i < n; i++ {
		fmt.Fscan(in, &x[i], &y[i])
		active = append(active, i)
		if len(active) < keep {
			continue
		}
	search:
		for p := 0; p < keep; p++ {
			for q := p + 1; q < keep; q++ {
				for _, s := range []int64{-1, 1} {
					a, b := active[p], active[q]
					dx, dy := x[a]+s*x[b], y[a]+s*y[b]
					if dx*dx+dy*dy > length*length {
						continue
					}
					var next []int
					for r := 0; r < keep; r++ {
						if r != p && r != q {
							next = append(next, active[r])
						}
					}
					active = append(next, join(a, b, s))
					break search
				}
			}
		}
	}
	// two vectors no longer than L: a sign making their dot product
	// non-positive keeps the sum within sqrt(2) L
	if len(active) == 2 {
		a, b := active[0], active[1]
		s := int64(1)
		if x[a]*x[b]+y[a]*y[b] > 0 {
			s = -1
		}
		join(a, b, s)
	}
	sign := make([]int64, nodes)
	for k := nodes - 1; k >= 0; k-- {
		sign[k] = 1
		if parent[k] >= 0 {
			sign[k] = sign[parent[k]] * rel[k]
		}
	}
	out := make([]byte, n)
	for i := range out {
		out[i] = '+'
		if sign[i] < 0 {
			out[i] = '-'
		}
	}
	fmt.Printf("YES\n%s\n", out)
}
