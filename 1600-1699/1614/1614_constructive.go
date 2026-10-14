package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var n int
	if _, err := fmt.Fscan(in, &n); err != nil {
		return
	}
	stops := 2 * n
	for k := 0; k < n; k++ {
		// k, k + 1, k - 1, k + 2, k - 2, ..., k + n around the circle of stops:
		// its neighbouring pairs are exactly those with sum 2k or 2k + 1
		fmt.Fprint(out, k+1)
		for j := 1; j <= n; j++ {
			fmt.Fprint(out, " ", (k+j)%stops+1)
			if j < n {
				fmt.Fprint(out, " ", (k-j+stops)%stops+1)
			}
		}
		fmt.Fprintln(out)
	}
}
