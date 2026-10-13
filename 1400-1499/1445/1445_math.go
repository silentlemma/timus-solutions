package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	biggest, total := 0, 0
	for i := 0; i < n; i++ {
		var size int
		fmt.Scan(&size)
		if size > biggest {
			biggest = size
		}
		total += size
	}
	// the biggest company needs gifts from outside it: prepared or from the others
	best := 2*biggest - total
	if best < 1 {
		best = 1
	}
	// in the worst order the biggest company comes first, and that many always suffice
	fmt.Println(best, biggest)
}
