package main

import (
	"bufio"
	"fmt"
	"math/bits"
	"os"
	"sort"
	"strings"
)

var (
	n      int
	cover  []uint32
	failed = map[uint32]int{}
	drops  []int
)

// pick at most budget cities covering the set left, appending to drops
func search(left uint32, budget int) bool {
	if left == 0 {
		return true
	}
	if f, ok := failed[left]; budget == 0 || (ok && f >= budget) {
		return false
	}
	gain := make([]int, n)
	best := 0
	for v := 0; v < n; v++ {
		gain[v] = bits.OnesCount32(cover[v] & left)
		if gain[v] > best {
			best = gain[v]
		}
	}
	if bits.OnesCount32(left) > budget*best {
		failed[left] = budget
		return false
	}
	// the uncovered city with the fewest cities able to hit it
	u := -1
	for v := 0; v < n; v++ {
		if left>>uint(v)&1 == 1 && (u < 0 || bits.OnesCount32(cover[v]) < bits.OnesCount32(cover[u])) {
			u = v
		}
	}
	var options []int
	for v := 0; v < n; v++ {
		if cover[u]>>uint(v)&1 == 1 {
			options = append(options, v)
		}
	}
	sort.SliceStable(options, func(a, b int) bool { return gain[options[a]] > gain[options[b]] })
	var tried []uint32
	for _, v := range options {
		hit := cover[v] & left
		// skip a drop that hits only part of what a tried one hits
		dominated := false
		for _, t := range tried {
			if hit&^t == 0 {
				dominated = true
			}
		}
		if dominated {
			continue
		}
		tried = append(tried, hit)
		drops = append(drops, v)
		if search(left&^hit, budget-1) {
			return true
		}
		drops = drops[:len(drops)-1]
	}
	failed[left] = budget
	return false
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var r int
	if _, err := fmt.Fscan(in, &n, &r); err != nil {
		return
	}
	x, y := make([]int, n), make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(in, &x[i], &y[i])
	}
	// cover[i]: the cities a bottle dropped on city i destroys
	cover = make([]uint32, n)
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			dx, dy := x[i]-x[j], y[i]-y[j]
			if dx*dx+dy*dy <= r*r {
				cover[i] |= 1 << uint(j)
			}
		}
	}
	everything := uint32(1)<<uint(n) - 1
	budget := 1
	for !search(everything, budget) {
		budget++
	}
	parts := make([]string, len(drops))
	for i, v := range drops {
		parts[i] = fmt.Sprint(v + 1)
	}
	fmt.Println(len(drops))
	fmt.Println(strings.Join(parts, " "))
}
