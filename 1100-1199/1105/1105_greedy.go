package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

const (
	shifts = 3
	eps    = 1e-9
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var t0, t1 float64
	var n int
	fmt.Fscan(in, &t0, &t1, &n)
	lo := make([]float64, n)
	hi := make([]float64, n)
	for i := range lo {
		fmt.Fscan(in, &lo[i], &hi[i])
	}
	// greedy cover: each step takes the observer reaching furthest among those
	// already present, so only neighbouring observers of the chain overlap
	order := make([]int, n)
	for i := range order {
		order[i] = i
	}
	sort.Slice(order, func(a, b int) bool { return lo[order[a]] < lo[order[b]] })
	var chain []int
	cur, i := t0, 0
	for cur < t1 && i < n {
		best := -1
		for ; i < n && lo[order[i]] <= cur; i++ {
			if best < 0 || hi[order[i]] > hi[best] {
				best = order[i]
			}
		}
		if best < 0 || hi[best] <= cur {
			if i < n {
				cur = lo[order[i]]
			} else {
				cur = t1
			}
			continue
		}
		chain = append(chain, best)
		cur = hi[best]
	}
	// dropping every third observer of the chain leaves each piece of time
	// alone in two of the three shifts, so the best shift keeps 2/3 of it
	m := len(chain)
	bestShift, bestAlone := 0, -1.0
	for shift := 0; shift < shifts; shift++ {
		alone := 0.0
		for k := 0; k < m; k++ {
			if k%shifts == shift {
				continue
			}
			alone += hi[chain[k]] - lo[chain[k]]
			if k+1 < m && (k+1)%shifts != shift && hi[chain[k]] > lo[chain[k+1]] {
				alone -= 2 * (hi[chain[k]] - lo[chain[k+1]])
			}
		}
		if alone > bestAlone {
			bestShift, bestAlone = shift, alone
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	if bestAlone < (t1-t0)*2/shifts-eps {
		out.WriteString("0\n")
		return
	}
	var painted []int
	for k := 0; k < m; k++ {
		if k%shifts != bestShift {
			painted = append(painted, chain[k]+1)
		}
	}
	out.WriteString(strconv.Itoa(len(painted)) + "\n")
	for _, p := range painted {
		out.WriteString(strconv.Itoa(p) + "\n")
	}
}
