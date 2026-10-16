package main

import "fmt"

const sides = 2

func main() {
	var n, k int
	if _, err := fmt.Scan(&n, &k); err != nil {
		return
	}
	// every minute fries at most k of the 2n sides, and one steak takes
	// two minutes on its own; rotating sides cyclically reaches both bounds
	minutes := (sides*n + k - 1) / k
	if minutes < sides {
		minutes = sides
	}
	fmt.Println(minutes)
}
