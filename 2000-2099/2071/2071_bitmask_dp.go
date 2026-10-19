package main

import (
	"bufio"
	"fmt"
	"math/bits"
	"os"
	"strconv"
	"strings"
)

const (
	kinds  = 8 // cocktails as masks of three juices; 0 is unused
	inf    = 1 << 30
	juices = "ABP"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var n int
	fmt.Fscan(in, &n)
	var glasses [kinds][]int
	for i := 1; i <= n; i++ {
		var s string
		fmt.Fscan(in, &s)
		mask := 0
		for _, c := range s {
			mask |= 1 << strings.IndexRune(juices, c)
		}
		glasses[mask] = append(glasses[mask], i)
	}
	// equal cocktails stand together; the cocktails present are ordered by a DP over
	// subsets, where best[used][last] counts the pourings, and a juice needs a new pouring
	// when a cocktail contains it and the previous one does not
	present := 0
	for k := 1; k < kinds; k++ {
		if len(glasses[k]) > 0 {
			present |= 1 << k
		}
	}
	var best, from [1 << kinds][kinds]int
	for used := range best {
		for last := range best[used] {
			best[used][last] = inf
		}
	}
	for k := 1; k < kinds; k++ {
		if present>>k&1 == 1 {
			best[1<<k][k] = bits.OnesCount(uint(k))
		}
	}
	for used := 0; used < 1<<kinds; used++ {
		for last := 1; last < kinds; last++ {
			if best[used][last] == inf {
				continue
			}
			for k := 1; k < kinds; k++ {
				if present>>k&1 == 0 || used>>k&1 == 1 {
					continue
				}
				cost := best[used][last] + bits.OnesCount(uint(k&^last))
				next := used | 1<<k
				if cost < best[next][k] {
					best[next][k] = cost
					from[next][k] = last
				}
			}
		}
	}
	last := 1
	for k := 1; k < kinds; k++ {
		if best[present][k] < best[present][last] {
			last = k
		}
	}
	fmt.Fprintln(out, best[present][last])
	var order []int
	for used := present; last != 0; {
		order = append(order, last)
		prev := from[used][last]
		used ^= 1 << last
		last = prev
	}
	parts := make([]string, 0, n)
	for i := len(order) - 1; i >= 0; i-- {
		for _, g := range glasses[order[i]] {
			parts = append(parts, strconv.Itoa(g))
		}
	}
	fmt.Fprintln(out, strings.Join(parts, " "))
}
