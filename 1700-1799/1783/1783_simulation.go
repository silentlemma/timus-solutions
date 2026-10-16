package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

// ceilDiv is the smallest whole x with x * t >= need, also for a negative
// need
func ceilDiv(need, t int64) int64 {
	if need >= 0 {
		return (need + t - 1) / t
	}
	return -(-need / t)
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var n, m int
	if _, err := fmt.Fscan(reader, &n, &m); err != nil {
		return
	}
	plan := make([]int64, n+m-1)
	for i := range plan {
		fmt.Fscan(reader, &plan[i])
	}
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	var stock int64
	for i := 0; i < n; i++ {
		// after t months of the same change x the stock is stock + t x,
		// which must reach the plan of that month
		x := int64(math.MinInt64)
		for t := 1; t <= m; t++ {
			if c := ceilDiv(plan[i+t-1]-stock, int64(t)); c > x {
				x = c
			}
		}
		if i > 0 {
			writer.WriteByte(' ')
		}
		writer.WriteString(fmt.Sprint(x))
		stock += x
	}
	writer.WriteByte('\n')
}
