package main

import "fmt"

var parent []int

func find(x int) int {
	root := x
	for parent[root] != root {
		root = parent[root]
	}
	for parent[x] != root {
		parent[x], x = root, parent[x]
	}
	return root
}

func main() {
	var k int64
	fmt.Scan(&k)
	// roots[v]: the residues s with v + s * s = 0 (mod k), the residues of
	// the earlier numbers b joined to a number a = v by a + b * b = 0
	roots := make([][]int64, k)
	written := make([][]int, k)
	for s := int64(0); s < k; s++ {
		v := (k - s*s%k) % k
		roots[v] = append(roots[v], s)
	}
	parent = []int{0}
	for a := 1; ; a++ {
		parent = append(parent, a)
		r := int64(a) % k
		square := (k - r*r%k) % k
		near := roots[r]
		seen := false
		for _, s := range near {
			seen = seen || s == square
		}
		if !seen {
			near = append(append([]int64(nil), near...), square)
		}
		for _, s := range near {
			for _, b := range written[s] {
				// every edge either joins two trees or closes the first cycle
				ra, rb := find(a), find(b)
				if ra == rb {
					fmt.Println(a)
					return
				}
				parent[rb] = ra
			}
		}
		written[r] = append(written[r], a)
	}
}
