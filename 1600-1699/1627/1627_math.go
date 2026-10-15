package main

import (
	"bufio"
	"fmt"
	"os"
)

const mod = 1000000000

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, m int
	if _, err := fmt.Fscan(in, &n, &m); err != nil {
		return
	}
	grid := make([]string, n)
	for i := range grid {
		fmt.Fscan(in, &grid[i])
	}
	id := make([][]int, n)
	v := 0
	for i := range id {
		id[i] = make([]int, m)
		for j := range id[i] {
			id[i][j] = -1
			if grid[i][j] == '.' {
				id[i][j] = v
				v++
			}
		}
	}
	// the Laplacian of the bedroom graph; by the matrix-tree theorem any
	// cofactor counts its spanning trees (0 when it is disconnected)
	lap := make([][]int64, v)
	for i := range lap {
		lap[i] = make([]int64, v)
	}
	join := func(u, w int) {
		lap[u][u]++
		lap[w][w]++
		lap[u][w]--
		lap[w][u]--
	}
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if id[i][j] < 0 {
				continue
			}
			if i+1 < n && id[i+1][j] >= 0 {
				join(id[i][j], id[i+1][j])
			}
			if j+1 < m && id[i][j+1] >= 0 {
				join(id[i][j], id[i][j+1])
			}
		}
	}
	size := v - 1
	a := make([][]int64, size)
	for i := range a {
		a[i] = make([]int64, size)
		for j := range a[i] {
			a[i][j] = (lap[i][j]%mod + mod) % mod
		}
	}
	// Elimination by Euclid's algorithm on rows: it only subtracts multiples
	// of rows and swaps them, so it works modulo 10^9, which is not prime.
	det := int64(1)
	for k := 0; k < size; k++ {
		for i := k + 1; i < size; i++ {
			for a[i][k] != 0 {
				q := a[k][k] / a[i][k]
				for j := k; j < size; j++ {
					a[k][j] = ((a[k][j]-q*a[i][j])%mod + mod) % mod
				}
				a[k], a[i] = a[i], a[k]
				det = (mod - det) % mod
			}
		}
		det = det * a[k][k] % mod
	}
	fmt.Println(det)
}
