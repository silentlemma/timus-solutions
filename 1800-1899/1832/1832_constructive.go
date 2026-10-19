package main

import "fmt"

func main() {
	var n int
	if _, err := fmt.Scan(&n); err != nil {
		return
	}
	// m, the least number not dividing n, divides no proper divisor either,
	// so colouring by x mod m separates every two artists d apart; m <= 13
	// since lcm(1, ..., 13) exceeds 300000
	m := 2
	for n%m == 0 {
		m++
	}
	p := 2
	for n%p != 0 {
		p++
	}
	// the wrap-around neighbours are n - d apart, at least n - n/p; the
	// last n/p artists get a second palette, so no gap inside either part
	// is that long and the parts never share a colour
	front := n - n/p
	out := make([]byte, n)
	for x := range out {
		out[x] = byte('a' + x%m)
		if x >= front {
			out[x] += byte(m)
		}
	}
	fmt.Println(string(out))
}
