package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
	"strconv"
	"strings"
)

const none = math.MinInt64 // an unreachable state

type step struct {
	prev int
	up   bool
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var x, n int
	fmt.Fscan(in, &x, &n)
	a, b := make([]int, n), make([]int, n)
	for i := range a {
		fmt.Fscan(in, &a[i])
	}
	for i := range b {
		fmt.Fscan(in, &b[i])
	}
	// utility above x is earned whatever the order; with b capped at x a task
	// done at repaired volume r (debt x - r) earns max(0, min(x, r) - (x - b))
	extra := int64(0)
	need := make([]int, n)
	order := make([]int, n)
	for i := range b {
		if b[i] > x {
			extra += int64(b[i] - x)
		}
		need[i] = x - min(b[i], x)
		order[i] = i
	}
	sort.SliceStable(order, func(i, j int) bool { return a[order[i]] < a[order[j]] })
	// some tasks are given up: they go first and only repair. The rest go by a
	// descending, so task i (ascending a) sees the given up ones before it and
	// every task from it on. best[s]: s = repair of given up tasks so far, capped
	suffix := make([]int, n+1)
	for k := n - 1; k >= 0; k-- {
		suffix[k] = suffix[k+1] + a[order[k]]
	}
	best := make([]int64, x+1)
	for s := range best {
		best[s] = none
	}
	best[0] = 0
	from := make([][]step, n)
	for k, i := range order {
		nxt := make([]int64, x+1)
		for s := range nxt {
			nxt[s] = none
		}
		from[k] = make([]step, x+1)
		for s := 0; s <= x; s++ {
			if best[s] == none {
				continue
			}
			gain := best[s] + int64(min(x, s+suffix[k])-need[i])
			if gain > nxt[s] {
				nxt[s], from[k][s] = gain, step{s, false}
			}
			t := min(x, s+a[i])
			if best[s] > nxt[t] {
				nxt[t], from[k][t] = best[s], step{s, true}
			}
		}
		best = nxt
	}
	s := 0
	for v := range best {
		if best[v] > best[s] {
			s = v
		}
	}
	fmt.Println(best[s] + extra)
	var givenUp, kept []string // kept comes out by a descending
	for k := n - 1; k >= 0; k-- {
		name := strconv.Itoa(order[k] + 1)
		if from[k][s].up {
			givenUp = append(givenUp, name)
		} else {
			kept = append(kept, name)
		}
		s = from[k][s].prev
	}
	fmt.Println(strings.Join(append(givenUp, kept...), " "))
}
