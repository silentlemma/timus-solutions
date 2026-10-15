package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var n int
	fmt.Scan(&n)
	// every two flags need a common color, and a color on at most two flags
	// serves one pair only, so k(k - 1) / 2 <= n; one color per pair is enough
	k := 1
	for (k+1)*k/2 <= n {
		k++
	}
	flags := make([][]int, k)
	color := 0
	for a := 0; a < k; a++ {
		for b := a + 1; b < k; b++ {
			color++
			flags[a] = append(flags[a], color)
			flags[b] = append(flags[b], color)
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	fmt.Fprintln(out, k)
	for _, flag := range flags {
		fmt.Fprint(out, len(flag))
		for _, c := range flag {
			fmt.Fprint(out, " ", c)
		}
		fmt.Fprintln(out)
	}
}
