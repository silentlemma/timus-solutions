package main

import "fmt"

func main() {
	var gap, n int
	fmt.Scan(&gap, &n)
	// at a stop with trams every k minutes the officer, arriving gap
	// minutes after the thief, leaves at best gap - gap % k minutes later,
	// and a gap below k means the thief may still be waiting there
	for i := 0; i < n; i++ {
		var k int
		fmt.Scan(&k)
		gap -= gap % k
		if gap == 0 {
			fmt.Println("YES")
			return
		}
	}
	fmt.Println("NO")
}
