package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const inf = 1 << 30

func main() {
	in := bufio.NewScanner(os.Stdin)
	in.Split(bufio.ScanWords)
	// next returns the next number, skipping the "*" lines between blocks
	next := func() int {
		in.Scan()
		for in.Text() == "*" {
			in.Scan()
		}
		v, _ := strconv.Atoi(in.Text())
		return v
	}
	levels := next()
	// the cheapest cost of reaching each planet of the current level
	cost := []int{0}
	for level := 0; level < levels; level++ {
		k := next()
		nxt := make([]int, k)
		for planet := range nxt {
			nxt[planet] = inf
			for src := next(); src != 0; src = next() {
				price := next()
				if cost[src-1] < inf && cost[src-1]+price < nxt[planet] {
					nxt[planet] = cost[src-1] + price
				}
			}
		}
		cost = nxt
	}
	best := inf
	for _, c := range cost {
		if c < best {
			best = c
		}
	}
	fmt.Println(best)
}
