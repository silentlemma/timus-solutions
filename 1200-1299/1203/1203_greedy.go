package main

import (
	"bufio"
	"fmt"
	"os"
)

const timeLimit = 30000

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	// the latest start among the talks that end at each minute
	latest := make([]int, timeLimit+1)
	for i := 0; i < n; i++ {
		var s, e int
		fmt.Fscan(in, &s, &e)
		if s > latest[e] {
			latest[e] = s
		}
	}
	// take the talk that ends first among those starting after the last one
	count, last := 0, 0
	for e := 1; e <= timeLimit; e++ {
		if latest[e] > last {
			count++
			last = e
		}
	}
	fmt.Println(count)
}
