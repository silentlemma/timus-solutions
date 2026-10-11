package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	// a row ends in white or red; it comes from a row one shorter ending in
	// the other of the two, or from one two shorter followed by blue
	prev, cur := int64(2), int64(2)
	for i := 2; i < n; i++ {
		prev, cur = cur, prev+cur
	}
	fmt.Println(cur)
}
