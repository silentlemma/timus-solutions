package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var n int
	fmt.Scan(&n)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	// every day uses three pairs and every pair may meet three times, so
	// at most n (n - 1) / 2 days; the triples i, i + d, i + 2d modulo n
	// give each pair three meetings: twice as neighbours, once apart
	fmt.Fprintln(out, n*(n-1)/2)
	for d := 1; d <= (n-1)/2; d++ {
		for i := 0; i < n; i++ {
			fmt.Fprintln(out, i+1, (i+d)%n+1, (i+2*d)%n+1)
		}
	}
}
