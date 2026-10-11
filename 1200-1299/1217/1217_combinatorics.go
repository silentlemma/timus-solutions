package main

import "fmt"

const digits = 10

// sums returns ways[s]: strings of k digits with digit sum s.
func sums(k int) []int64 {
	ways := []int64{1}
	for i := 0; i < k; i++ {
		next := make([]int64, len(ways)+digits-1)
		for s, w := range ways {
			for d := 0; d < digits; d++ {
				next[s+d] += w
			}
		}
		ways = next
	}
	return ways
}

// matching counts pairs of a k-digit and an m-digit string with equal sums.
func matching(k, m int) int64 {
	a, b := sums(k), sums(m)
	total := int64(0)
	for s := 0; s < len(a) && s < len(b); s++ {
		total += a[s] * b[s]
	}
	return total
}

func main() {
	var n int
	fmt.Scan(&n)
	// size[in the first half][odd] counts positions; lucky both ways means the
	// odd digits of the first half sum like the even ones of the second half,
	// and the even digits of the first half like the odd ones of the second
	var size [2][2]int
	for p := 1; p <= n; p++ {
		h := 0
		if p <= n/2 {
			h = 1
		}
		size[h][p%2]++
	}
	fmt.Println(matching(size[1][1], size[0][0]) * matching(size[1][0], size[0][1]))
}
