package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

const percent = 100
const outputScale = 100000000

type fraction struct{ num, den int64 }

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	var limit int64
	if _, err := fmt.Fscan(in, &n, &limit); err != nil {
		return
	}
	own := make([]int64, n+1)
	children := make([][]int, n+1)
	for i := 2; i <= n; i++ {
		var parent int
		fmt.Fscan(in, &parent, &own[i])
		children[parent] = append(children[parent], i)
	}
	order := []int{1}
	for i := 0; i < len(order); i++ {
		order = append(order, children[order[i]]...)
	}
	ready := make([]int64, n+1)
	var times []int64
	// x = 100 num/den: a noble with c vassals waits for ceil(num c/den) of
	// them, so the wait is that order statistic of their ready days
	readyBy := func(f fraction) bool {
		for i := len(order) - 1; i >= 0; i-- {
			v := order[i]
			c := int64(len(children[v]))
			need, wait := (f.num*c+f.den-1)/f.den, int64(0)
			if need > 0 {
				times = times[:0]
				for _, w := range children[v] {
					times = append(times, ready[w])
				}
				sort.Slice(times, func(a, b int) bool { return times[a] < times[b] })
				wait = times[need-1]
			}
			ready[v] = wait + own[v]
		}
		return ready[1] <= limit
	}
	// the answer is a largest fraction m/c over the vassal counts c
	seen := make(map[int]bool)
	var fractions []fraction
	for v := 1; v <= n; v++ {
		c := len(children[v])
		if c > 0 && !seen[c] {
			seen[c] = true
			for m := 0; m <= c; m++ {
				fractions = append(fractions, fraction{int64(m), int64(c)})
			}
		}
	}
	if len(fractions) == 0 {
		fractions = append(fractions, fraction{1, 1})
	}
	sort.Slice(fractions, func(a, b int) bool {
		return fractions[a].num*fractions[b].den < fractions[b].num*fractions[a].den
	})
	lo, hi := 0, len(fractions)-1
	for lo < hi {
		mid := (lo + hi + 1) / 2
		if readyBy(fractions[mid]) {
			lo = mid
		} else {
			hi = mid - 1
		}
	}
	answer := (percent*fractions[lo].num*outputScale + fractions[lo].den/2) / fractions[lo].den
	fmt.Printf("%d.%08d\n", answer/outputScale, answer%outputScale)
}
