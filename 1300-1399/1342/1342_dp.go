package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, m int
	fmt.Fscan(in, &n, &m)
	k, first, last := make([]int, n), make([]int, n), make([]int, n)
	total := 0
	for i := 0; i < n; i++ {
		fmt.Fscan(in, &k[i], &first[i], &last[i])
		total += k[i]
	}
	target := m
	if total < target {
		target = total
	}
	// best[j]: the cheapest way to make exactly j brooms at the factories so far
	best := make([]float64, target+1)
	for j := 1; j <= target; j++ {
		best[j] = math.Inf(1)
	}
	fresh := make([]float64, target+1)
	reach := 0
	for i := 0; i < n; i++ {
		step := 0.0
		if k[i] > 1 {
			step = float64(last[i]-first[i]) / float64(k[i]-1)
		}
		// cost[x]: x brooms at this factory, the j-th one costing first + step (j - 1)
		cost := make([]float64, k[i]+1)
		for x := range cost {
			fx := float64(x)
			cost[x] = fx*float64(first[i]) + step*fx*(fx-1)/2
		}
		reach += k[i]
		if reach > target {
			reach = target
		}
		copy(fresh, best)
		for j := 1; j <= reach; j++ {
			here := fresh[j]
			for x := 1; x <= j && x <= k[i]; x++ {
				if v := best[j-x] + cost[x]; v < here {
					here = v
				}
			}
			fresh[j] = here
		}
		best, fresh = fresh, best
	}
	if target < m {
		fmt.Printf("Maximum possible amount: %d\n", target)
	}
	fmt.Printf("Minimum possible cost: %.2f\n", best[target])
}
