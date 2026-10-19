package main

import (
	"bufio"
	"fmt"
	"os"
)

const alice = 1

func main() {
	in := bufio.NewReader(os.Stdin)
	var length, total, va, vb int64
	var n int
	fmt.Fscan(in, &length, &total, &va, &vb, &n)
	// riding in opposite directions, they meet whenever the distance ridden by
	// both together reaches a new multiple of the length; the intervals of one
	// kid do not overlap, so their durations add up
	var resting [2]int64
	for i := 0; i < n; i++ {
		var kid, start, duration int64
		fmt.Fscan(in, &kid, &start, &duration)
		if kid == alice {
			resting[0] += duration
		} else {
			resting[1] += duration
		}
	}
	ridden := va*(total-resting[0]) + vb*(total-resting[1])
	fmt.Println(ridden / length)
}
