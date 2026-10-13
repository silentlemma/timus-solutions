package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

// two hashes modulo two primes, packed into one 64-bit key
const (
	mod1, mod2 = 1000000007, 998244353
	row1, row2 = 131, 137
	col1, col2 = 1009, 1013
	half       = 32
	lowMask    = 1<<half - 1
)

var (
	n, m int
	grid [][]byte
)

func power(b uint64, e int, mod uint64) uint64 {
	r := uint64(1)
	for ; e > 0; e-- {
		r = r * b % mod
	}
	return r
}

func same(r1, c1, r2, c2, k int) bool {
	for t := 0; t < k; t++ {
		if string(grid[r1+t][c1:c1+k]) != string(grid[r2+t][c2:c2+k]) {
			return false
		}
	}
	return true
}

type corner struct{ r, c int }

type entry struct {
	key uint64
	pos int
}

// find returns two different equal k x k squares as top-left corners
func find(k int) (bool, [2]corner) {
	width := m - k + 1
	rows := make([][]uint64, n)
	p1, p2 := power(row1, k, mod1), power(row2, k, mod2)
	for i := 0; i < n; i++ {
		rows[i] = make([]uint64, width)
		var h1, h2 uint64
		for j := 0; j < m; j++ {
			c := uint64(grid[i][j])
			h1 = (h1*row1 + c) % mod1
			h2 = (h2*row2 + c) % mod2
			if j >= k {
				old := uint64(grid[i][j-k])
				h1 = (h1 + mod1 - old*p1%mod1) % mod1
				h2 = (h2 + mod2 - old*p2%mod2) % mod2
			}
			if j >= k-1 {
				rows[i][j-k+1] = h1<<half | h2
			}
		}
	}
	p1, p2 = power(col1, k, mod1), power(col2, k, mod2)
	c1s, c2s := make([]uint64, width), make([]uint64, width)
	keys := make([]entry, 0, (n-k+1)*width)
	for i := 0; i < n; i++ {
		for j := 0; j < width; j++ {
			c1s[j] = (c1s[j]*col1 + rows[i][j]>>half) % mod1
			c2s[j] = (c2s[j]*col2 + rows[i][j]&lowMask) % mod2
			if i >= k {
				c1s[j] = (c1s[j] + mod1 - (rows[i-k][j]>>half)*p1%mod1) % mod1
				c2s[j] = (c2s[j] + mod2 - (rows[i-k][j]&lowMask)*p2%mod2) % mod2
			}
			if i >= k-1 {
				keys = append(keys, entry{c1s[j]<<half | c2s[j], (i-k+1)*width + j})
			}
		}
	}
	sort.Slice(keys, func(a, b int) bool {
		if keys[a].key != keys[b].key {
			return keys[a].key < keys[b].key
		}
		return keys[a].pos < keys[b].pos
	})
	for t := 1; t < len(keys); t++ {
		if keys[t].key == keys[t-1].key {
			a, b := keys[t-1].pos, keys[t].pos
			pair := [2]corner{{a / width, a % width}, {b / width, b % width}}
			if same(pair[0].r, pair[0].c, pair[1].r, pair[1].c, k) {
				return true, pair
			}
		}
	}
	return false, [2]corner{}
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Fscan(reader, &n, &m)
	grid = make([][]byte, n)
	for i := range grid {
		var line string
		fmt.Fscan(reader, &line)
		grid[i] = []byte(line)
	}
	// equal k x k squares contain equal (k - 1) x (k - 1) ones, so the
	// largest size can be found by binary search
	lo, hi, best := 1, n, 0
	if m < hi {
		hi = m
	}
	var where [2]corner
	for lo <= hi {
		k := (lo + hi) / 2
		if ok, corners := find(k); ok {
			best, where, lo = k, corners, k+1
		} else {
			hi = k - 1
		}
	}
	if best == 0 {
		fmt.Println(0)
		return
	}
	fmt.Printf("%d\n%d %d\n%d %d\n", best, where[0].r+1, where[0].c+1, where[1].r+1, where[1].c+1)
}
