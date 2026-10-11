package main

import "fmt"

func main() {
	var n, k int
	fmt.Scan(&n, &k)
	if n < k {
		fmt.Println(0)
		return
	}
	// with r = N mod K, an s x s corner square is left over, s = min(r, K - r)
	r := n % k
	s := r
	if k-r < s {
		s = k - r
	}
	fmt.Println((n*n - s*s) / k)
}
