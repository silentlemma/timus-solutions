package main

import "fmt"

const first = 2 // the first step removes every second day

// quiet counts the quiet days among the first n: step k removes every k-th of
// those still left, which is n / k of a prefix of length n, until n < k
func quiet(n int64) int64 {
	for k := int64(first); n >= k; k++ {
		n -= n / k
	}
	return n
}

func main() {
	var left, right int64
	fmt.Scan(&left, &right)
	fmt.Println(quiet(right) - quiet(left-1))
}
