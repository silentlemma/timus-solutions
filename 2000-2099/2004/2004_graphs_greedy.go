package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func solve(order int) string {
	size := 1 << uint(order)
	mask := size - 1
	seen := make([]bool, size)
	seen[0] = true
	var result strings.Builder
	result.Grow(size + order - 1)
	for i := 0; i < order; i++ {
		result.WriteByte('0')
	}
	window := 0
	for step := 0; step < size-1; step++ {
		window = (window << 1) & mask
		if !seen[window|1] {
			window |= 1
			result.WriteByte('1')
		} else {
			result.WriteByte('0')
		}
		seen[window] = true
	}
	return result.String()
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var order int
	fmt.Fscan(in, &order)
	out := bufio.NewWriter(os.Stdout)
	fmt.Fprintln(out, solve(order))
	out.Flush()
}
