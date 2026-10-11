package main

import (
	"bufio"
	"os"
	"strconv"
)

const fixed = 153 // 1 + 125 + 27: every multiple of 3 ends here

func cubes(x int64) int64 {
	s := int64(0)
	for ; x > 0; x /= 10 {
		d := x % 10
		s += d * d * d
	}
	return s
}

func main() {
	in := bufio.NewScanner(os.Stdin)
	in.Split(bufio.ScanWords)
	next := func() int64 {
		in.Scan()
		x, _ := strconv.Atoi(in.Text())
		return int64(x)
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	t := next()
	for i := int64(0); i < t; i++ {
		n, k, l := next(), next(), next()
		// the gap before base N is F applied N - 1 times to K; from a
		// multiple of 3 it reaches 153 within 14 steps and stays there
		gap := k
		for step := int64(0); step < n-1 && gap != fixed; step++ {
			gap = cubes(gap)
		}
		out.WriteString(strconv.FormatInt(gap-l, 10) + "\n")
	}
}
