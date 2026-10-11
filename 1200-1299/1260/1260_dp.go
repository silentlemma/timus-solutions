package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	// rows of the ages 1..k starting with 1: a(k) = a(k-1) + a(k-3) + 1,
	// with a(1) = 1 and the rule run back to a(0) = 0, a(-1) = -1
	older, old, cur := int64(-1), int64(0), int64(1)
	for i := 1; i < n; i++ {
		older, old, cur = old, cur, cur+older+1
	}
	fmt.Println(cur)
}
