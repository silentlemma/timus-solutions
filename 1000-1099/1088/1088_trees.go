package main

import "fmt"

func main() {
	var d, e, f, dp, ep, h int64
	fmt.Scan(&d, &e, &f, &dp, &ep, &h)
	// pier p - 1 written in F bits is the path to it, a left turn being 1 and
	// the first turn the highest bit; a stone k hours from the sea is that
	// path without its last k turns
	a, depthA := (ep-1)>>uint(e), f-e
	b, depthB := (dp-1)>>uint(d), f-d
	var hours int64
	for ; depthA > depthB; depthA, hours = depthA-1, hours+1 {
		a >>= 1
	}
	for ; depthB > depthA; depthB, hours = depthB-1, hours+1 {
		b >>= 1
	}
	for ; a != b; hours += 2 {
		a, b = a>>1, b>>1
	}
	if hours <= h {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}
}
