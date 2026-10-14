package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func mod(v, m int64) int64 {
	return (v%m + m) % m
}

func main() {
	var n int64
	if _, err := fmt.Scan(&n); err != nil {
		return
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	used := make(map[int64]bool, n)
	total, length := int64(0), int64(0) // the sum and the number of terms so far
	for m := int64(1); m <= n; m++ {
		// put a large x at position k and then m at k + 1: x must make the
		// sum divisible by k, and x + m divisible by k + 1
		k := length + 1
		a := mod(-total, k)
		b := mod(-total-m, k+1)
		// x = a + k t, and k = -1 modulo k + 1, so t = a - b modulo k + 1
		step := k * (k + 1)
		x := a + k*mod(a-b, k+1)
		if x <= n {
			x += (n-x)/step*step + step
		}
		for used[x] {
			x += step
		}
		used[x] = true
		out.WriteString(strconv.FormatInt(x, 10))
		out.WriteByte(' ')
		out.WriteString(strconv.FormatInt(m, 10))
		if m < n {
			out.WriteByte(' ')
		}
		total += x + m
		length += 2
	}
	out.WriteByte('\n')
}
