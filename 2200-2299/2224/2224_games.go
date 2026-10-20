package main

import (
	"bufio"
	"fmt"
	"os"
)

func blueWins(n int64, r1 int, c1 int64, r2 int, c2 int64) bool {
	// Reflect the board so Blue starts to the left of Red.
	if c1 > c2 {
		c1 = n + 1 - c1
		c2 = n + 1 - c2
	}
	gap := c2 - c1
	left, right := c1-1, n-c2
	if r1 == r2 {
		return left > right || (left == right && gap%2 == 0)
	}
	if gap == 0 || left == right {
		return false
	}
	if gap == 1 {
		return true
	}
	// A one-column tail advantage makes the gap parity decisive.
	if left == right+1 || right == left+1 {
		return gap%2 == 1
	}
	return left > right
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, c1, c2 int64
	var r1, r2 int
	fmt.Fscan(in, &n, &r1, &c1, &r2, &c2)
	if blueWins(n, r1, c1, r2, c2) {
		fmt.Println("Blue")
	} else {
		fmt.Println("Red")
	}
}
