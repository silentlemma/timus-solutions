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
	fmt.Fscan(in, &n)
	total := n + 2
	x, y := make([]int64, total), make([]int64, total)
	for i := 0; i < total; i++ {
		fmt.Fscan(in, &x[i], &y[i])
	}
	// always run to the farthest point not visited yet: the point before had
	// this one as its farthest, so it was at least as far as the next one,
	// which makes every turn acute
	seen := make([]bool, total)
	at := 0
	seen[0] = true
	out.WriteString("YES\n1")
	for step := 1; step < total; step++ {
		far, best := -1, int64(-1)
		for j := 0; j < total; j++ {
			dx, dy := x[j]-x[at], y[j]-y[at]
			if d := dx*dx + dy*dy; !seen[j] && d > best {
				far, best = j, d
			}
		}
		seen[far] = true
		at = far
		out.WriteString(" " + strconv.Itoa(far+1))
	}
	out.WriteString("\n")
}
