package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

func gcd(a, b int64) int64 {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func abs(x int64) int64 {
	if x < 0 {
		return -x
	}
	return x
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Split(bufio.ScanWords)
	next := func() int64 {
		scanner.Scan()
		v, _ := strconv.Atoi(scanner.Text())
		return int64(v)
	}
	n := int(next())
	s := make([]int64, n)
	q := make([]int64, n)
	for i := range s {
		s[i] = next()
	}
	var g int64
	for i := range q {
		q[i] = next()
		g = gcd(g, q[i])
	}
	var total int64
	for i := range q {
		q[i] /= g
		total += q[i]
	}
	// The heaps become k * q for an integer k >= 1, and the cost
	// sum |s - k q| = sum q |s / q - k| is convex in k with its real minimum
	// at the median of the ratios s / q weighted by q.
	order := make([]int, n)
	for i := range order {
		order[i] = i
	}
	sort.Slice(order, func(a, b int) bool {
		i, j := order[a], order[b]
		return s[i]*q[j] < s[j]*q[i]
	})
	var weight int64
	median := order[n-1]
	for _, i := range order {
		weight += q[i]
		if 2*weight >= total {
			median = i
			break
		}
	}
	low := s[median] / q[median]
	cost := func(k int64) int64 {
		var sum int64
		for i := range s {
			sum += abs(s[i] - k*q[i])
		}
		return sum
	}
	best := cost(low + 1)
	if low >= 1 {
		if c := cost(low); c < best {
			best = c
		}
	}
	fmt.Println(best)
}
