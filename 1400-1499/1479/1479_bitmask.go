package main

import (
	"fmt"
	"math/bits"
)

const shortest = 3 // a route has at least three stops

func main() {
	var n, m int
	fmt.Scan(&n, &m)
	adj := make([]int, n)
	for i := 0; i < m; i++ {
		var a, b int
		fmt.Scan(&a, &b)
		a, b = a-1, b-1
		adj[a] |= 1 << uint(b)
		adj[b] |= 1 << uint(a)
	}

	// paths[mask*n+v]: simple paths from the lowest stop of mask through
	// all of mask, ending at v; a path that can close counts its cycle twice
	full := 1<<uint(n) - 1
	paths := make([]int64, (full+1)*n)
	cycles := make([]int64, full+1)
	for s := 0; s < n; s++ {
		paths[(1<<uint(s))*n+s] = 1
	}
	for mask := 1; mask <= full; mask++ {
		low := mask & -mask
		start := uint(bits.TrailingZeros(uint(mask)))
		free := ^mask & ^(low<<1 - 1) & full // stops that may still join
		var closing int64
		for v := 0; v < n; v++ {
			count := paths[mask*n+v]
			if count == 0 {
				continue
			}
			if adj[v]>>start&1 == 1 {
				closing += count
			}
			for step := adj[v] & free; step != 0; step &= step - 1 {
				u := bits.TrailingZeros(uint(step))
				paths[(mask|1<<uint(u))*n+u] += count
			}
		}
		if bits.OnesCount(uint(mask)) >= shortest {
			cycles[mask] = closing / 2
		}
	}

	// the bipartite graph of routes and stops needs as many rows as its
	// largest degree: the longest route or the busiest stop
	var best int64
	through := make([]int64, n)
	for mask := 1; mask <= full; mask++ {
		if cycles[mask] == 0 {
			continue
		}
		if size := int64(bits.OnesCount(uint(mask))); size > best {
			best = size
		}
		for v := 0; v < n; v++ {
			if mask>>uint(v)&1 == 1 {
				through[v] += cycles[mask]
			}
		}
	}
	for _, t := range through {
		if t > best {
			best = t
		}
	}
	fmt.Println(best)
}
