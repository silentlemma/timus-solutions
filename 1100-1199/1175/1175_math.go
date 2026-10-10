package main

import "fmt"

type pair struct{ x, y int64 }

var a1, a2, a3, a4, b1, b2, c int64

func step(s pair) pair {
	h := a1*s.x*s.y + a2*s.x + a3*s.y + a4
	if h > b1 && h > b2 && c > 0 {
		h -= (h - b2 + c - 1) / c * c
	}
	return pair{s.y, h}
}

func main() {
	var x1, x2 int64
	fmt.Scan(&a1, &a2, &a3, &a4, &b1, &b2, &c, &x1, &x2)
	// the next term depends only on the last two, so the pairs of
	// neighbouring terms run into a cycle; Brent's method finds it in O(1)
	// memory: the length first, then where it starts
	power, length := int64(1), int64(1)
	slow := pair{x1, x2}
	fast := step(slow)
	for slow != fast {
		if power == length {
			slow, power, length = fast, power*2, 0
		}
		fast = step(fast)
		length++
	}
	slow, fast = pair{x1, x2}, pair{x1, x2}
	for k := int64(0); k < length; k++ {
		fast = step(fast)
	}
	start := int64(1)
	for slow != fast {
		slow, fast = step(slow), step(fast)
		start++
	}
	fmt.Println(start, length)
}
