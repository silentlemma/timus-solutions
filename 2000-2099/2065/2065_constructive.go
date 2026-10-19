package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	var n, k int
	fmt.Scan(&n, &k)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	// n - k + 1 zeros, then 1, -1, 2, -2, ...: k distinct values and only k
	// distinct segment sums, the least possible
	for i := 0; i < n-k+1; i++ {
		if i > 0 {
			out.WriteByte(' ')
		}
		out.WriteByte('0')
	}
	for i := 1; i < k; i++ {
		v := (i + 1) / 2
		if i%2 == 0 {
			v = -(i / 2)
		}
		out.WriteString(" " + strconv.Itoa(v))
	}
	out.WriteByte('\n')
}
