package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var n int
	fmt.Scan(&n)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	fmt.Fprintln(writer, n*n+n/2+1)
	// a chessboard: the large numbers go down on one colour and the small
	// ones up on the other, both in reading order
	big, small := n*n, 1
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if j > 0 {
				writer.WriteByte(' ')
			}
			if (i+j)%2 == 0 {
				fmt.Fprint(writer, big)
				big--
			} else {
				fmt.Fprint(writer, small)
				small++
			}
		}
		writer.WriteByte('\n')
	}
}
