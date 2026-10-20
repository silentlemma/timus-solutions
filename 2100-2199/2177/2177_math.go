package main

import (
	"bufio"
	"fmt"
	"os"
)

const minSum int64 = 3

func longestChain(first, second int64) int64 {
	if first > second {
		first, second = second, first
	}
	difference := second - first
	if difference == 0 {
		return 2
	}
	if difference == 1 {
		return second - 1
	}
	if difference == 2 {
		if second%2 == 1 {
			return second - 1
		}
		return second / 2
	}
	// A longest chain joins two distinct residue classes modulo the difference.
	return 2 * ((second-minSum)/difference + 1)
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var first, second int64
	fmt.Fscan(in, &first, &second)
	fmt.Println(longestChain(first, second))
}
