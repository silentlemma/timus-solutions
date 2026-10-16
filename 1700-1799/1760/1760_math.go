package main

import "fmt"

var big, small int64

func pairs(k int64) int64 { return k * (k - 1) / 2 }

func gcd(x, y int64) int64 {
	for y != 0 {
		x, y = y, x%y
	}
	return x
}

// shared counts pairs among the first m sleepers on one page of both
// notebooks: it walks the pages of the larger size, each cut by the smaller
// pages into a head, whole pages and a tail
func shared(m int64) int64 {
	var total int64
	for start := int64(0); start < m; start += big {
		end := start + big
		if end > m {
			end = m
		}
		cut := (start/small + 1) * small
		if cut >= end {
			total += pairs(end - start)
		} else {
			whole, tail := (end-cut)/small, (end-cut)%small
			total += pairs(cut-start) + whole*pairs(small) + pairs(tail)
		}
	}
	return total
}

func main() {
	var a, b, n int64
	if _, err := fmt.Scan(&a, &b, &n); err != nil {
		return
	}
	big, small = a, b
	if small > big {
		big, small = small, big
	}
	// both page breaks repeat every lcm(a, b) sleepers, and so do the pairs
	period := a / gcd(a, b) * b
	var both int64
	if period <= n {
		both = n/period*shared(period) + shared(n%period)
	} else {
		both = shared(n)
	}
	vasily := n/a*pairs(a) + pairs(n%a)
	fmt.Println(vasily - both)
}
