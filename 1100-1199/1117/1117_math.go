package main

import (
	"fmt"
	"math/bits"
)

// evens is the sum over even e <= n of tz(e) - 1, that is sum over y <= n/2 of tz(y)
func evens(n int64) int64 {
	m := n / 2
	return m - int64(bits.OnesCount64(uint64(m)))
}

// extra is tz(x) - 1 for an even x and 0 for an odd one
func extra(x int64) int64 {
	if x%2 != 0 {
		return 0
	}
	return int64(bits.TrailingZeros64(uint64(x))) - 1
}

func main() {
	var i, j int64
	fmt.Scan(&i, &j)
	if i > j {
		i, j = j, i
	}
	// numbers run through the tree in order, so a node's height is the count of
	// trailing zeros; between k and k + 1 the even one is an ancestor of the
	// odd leaf, and the message waits one day per node in between
	days := int64(0)
	if i < j {
		days = 2*(evens(j)-evens(i-1)) - extra(i) - extra(j)
	}
	fmt.Println(days)
}
