package main

import "fmt"

func main() {
	var n, k int64
	fmt.Scan(&n, &k)
	// as long as fewer computers than cables have the program, each hour doubles
	// the count; after that k computers get it each hour
	have, hours := int64(1), int64(0)
	for have < n && have < k {
		have *= 2
		hours++
	}
	if have < n {
		hours += (n - have + k - 1) / k
	}
	fmt.Println(hours)
}
