package main

import (
	"bufio"
	"fmt"
	"os"
)

const inf = int64(1) << 62

func abs(x int64) int64 {
	if x < 0 {
		return -x
	}
	return x
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	pos := make([]int64, n)
	for i := 1; i < n; i++ {
		fmt.Fscan(in, &pos[i])
		pos[i] += pos[i-1]
	}
	var start int
	var period, firstUp, firstDown int64
	fmt.Fscan(in, &start, &period, &firstUp, &firstDown)
	start--
	if n == 1 {
		fmt.Println(0)
		return
	}
	// trains run forever: towards N they pass station i at firstUp + pos[i]
	// plus multiples of the period, towards 1 at firstDown + pos[N] - pos[i]
	var phase [2][]int64
	for d := range phase {
		phase[d] = make([]int64, n)
	}
	for i := 0; i < n; i++ {
		phase[0][i] = (firstUp + pos[i]) % period
		phase[1][i] = (firstDown + pos[n-1] - pos[i]) % period
	}
	// the first train in direction d at station j not before time t
	next := func(d, j int, t int64) int64 {
		return t + ((phase[d][j]-t)%period+period)%period
	}
	full := 1<<uint(n) - 1
	arrive := make([]int64, (full+1)*n)
	best := inf
	for d0 := 0; d0 < 2; d0++ {
		t0 := phase[d0][start]
		// arrive[mask*n+j]: earliest time standing at j with mask inspected
		for i := range arrive {
			arrive[i] = inf
		}
		for k := 0; k < n; k++ {
			if (d0 == 0 && k > start) || (d0 == 1 && k < start) {
				arrive[(1<<uint(start)|1<<uint(k))*n+k] = t0 + abs(pos[k]-pos[start])
			}
		}
		for mask := 0; mask < full; mask++ {
			if mask>>uint(start)&1 == 0 {
				continue
			}
			for j := 0; j < n; j++ {
				t := arrive[mask*n+j]
				if t == inf {
					continue
				}
				for d := 0; d < 2; d++ {
					dep := next(d, j, t+1)
					for k := 0; k < n; k++ {
						if (d == 0 && k <= j) || (d == 1 && k >= j) || mask>>uint(k)&1 == 1 {
							continue
						}
						at := (mask|1<<uint(k))*n + k
						if a := dep + abs(pos[k]-pos[j]); a < arrive[at] {
							arrive[at] = a
						}
					}
				}
			}
		}
		// with everything inspected, ride straight back to the start
		for j := 0; j < n; j++ {
			if t := arrive[full*n+j]; t != inf && j != start {
				d := 1
				if start > j {
					d = 0
				}
				if total := next(d, j, t+1) + abs(pos[start]-pos[j]) - t0; total < best {
					best = total
				}
			}
		}
	}
	fmt.Println(best)
}
