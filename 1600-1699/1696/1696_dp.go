package main

import "fmt"

func main() {
	var n, k int
	var p int64
	fmt.Scan(&n, &k, &p)
	// salaries by rank must avoid a strictly decreasing triple; the state is
	// a, the largest salary so far, and b, the largest salary that follows a
	// larger one (0 if none); ways[a][b] counts such prefixes modulo p
	grid := func() [][]int64 {
		g := make([][]int64, k+1)
		for i := range g {
			g[i] = make([]int64, k+1)
		}
		return g
	}
	ways := grid()
	for z := 1; z <= k; z++ {
		ways[z][0] = 1 % p
	}
	for step := 1; step < n; step++ {
		next := grid()
		// a new salary z is allowed when z >= b, and turns (a, b) into (a, z) if
		// z < a, or into (z, b) if z >= a
		// z < a: (a, b) -> (a, z) for every b <= z, a prefix sum along the row
		for a := 1; a <= k; a++ {
			running := int64(0)
			for c := 0; c < a; c++ {
				running = (running + ways[a][c]) % p
				if c > 0 {
					next[a][c] = running
				}
			}
		}
		// z >= a: (a, b) -> (z, b) for every a <= z, a prefix sum down the column
		for b := 0; b < k; b++ {
			running := int64(0)
			for z := b + 1; z <= k; z++ {
				running = (running + ways[z][b]) % p
				next[z][b] = (next[z][b] + running) % p
			}
		}
		ways = next
	}
	total := int64(0)
	for _, row := range ways {
		for _, x := range row {
			total = (total + x) % p
		}
	}
	// month total + 1 counted from the first month, numbered 1..p in its year
	fmt.Println(total + 1)
}
