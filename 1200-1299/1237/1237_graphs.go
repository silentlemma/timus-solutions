package main

import (
	"bufio"
	"fmt"
	"os"
)

const inf = 1 << 60

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var n, m int
	fmt.Fscan(in, &n, &m)
	bx, by, bw := make([]int, n), make([]int, n), make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(in, &bx[i], &by[i], &bw[i])
	}
	sx, sy, cap := make([]int, m), make([]int, m), make([]int, m)
	for j := 0; j < m; j++ {
		fmt.Fscan(in, &sx[j], &sy[j], &cap[j])
	}
	plan, dist := make([][]int, n), make([][]int, n)
	load := make([]int, m)
	for i := range plan {
		plan[i], dist[i] = make([]int, m), make([]int, m)
		for j := 0; j < m; j++ {
			fmt.Fscan(in, &plan[i][j])
			load[j] += plan[i][j]
			dist[i][j] = abs(bx[i]-sx[j]) + abs(by[i]-sy[j]) + 1
		}
	}
	// nodes 0..m-1 are shelters and m is the spare room; j -> k moves one
	// worker of some building from shelter j to k, j -> m uses a free place
	// at j, and m -> k lets shelter k end up one worker short
	v := m + 1
	w := make([][]int, v)
	via := make([][]int, v)
	for j := range w {
		w[j], via[j] = make([]int, v), make([]int, v)
		for k := range w[j] {
			w[j][k] = inf
		}
	}
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if plan[i][j] == 0 {
				continue
			}
			for k := 0; k < m; k++ {
				if c := dist[i][k] - dist[i][j]; k != j && c < w[j][k] {
					w[j][k], via[j][k] = c, i
				}
			}
		}
	}
	for j := 0; j < m; j++ {
		if load[j] < cap[j] {
			w[j][m] = 0
		}
		w[m][j] = 0
	}
	// Bellman-Ford from all nodes at once; a change in round v means a
	// negative cycle, which the predecessors lead into
	d, pred := make([]int, v), make([]int, v)
	last := -1
	for round := 0; round < v; round++ {
		last = -1
		for j := 0; j < v; j++ {
			for k := 0; k < v; k++ {
				if w[j][k] < inf && d[j]+w[j][k] < d[k] {
					d[k], pred[k], last = d[j]+w[j][k], j, k
				}
			}
		}
		if last < 0 {
			break
		}
	}
	if last < 0 {
		fmt.Fprintln(out, "OPTIMAL")
		return
	}
	for step := 0; step < v; step++ {
		last = pred[last]
	}
	// shift one worker along each shelter-to-shelter edge of the cycle
	for k := last; ; {
		j := pred[k]
		if j < m && k < m {
			plan[via[j][k]][j]--
			plan[via[j][k]][k]++
		}
		if k = j; k == last {
			break
		}
	}
	fmt.Fprintln(out, "SUBOPTIMAL")
	for i := range plan {
		for j, e := range plan[i] {
			if j > 0 {
				fmt.Fprint(out, " ")
			}
			fmt.Fprint(out, e)
		}
		fmt.Fprintln(out)
	}
}
