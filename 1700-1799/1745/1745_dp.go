package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

type word struct {
	change, low, size, id int
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	// each word: net change of the depth, lowest depth reached, length
	var rising, falling []word
	top := 0
	for i := 0; i < n; i++ {
		var w string
		fmt.Fscan(in, &w)
		depth, low := 0, 0
		for _, c := range w {
			if c == '(' {
				depth++
			} else {
				depth--
			}
			if depth < low {
				low = depth
			}
		}
		top += len(w)
		if depth >= 0 {
			rising = append(rising, word{depth, low, len(w), i + 1})
		} else {
			falling = append(falling, word{depth, low, len(w), i + 1})
		}
	}
	// in a best answer the words that open more than they close come first,
	// those that dip least first; the rest go last, those that end highest
	// above their lowest point first
	sort.SliceStable(rising, func(a, b int) bool { return rising[a].low > rising[b].low })
	sort.SliceStable(falling, func(a, b int) bool {
		return falling[a].low-falling[a].change < falling[b].low-falling[b].change
	})
	order := append(rising, falling...)
	// best[d]: longest prefix built so far that ends at depth d
	best := make([]int, top+1)
	next := make([]int, top+1)
	for d := range best {
		best[d] = -1
	}
	best[0] = 0
	taken := make([][]bool, len(order))
	for k, w := range order {
		copy(next, best)
		taken[k] = make([]bool, top+1)
		for d := 0; d <= top; d++ {
			if best[d] < 0 || d+w.low < 0 {
				continue
			}
			if e := d + w.change; best[d]+w.size > next[e] {
				next[e] = best[d] + w.size
				taken[k][e] = true
			}
		}
		best, next = next, best
	}
	var used []string
	for k, d := len(order)-1, 0; k >= 0; k-- {
		if taken[k][d] {
			used = append(used, strconv.Itoa(order[k].id))
			d -= order[k].change
		}
	}
	for i, j := 0, len(used)-1; i < j; i, j = i+1, j-1 {
		used[i], used[j] = used[j], used[i]
	}
	fmt.Println(best[0], len(used))
	fmt.Println(strings.Join(used, " "))
}
