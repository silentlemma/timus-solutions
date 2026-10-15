package main

import "fmt"

func main() {
	var n, s int64
	fmt.Scan(&n, &s)
	yes := s - 2*n // YES takes 3 bytes, NO takes 2
	no := n - yes
	// the first test fails when its answer is NO, any later one when its
	// answer differs from the one before: no / n + (n - 1) * 2 yes no / (n (n - 1))
	fmt.Printf("%.7f\n", float64(no*(2*yes+1))/float64(n))
}
