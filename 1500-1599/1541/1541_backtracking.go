package main

import (
	"fmt"
	"strconv"
	"strings"
)

const (
	fastest = 100000 // no speed above this
	most    = 19     // K < 20 leagues
	slack   = 1e-9   // floating point margin for the pruning bound
	big     = 1 << 61
)

var (
	harmonic [fastest + 2]float64
	path     []int64
)

func gcd(a, b int64) int64 {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

// largest is the largest sum of count unit fractions with denominators from start
func largest(start int64, count int) float64 {
	end := start + int64(count) - 1
	if end > fastest {
		end = fastest
	}
	if start > end {
		return 0
	}
	return harmonic[end] - harmonic[start-1]
}

// search writes p / q as left or fewer unit fractions above 1 / last
func search(p, q, last int64, left int) bool {
	if p == 0 {
		return true
	}
	if left == 0 {
		return false
	}
	start := (q + p - 1) / p // 1 / d must fit into p / q
	if start <= last {
		start = last + 1
	}
	// left fractions of 1 / d at most
	stop := int64(fastest)
	if q <= big/int64(left) && int64(left)*q/p < stop {
		stop = int64(left) * q / p
	}
	if start > stop || largest(start, left)+slack < float64(p)/float64(q) {
		return false
	}
	for d := start; d <= stop; d++ {
		if float64(p)/float64(q)-1.0/float64(d) > largest(d+1, left-1)+slack {
			continue
		}
		// keep every fraction within 64 bits
		if q > big/d || p > big/d {
			continue
		}
		np, nq := p*d-q, q*d
		g := gcd(np, nq)
		path = append(path, d)
		if search(np/g, nq/g, d, left-1) {
			return true
		}
		path = path[:len(path)-1]
	}
	return false
}

func main() {
	var m, n int64
	fmt.Scan(&m, &n)
	// M / N hours over legs of one league each: M / N = 1 / V1 + ... + 1 / VK
	// with distinct whole speeds, a sum of distinct unit fractions
	for d := 1; d <= fastest; d++ {
		harmonic[d] = harmonic[d-1] + 1.0/float64(d)
	}
	// the fewest fractions first keeps the search small
	for k := 1; k <= most; k++ {
		if search(m, n, 0, k) {
			speeds := make([]string, len(path))
			for i, d := range path {
				speeds[len(path)-1-i] = strconv.FormatInt(d, 10)
			}
			fmt.Println(len(path))
			fmt.Println(strings.Join(speeds, " "))
			return
		}
	}
	fmt.Println(-1)
}
