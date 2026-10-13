package main

import "fmt"

const pieces = 5

type seg struct{ x, span, level int }

var pw, ph [pieces]int
var used [pieces]bool
var height int

// skyline filling: the lowest, then leftmost, stretch of the outline must
// hold the bottom-left corner of some piece in every tiling
func fill(sky []seg, left int) bool {
	if left == 0 {
		return true
	}
	k := 0
	for i := range sky {
		if sky[i].level < sky[k].level {
			k = i
		}
	}
	s := sky[k]
	tried := map[[2]int]bool{}
	for i := 0; i < pieces; i++ {
		if used[i] {
			continue
		}
		for _, o := range [][2]int{{pw[i], ph[i]}, {ph[i], pw[i]}} {
			w, h := o[0], o[1]
			if tried[o] || w > s.span || s.level+h > height {
				continue
			}
			tried[o] = true
			all := append([]seg{}, sky[:k]...)
			all = append(all, seg{s.x, w, s.level + h})
			if w < s.span {
				all = append(all, seg{s.x + w, s.span - w, s.level})
			}
			all = append(all, sky[k+1:]...)
			var next []seg
			for _, g := range all {
				if len(next) > 0 && next[len(next)-1].level == g.level {
					next[len(next)-1].span += g.span
				} else {
					next = append(next, g)
				}
			}
			used[i] = true
			if fill(next, left-1) {
				return true
			}
			used[i] = false
		}
	}
	return false
}

func main() {
	area := 0
	for i := 0; i < pieces; i++ {
		fmt.Scan(&pw[i], &ph[i])
		area += pw[i] * ph[i]
	}
	for width := 1; width*width <= area; width++ {
		if area%width == 0 {
			height = area / width
			if fill([]seg{{0, width, 0}}, pieces) {
				fmt.Println("YES")
				return
			}
		}
	}
	fmt.Println("NO")
}
