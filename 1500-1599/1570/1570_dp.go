package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const (
	scale      = 1000 // satiety has at most three digits after the point
	mostDishes = 128  // more than the number of different dishes
	none       = int64(1) << 62
	digits     = 3
)

func thousandths(text string) int {
	whole, part := text, ""
	if i := strings.IndexByte(text, '.'); i >= 0 {
		whole, part = text[:i], text[i+1:]
	}
	w, _ := strconv.Atoi(whole)
	p, _ := strconv.Atoi((part + "000")[:digits])
	return w*scale + p
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, m int
	fmt.Fscan(in, &n, &m)
	names := make([]string, n)
	price, fill := make([]int, n), make([]int, n)
	for i := 0; i < n; i++ {
		var f string
		fmt.Fscan(in, &names[i], &price[i], &f)
		fill[i] = thousandths(f)
	}
	top := m * scale
	// best[s]: the least cost, then the most different dishes, of an order with
	// satiety s, where s = top stands for top or more; one number holds both,
	// cost * mostDishes - dishes, so that smaller is better
	best, mine := make([]int64, top+1), make([]int64, top+1)
	for s := range best {
		best[s] = none
	}
	best[0] = 0
	// per dish: whether the best order at s takes it, and in the orders
	// that take it, the satiety before the last plate and if that plate was the
	// first one, which leaves the orders without the dish
	took, first := make([][]bool, n), make([][]bool, n)
	back := make([][]int32, n)
	for i := 0; i < n; i++ {
		took[i], first[i], back[i] = make([]bool, top+1), make([]bool, top+1), make([]int32, top+1)
		step := int64(price[i]) * mostDishes
		for s := range mine {
			mine[s] = none
		}
		for s := 0; s <= top; s++ {
			t := s + fill[i]
			if t > top {
				t = top
			}
			if best[s] < none && best[s]+step-1 < mine[t] {
				mine[t], back[i][t], first[i][t] = best[s]+step-1, int32(s), true
			}
		}
		// more plates of the same dish, from lower satiety up
		for s := 0; s < top; s++ {
			t := s + fill[i]
			if t > top {
				t = top
			}
			if mine[s] < none && mine[s]+step < mine[t] {
				mine[t], back[i][t], first[i][t] = mine[s]+step, int32(s), false
			}
		}
		for s := 0; s <= top; s++ {
			if mine[s] < best[s] {
				best[s], took[i][s] = mine[s], true
			}
		}
	}
	// walk back from the full order, dish by dish from the last one
	plates := make([]int, n)
	s := top
	for i := n - 1; i >= 0; i-- {
		if !took[i][s] {
			continue
		}
		for done := false; !done; {
			plates[i]++
			done = first[i][s]
			s = int(back[i][s])
		}
	}
	cost := 0
	for i := range plates {
		cost += price[i] * plates[i]
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	fmt.Fprintln(out, cost)
	for i := range plates {
		if plates[i] > 0 {
			fmt.Fprintln(out, names[i], plates[i])
		}
	}
}
