package main

import (
	"bufio"
	"fmt"
	"os"
)

// the disks start on the source rod and go to the target rod
const (
	source = 1
	target = 2
	spare  = 3
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	rod := make([]int, n+1)
	for i := 1; i <= n; i++ {
		fmt.Fscan(in, &rod[i])
	}
	// disks 1..k are being moved from a to b over c; disk k moves once, in the
	// middle: before it the others go to c, after it they go from c to b
	a, b, c := source, target, spare
	var steps int64
	for k := n; k >= 1; k-- {
		if rod[k] == a {
			b, c = c, b
		} else if rod[k] == b {
			steps += 1 << uint(k-1)
			a, c = c, a
		} else {
			steps = -1
			break
		}
	}
	fmt.Println(steps)
}
