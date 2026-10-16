package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var n, m, a, b, r, s int
	if _, err := fmt.Fscan(reader, &n, &m, &a, &b, &r, &s); err != nil {
		return
	}
	// bus i takes the fans after the border P(i-1) up to the border P(i),
	// with P(0) = 0, P(m) = n and a <= P(i) - P(i-1) <= b; a fan in bus f
	// puts P(f) at or above them and P(f-1) below them
	lo, hi := make([]int, m+1), make([]int, m+1)
	for i := range hi {
		hi[i] = n
	}
	hi[0], lo[m] = 0, n
	for i := 0; i < s; i++ {
		var fan, bus int
		fmt.Fscan(reader, &fan, &bus)
		lo[bus] = max(lo[bus], fan)
		hi[bus-1] = min(hi[bus-1], fan-1)
	}
	// the borders reachable from the left end and from the right end each
	// form a range, and a border is possible when it is in both
	for i := 1; i <= m; i++ {
		lo[i] = max(lo[i], lo[i-1]+a)
		hi[i] = min(hi[i], hi[i-1]+b)
	}
	for i := m - 1; i >= 0; i-- {
		lo[i] = max(lo[i], lo[i+1]-b)
		hi[i] = min(hi[i], hi[i+1]-a)
	}
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	for i := 0; i <= m; i++ {
		if lo[i] > hi[i] {
			fmt.Fprintln(writer, "IMPOSSIBLE")
			return
		}
	}
	// fan r rides in bus k when some P(k-1) below r and P(k) at or above r
	// are possible borders a to b apart
	var buses []int
	for k := 1; k <= m; k++ {
		xLo, xHi := lo[k-1], min(hi[k-1], r-1)
		yLo, yHi := max(lo[k], r), hi[k]
		if xLo <= xHi && yLo <= yHi && yHi-xLo >= a && yLo-xHi <= b {
			buses = append(buses, k)
		}
	}
	fmt.Fprintln(writer, len(buses))
	for i, k := range buses {
		if i > 0 {
			writer.WriteByte(' ')
		}
		writer.WriteString(strconv.Itoa(k))
	}
	writer.WriteByte('\n')
}
