package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

const jury = 255

type plot struct{ w, s, x, y int }

func main() {
	in := bufio.NewReader(os.Stdin)
	var size, park, m int
	fmt.Fscan(in, &size, &park, &m)
	plots := make([]plot, m)
	for i := range plots {
		fmt.Fscan(in, &plots[i].w, &plots[i].s, &plots[i].x, &plots[i].y)
	}
	top := size - park + 1
	// sliding the park left only drops plots until its left side reaches a
	// plot's right side or the border, so only those positions are tried
	xset, yset := map[int]bool{1: true}, map[int]bool{1: true}
	for _, p := range plots {
		if p.x+p.s <= top {
			xset[p.x+p.s] = true
		}
		if p.y+p.s <= top {
			yset[p.y+p.s] = true
		}
	}
	keys := func(set map[int]bool) []int {
		var out []int
		for v := range set {
			out = append(out, v)
		}
		sort.Ints(out)
		return out
	}
	best := jury
	for _, px := range keys(xset) {
		for _, py := range keys(yset) {
			worst := 1
			for _, p := range plots {
				if px < p.x+p.s && p.x < px+park && py < p.y+p.s && p.y < py+park && p.w > worst {
					worst = p.w
				}
			}
			if worst < best {
				best = worst
			}
		}
	}
	if best == jury {
		fmt.Println("IMPOSSIBLE")
	} else {
		fmt.Println(best)
	}
}
