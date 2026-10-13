package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

const shear = 20001 // x' = shear x + y keeps all points apart and no segment vertical

type pt struct{ x, y int64 }

func sign(v int64) int {
	if v > 0 {
		return 1
	}
	if v < 0 {
		return -1
	}
	return 0
}

func orient(a, b, c pt) int { return sign((b.x-a.x)*(c.y-a.y) - (b.y-a.y)*(c.x-a.x)) }

func min64(a, b int64) int64 {
	if a < b {
		return a
	}
	return b
}

func max64(a, b int64) int64 {
	if a > b {
		return a
	}
	return b
}

func onBox(a, b, c pt) bool {
	return min64(a.x, b.x) <= c.x && c.x <= max64(a.x, b.x) &&
		min64(a.y, b.y) <= c.y && c.y <= max64(a.y, b.y)
}

// closed segments pq and rs share a point
func touch(p, q, r, s pt) bool {
	o1, o2, o3, o4 := orient(p, q, r), orient(p, q, s), orient(r, s, p), orient(r, s, q)
	if o1*o2 < 0 && o3*o4 < 0 {
		return true
	}
	return (o1 == 0 && onBox(p, q, r)) || (o2 == 0 && onBox(p, q, s)) ||
		(o3 == 0 && onBox(r, s, p)) || (o4 == 0 && onBox(r, s, q))
}

var from, to, lo, hi []pt

// the sign of the height of segment i above point p, at the x of p
func side(i int, p pt) int {
	a, b := lo[i], hi[i]
	return sign(a.y*(b.x-a.x) + (b.y-a.y)*(p.x-a.x) - p.y*(b.x-a.x))
}

func slopeLess(i, j int) bool {
	return (hi[i].y-lo[i].y)*(hi[j].x-lo[j].x) < (hi[j].y-lo[j].y)*(hi[i].x-lo[i].x)
}

type event struct {
	x          int64
	kind, item int // starts come before ends
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(reader, &n)
	from, to, lo, hi = make([]pt, n), make([]pt, n), make([]pt, n), make([]pt, n)
	events := make([]event, 0, 2*n)
	for i := 0; i < n; i++ {
		fmt.Fscan(reader, &from[i].x, &from[i].y, &to[i].x, &to[i].y)
		a := pt{shear*from[i].x + from[i].y, from[i].y}
		b := pt{shear*to[i].x + to[i].y, to[i].y}
		if b.x < a.x {
			a, b = b, a
		}
		lo[i], hi[i] = a, b
		events = append(events, event{a.x, 0, i}, event{b.x, 1, i})
	}
	// Shamos-Hoey: sweep a vertical line over the sheared plane, keep the
	// segments it crosses ordered by height, and test only neighbours
	sort.Slice(events, func(a, b int) bool {
		if events[a].x != events[b].x {
			return events[a].x < events[b].x
		}
		if events[a].kind != events[b].kind {
			return events[a].kind < events[b].kind
		}
		return events[a].item < events[b].item
	})
	meet := func(i, j int) {
		if touch(from[i], to[i], from[j], to[j]) {
			fmt.Printf("YES\n%d %d\n", i+1, j+1)
			os.Exit(0)
		}
	}
	var line []int
	for _, ev := range events {
		i := ev.item
		if ev.kind == 0 {
			p := lo[i]
			l, h := 0, len(line)
			for l < h {
				mid := (l + h) / 2
				c := side(line[mid], p)
				if c < 0 || (c == 0 && slopeLess(line[mid], i)) {
					l = mid + 1
				} else {
					h = mid
				}
			}
			line = append(line, 0)
			copy(line[l+1:], line[l:])
			line[l] = i
			if l > 0 {
				meet(i, line[l-1])
			}
			if l+1 < len(line) {
				meet(i, line[l+1])
			}
		} else {
			p := hi[i]
			l, h := 0, len(line)
			for l < h {
				mid := (l + h) / 2
				if side(line[mid], p) < 0 {
					l = mid + 1
				} else {
					h = mid
				}
			}
			k := l
			for k < len(line) && line[k] != i {
				k++
			}
			if k == len(line) {
				for k = 0; line[k] != i; k++ {
				}
			}
			line = append(line[:k], line[k+1:]...)
			if k > 0 && k < len(line) {
				meet(line[k-1], line[k])
			}
		}
	}
	fmt.Println("NO")
}
