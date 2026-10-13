package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	var n, m int
	fmt.Fscan(reader, &n, &m)
	var gone []int // original numbers of destroyed rooms, sorted
	for i := 0; i < m; i++ {
		var letter string
		var x int
		fmt.Fscan(reader, &letter, &x)
		// gone[j] - j <= x holds for a prefix: the rooms gone below room x
		lo, hi := 0, len(gone)
		for lo < hi {
			mid := (lo + hi) / 2
			if gone[mid]-mid <= x {
				lo = mid + 1
			} else {
				hi = mid
			}
		}
		original := x + lo
		if letter == "D" {
			gone = append(gone, 0)
			copy(gone[lo+1:], gone[lo:])
			gone[lo] = original
		} else {
			fmt.Fprintln(writer, original)
		}
	}
}
