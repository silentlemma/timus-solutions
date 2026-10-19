package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

const endless = int64(1) << 62

type sip struct {
	from, to int64
	layer    int
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var n int
	fmt.Fscan(in, &n)
	times := make([]int64, n)
	words := make([]string, n)
	values := make([]int64, n)
	seen := map[string]bool{}
	var names []string
	for i := 0; i < n; i++ {
		fmt.Fscan(in, &times[i], &words[i])
		if words[i] != "fire" {
			fmt.Fscan(in, &values[i])
		}
		if words[i] != "fire" && words[i] != "Oleg" && !seen[words[i]] {
			seen[words[i]] = true
			names = append(names, words[i])
		}
	}
	sort.Strings(names)
	index := map[string]int{}
	for i, s := range names {
		index[s] = i
	}
	m := len(names)
	// layers in order of names (the densest at the bottom), with a Fenwick tree of heights
	tree := make([]int64, m+1)
	height := make([]int64, m)
	top := 1
	for top*2 <= m {
		top *= 2
	}
	add := func(i int, delta int64) {
		height[i] += delta
		for i++; i <= m; i += i & -i {
			tree[i] += delta
		}
	}
	// the layer that contains level h, and how much of it lies above h
	layerAt := func(h int64) (int, int64) {
		pos := 0
		for step := top; step > 0; step >>= 1 {
			if pos+step <= m && tree[pos+step] <= h {
				pos += step
				h -= tree[pos]
			}
		}
		return pos, height[pos] - h
	}
	var total, straw, clock int64
	drinking := false
	var sips []sip // neighbours of one liqueur merged
	drink := func(amount int64) {
		for amount > 0 && total > straw {
			layer, above := layerAt(straw)
			take := above
			if amount < take {
				take = amount
			}
			add(layer, -take)
			total -= take
			amount -= take
			if k := len(sips) - 1; k >= 0 && sips[k].layer == layer && sips[k].to == clock {
				sips[k].to = clock + take
			} else {
				sips = append(sips, sip{clock, clock + take, layer})
			}
			clock += take
		}
	}
	for i := 0; i < n; i++ {
		if drinking {
			drink(times[i] - clock)
			// running dry before this moment stops him; running dry exactly now does not
			// matter: a pour lets him go on, and Oleg or fire set the state anyway
			drinking = clock == times[i]
		}
		clock = times[i]
		switch words[i] {
		case "Oleg":
			straw = values[i]
			drinking = true
		case "fire":
			drinking = false
		default:
			add(index[words[i]], values[i])
			total += values[i]
		}
	}
	if drinking {
		drink(endless)
	}
	var b strings.Builder
	for _, s := range sips {
		b.WriteString(strconv.FormatInt(s.from, 10) + "-" + strconv.FormatInt(s.to, 10) + " ")
		b.WriteString(names[s.layer] + "\n")
	}
	out.WriteString(b.String())
}
