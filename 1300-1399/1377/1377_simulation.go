package main

import "fmt"

// east, south, west, north: turning right moves one step along this list
var steps = [][2]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}

func main() {
	var n, m, r1, c1, r2, c2 int
	fmt.Scan(&n, &m, &r1, &c1, &r2, &c2)
	// dig the whole spiral, numbering the graves by the night they are dug,
	// with a frame of dug cells around the cemetery standing for the wall
	night := make([][]int, n+2)
	for r := range night {
		night[r] = make([]int, m+2)
		for c := range night[r] {
			if r == 0 || r == n+1 || c == 0 || c == m+1 {
				night[r][c] = 0
			} else {
				night[r][c] = -1
			}
		}
	}
	r, c, d := 1, 1, 0
	night[1][1] = 1
	for day := 2; day <= n*m; day++ {
		for night[r+steps[d][0]][c+steps[d][1]] >= 0 {
			d = (d + 1) % len(steps)
		}
		r, c = r+steps[d][0], c+steps[d][1]
		night[r][c] = day
	}
	gap := night[r1][c1] - night[r2][c2]
	if gap < 0 {
		gap = -gap
	}
	fmt.Println(gap)
}
