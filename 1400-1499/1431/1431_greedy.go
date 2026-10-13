package main

import "fmt"

const top = 30

func main() {
	var n int
	fmt.Scan(&n)
	count := make([]int, top+2)
	for i := 0; i < n; i++ {
		var c int
		fmt.Scan(&c)
		count[c]++
	}
	// two types share a symmetric alternating row only as ABA...BA, counts differing by one,
	// along the chain of counts, pairing the leftovers of c with c + 1 at once is best
	pairs, left := 0, 0
	for c := 1; c <= top; c++ {
		matched := left
		if count[c] < matched {
			matched = count[c]
		}
		pairs += matched
		left = count[c] - matched
	}
	fmt.Println(n - pairs)
}
