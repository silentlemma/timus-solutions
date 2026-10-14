package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var n int
	var r int64
	fmt.Fscan(in, &n, &r)
	sizes := make([]int64, n)
	for i := range sizes {
		fmt.Fscan(in, &sizes[i])
	}
	// coats whose sizes lie within r of each other need different trips, so
	// the largest number of sizes in a window [x, x + r] is a lower bound
	trips := 0
	for lo, hi := 0, 0; hi < n; hi++ {
		for sizes[hi]-sizes[lo] > r {
			lo++
		}
		if hi-lo+1 > trips {
			trips = hi - lo + 1
		}
	}
	// and it is enough: dealing the sorted coats round, the coat after coat i
	// in a trip is coat i + trips, which lies beyond that window
	fmt.Fprintln(out, trips)
	for t := 0; t < trips; t++ {
		out.WriteString(strconv.Itoa((n - t + trips - 1) / trips))
		for coat := t + 1; coat <= n; coat += trips {
			out.WriteString(" " + strconv.Itoa(coat))
		}
		out.WriteString("\n")
	}
}
