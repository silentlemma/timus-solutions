package main

import (
	"bufio"
	"fmt"
	"os"
)

// east, south, west, north: turning right moves one step along this list
var steps = [][2]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}

func main() {
	var n, m, rt, ct, rl, cl, t int
	fmt.Scan(&n, &m, &rt, &ct, &rl, &cl, &t)
	// dig the spiral up to the treasure, remembering the order of the graves,
	// with a frame of dug cells around the cemetery standing for the wall
	seen := make([][]bool, n+2)
	for r := range seen {
		seen[r] = make([]bool, m+2)
		seen[r][0], seen[r][m+1] = true, true
	}
	for c := 0; c < m+2; c++ {
		seen[0][c], seen[n+1][c] = true, true
	}
	path := [][2]int{{1, 1}}
	seen[1][1] = true
	r, c, d := 1, 1, 0
	for r != rt || c != ct {
		nr, nc := r+steps[d][0], c+steps[d][1]
		if seen[nr][nc] {
			d = (d + 1) % len(steps)
			continue
		}
		r, c = nr, nc
		seen[r][c] = true
		path = append(path, [2]int{r, c})
	}
	// Lara runs along the tunnel, at most t graves either way
	here := 0
	for path[here] != [2]int{rl, cl} {
		here++
	}
	lo, hi := here-t, here+t
	if lo < 0 {
		lo = 0
	}
	if hi > len(path)-1 {
		hi = len(path) - 1
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for i := lo; i <= hi; i++ {
		fmt.Fprintln(out, path[i][0], path[i][1])
	}
}
