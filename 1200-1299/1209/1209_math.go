package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

const square = 8

// isSquare tells whether v is a perfect square, correcting the floating root.
func isSquare(v int64) bool {
	r := int64(math.Sqrt(float64(v)))
	for r*r > v {
		r--
	}
	for (r+1)*(r+1) <= v {
		r++
	}
	return r*r == v
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var n int
	fmt.Fscan(in, &n)
	for i := 0; i < n; i++ {
		var k int64
		fmt.Fscan(in, &k)
		if i > 0 {
			out.WriteByte(' ')
		}
		// the ones stand at 1 + m(m - 1) / 2, that is where 8(k - 1) + 1 is a
		// perfect square
		if isSquare(square*(k-1) + 1) {
			out.WriteByte('1')
		} else {
			out.WriteByte('0')
		}
	}
	out.WriteByte('\n')
}
