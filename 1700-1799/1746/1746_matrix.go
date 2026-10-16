package main

import (
	"bufio"
	"fmt"
	"os"
)

func multiply(a, b [][]int64, mod int64) [][]int64 {
	n := len(a)
	c := make([][]int64, n)
	for i := range c {
		c[i] = make([]int64, n)
		for k := 0; k < n; k++ {
			if a[i][k] == 0 {
				continue
			}
			for j := 0; j < n; j++ {
				c[i][j] = (c[i][j] + a[i][k]*b[k][j]) % mod
			}
		}
	}
	return c
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var n, m, d, mod int64
	var q int
	fmt.Fscan(in, &n, &m, &d, &mod, &q)
	points := make([][]int64, q)
	for i := range points {
		points[i] = make([]int64, n)
		for k := range points[i] {
			fmt.Fscan(in, &points[i][k])
		}
	}
	// the number of routes depends only on how many coordinates differ
	// from the target: a move fixes one of them, changes one of them to
	// another wrong value, or spoils one that was right
	size := int(n) + 1
	step := make([][]int64, size)
	power := make([][]int64, size)
	for h := 0; h < size; h++ {
		step[h] = make([]int64, size)
		power[h] = make([]int64, size)
		power[h][h] = 1 % mod
		hh := int64(h)
		if h > 0 {
			step[h][h-1] = hh % mod
			step[h][h] = hh * (m - 2) % mod
		}
		if h < size-1 {
			step[h][h+1] = (n - hh) * (m - 1) % mod
		}
	}
	for ; d > 0; d >>= 1 {
		if d&1 == 1 {
			power = multiply(power, step, mod)
		}
		step = multiply(step, step, mod)
	}
	for i := range points {
		for j := range points {
			differ := 0
			for k := range points[i] {
				if points[i][k] != points[j][k] {
					differ++
				}
			}
			if j > 0 {
				fmt.Fprint(out, " ")
			}
			fmt.Fprint(out, power[differ][0])
		}
		fmt.Fprintln(out)
	}
}
