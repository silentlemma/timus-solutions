package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	x, y := make([]int64, n+1), make([]int64, n+1)
	cities := make([]int, n)
	for i := 1; i <= n; i++ {
		fmt.Fscan(in, &x[i], &y[i])
		cities[i-1] = i
	}
	sort.Slice(cities, func(i, j int) bool {
		a, b := cities[i], cities[j]
		if x[a] != x[b] {
			return x[a] < x[b]
		}
		return y[a] < y[b]
	})
	// neighbours in (x, y) order: each road lies in its own strip of x, and
	// two roads can share only the border line, where they end at different
	// cities because no three cities are on one line
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for k := 0; k < n; k += 2 {
		fmt.Fprintln(out, cities[k], cities[k+1])
	}
}
