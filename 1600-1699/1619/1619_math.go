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
	var t int
	if _, err := fmt.Fscan(in, &t); err != nil {
		return
	}
	for ; t > 0; t-- {
		var k, m int
		fmt.Fscan(in, &k, &m)
		// the ballot theorem: the elder stays ahead or level with this chance
		if m > k {
			fmt.Fprintln(out, "0")
		} else {
			fmt.Fprintf(out, "%.10f\n", float64(k-m+1)/float64(k+1))
		}
	}
}
