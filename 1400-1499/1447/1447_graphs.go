package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

const bufSize = 1 << 16

var n int
var cost, dist []int64 // n by n, 0 marks a missing link, real values are positive

func gcd(a, b int64) int64 {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

// Prim on the weights c q - d p, exact integers; returns the tree's
// total weight, cost and length
func tree(p, q int64) (int64, int64, int64) {
	best := make([]int64, n)
	bc := make([]int64, n)
	bd := make([]int64, n)
	used := make([]bool, n)
	for i := range best {
		best[i] = math.MaxInt64
	}
	best[0] = 0
	var total, tc, td int64
	for step := 0; step < n; step++ {
		u := -1
		for v := 0; v < n; v++ {
			if !used[v] && (u < 0 || best[v] < best[u]) {
				u = v
			}
		}
		used[u] = true
		total, tc, td = total+best[u], tc+bc[u], td+bd[u]
		cu, du := cost[u*n:(u+1)*n], dist[u*n:(u+1)*n]
		for v := 0; v < n; v++ {
			if cu[v] != 0 && !used[v] {
				if w := cu[v]*q - du[v]*p; w < best[v] {
					best[v], bc[v], bd[v] = w, cu[v], du[v]
				}
			}
		}
	}
	return total, tc, td
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, bufSize)
	readInt := func() int {
		x := 0
		c, _ := reader.ReadByte()
		for c < '0' {
			c, _ = reader.ReadByte()
		}
		for c >= '0' {
			x = x*10 + int(c-'0')
			var err error
			if c, err = reader.ReadByte(); err != nil {
				break
			}
		}
		return x
	}
	n = readInt()
	m := readInt()
	cost = make([]int64, n*n)
	dist = make([]int64, n*n)
	for i := 0; i < m; i++ {
		a, b := readInt()-1, readInt()-1
		d, c := int64(readInt()), int64(readInt())
		cost[a*n+b], cost[b*n+a] = c, c
		dist[a*n+b], dist[b*n+a] = d, d
	}
	// Dinkelbach: the ratio p / q of the last tree drops until no tree beats it
	_, p, q := tree(0, 1)
	for {
		total, tc, td := tree(p, q)
		if total >= 0 {
			break
		}
		g := gcd(tc, td)
		p, q = tc/g, td/g
	}
	fmt.Printf("%.10f\n", float64(p)/float64(q))
}
