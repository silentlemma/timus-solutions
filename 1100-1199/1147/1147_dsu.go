package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

const (
	// white is the colour of the sheet
	white = 1
	// colours are at most this
	colours = 2500
)

type rect struct{ x1, y1, x2, y2, colour int }

func unique(v []int) []int {
	sort.Ints(v)
	out := v[:0]
	for k, c := range v {
		if k == 0 || c != v[k-1] {
			out = append(out, c)
		}
	}
	return out
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var width, height, n int
	fmt.Fscan(in, &width, &height, &n)
	rects := make([]rect, n)
	xs, ys := []int{0, width}, []int{0, height}
	for k := range rects {
		r := &rects[k]
		fmt.Fscan(in, &r.x1, &r.y1, &r.x2, &r.y2, &r.colour)
		xs = append(xs, r.x1, r.x2)
		ys = append(ys, r.y1, r.y2)
	}
	xs, ys = unique(xs), unique(ys)
	area := make([]int64, colours+1)
	skip := make([]int, len(ys))
	find := func(j int) int {
		for skip[j] != j {
			skip[j] = skip[skip[j]]
			j = skip[j]
		}
		return j
	}
	for i := 0; i+1 < len(xs); i++ {
		strip := int64(xs[i+1] - xs[i])
		// the top rectangles paint the cells of this strip first, and skip[j]
		// leads past painted cells to the next unpainted one
		for j := range skip {
			skip[j] = j
		}
		painted := 0
		for k := n - 1; k >= 0 && painted < height; k-- {
			r := rects[k]
			if r.x1 > xs[i] || r.x2 < xs[i+1] {
				continue
			}
			hi := sort.SearchInts(ys, r.y2)
			got := 0
			for j := find(sort.SearchInts(ys, r.y1)); j < hi; j = find(j + 1) {
				got += ys[j+1] - ys[j]
				skip[j] = j + 1
			}
			area[r.colour] += int64(got) * strip
			painted += got
		}
		area[white] += int64(height-painted) * strip
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for c := 1; c <= colours; c++ {
		if area[c] > 0 {
			fmt.Fprintln(out, c, area[c])
		}
	}
}
