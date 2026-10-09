package main

import "fmt"

const digits = 10

func main() {
	var n int
	fmt.Scan(&n)
	half, limit := n/2, 1
	for i := 0; i < half; i++ {
		limit *= digits
	}
	// ways[s]: how many halves (numbers below 10^half) have digit sum s
	ways := make([]int64, (digits-1)*half+1)
	for x := 0; x < limit; x++ {
		s := 0
		for y := x; y > 0; y /= digits {
			s += y % digits
		}
		ways[s]++
	}
	// the two halves are chosen independently with the same sum
	var total int64
	for _, w := range ways {
		total += w * w
	}
	fmt.Println(total)
}
