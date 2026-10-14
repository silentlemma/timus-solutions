package main

import (
	"bufio"
	"fmt"
	"os"
)

const need = 2 // a run needs two generating intervals inside it to be split

// a rectangle by its top-left and bottom-right pixels, counted from 1
type rect struct{ x1, y1, x2, y2 int }

// smallestFamily: g[l][r] means columns l .. r-1 are a union of chosen
// intervals inside them. Going right, an interval two smaller chosen ones
// cover is dropped and those it leaned on move right: the smallest family.
func smallestFamily(g [][]bool, width int) {
	for right := 1; right <= width; right++ {
		for {
			count := make([]int, width+1)
			covered, rest := 0, 0 // chosen intervals inside [t, u), those starting before t
			u, t := right, right-1
			redundant := true
			for u > t {
				covered -= count[u]
				for left := 0; left < u; left++ {
					if !g[left][u] {
						continue
					}
					count[left]++
					if left >= t {
						covered++
					} else {
						rest++
					}
				}
				if covered+rest < need {
					redundant = false
					break
				}
				for covered < need {
					t--
					covered += count[t]
					rest -= count[t]
				}
				u--
			}
			if !redundant {
				break
			}
			w := u
			for !g[w][right] {
				w++
			}
			g[w][right] = false
			for end := right - 1; w > u; end-- {
				x := u
				for x < w && !g[x][end] {
					x++
				}
				if x == w {
					continue
				}
				g[x][end] = false
				g[w][end] = true
				w = x
			}
		}
	}
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var n, m int
	fmt.Fscan(in, &n, &m)
	// the black pixels of a column form one run from top to bottom
	top, bottom := make([]int, m), make([]int, m)
	for c := range top {
		top[c], bottom[c] = n, -1
	}
	g := make([][]bool, m+1)
	for i := range g {
		g[i] = make([]bool, m+1)
	}
	for row := 0; row < n; row++ {
		var line string
		fmt.Fscan(in, &line)
		for col := 0; col < m; {
			if line[col] == '0' {
				col++
				continue
			}
			left := col
			for col < m && line[col] == '1' {
				if row < top[col] {
					top[col] = row
				}
				if row > bottom[col] {
					bottom[col] = row
				}
				col++
			}
			g[left][col] = true
		}
	}
	smallestFamily(g, m)
	// a chosen interval of columns spans every row where all of them are black
	var rects []rect
	for lo := 0; lo < m; lo++ {
		for hi := lo + 1; hi <= m; hi++ {
			if !g[lo][hi] {
				continue
			}
			first, last := 0, n-1
			for c := lo; c < hi; c++ {
				if top[c] > first {
					first = top[c]
				}
				if bottom[c] < last {
					last = bottom[c]
				}
			}
			rects = append(rects, rect{first + 1, lo + 1, last + 1, hi})
		}
	}
	fmt.Fprintln(out, len(rects))
	for _, r := range rects {
		fmt.Fprintln(out, r.x1, r.y1, r.x2, r.y2)
	}
}
