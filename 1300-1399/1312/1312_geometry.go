package main

import (
	"fmt"
	"math"
	"strings"
)

const (
	eps    = 1e-9 // relative to the size of the tray
	plates = 3
)

type point struct{ x, y float64 }

var (
	h, w, tol float64
	radii     [plates]float64
	order     [plates]int
	pos       [plates]point
)

func fits(p point, r float64) bool {
	return p.x >= r-tol && p.x <= h-r+tol && p.y >= r-tol && p.y <= w-r+tol
}

// touching gives the centres of a circle touching circles (a, ra) and
// (b, rb) from outside, with ra and rb already increased by its radius
func touching(a point, ra float64, b point, rb float64) []point {
	dx, dy := b.x-a.x, b.y-a.y
	d2 := dx*dx + dy*dy
	if d2 == 0 {
		return nil
	}
	d := math.Sqrt(d2)
	x := (d2 + ra*ra - rb*rb) / (2 * d)
	h2 := (ra - x) * (ra + x)
	if h2 < 0 {
		return nil
	}
	hh := math.Sqrt(h2)
	mx, my := a.x+dx*x/d, a.y+dy*x/d
	return []point{{mx - dy*hh/d, my + dx*hh/d}, {mx + dy*hh/d, my - dx*hh/d}}
}

func place(k int) bool {
	if k == plates {
		return true
	}
	r := radii[order[k]]
	xs, ys := []float64{r, h - r}, []float64{r, w - r}
	var cand []point
	for _, x := range xs {
		for _, y := range ys {
			cand = append(cand, point{x, y}) // the four corners
		}
	}
	for i := 0; i < k; i++ {
		q := pos[order[i]]
		s := radii[order[i]] + r
		for _, x := range xs { // against a side wall and a placed plate
			if t := s*s - (x-q.x)*(x-q.x); t >= 0 {
				cand = append(cand, point{x, q.y - math.Sqrt(t)}, point{x, q.y + math.Sqrt(t)})
			}
		}
		for _, y := range ys {
			if t := s*s - (y-q.y)*(y-q.y); t >= 0 {
				cand = append(cand, point{q.x - math.Sqrt(t), y}, point{q.x + math.Sqrt(t), y})
			}
		}
		for j := 0; j < i; j++ { // against two placed plates
			cand = append(cand, touching(q, s, pos[order[j]], radii[order[j]]+r)...)
		}
	}
	for _, p := range cand {
		if !fits(p, r) {
			continue
		}
		ok := true
		for i := 0; i < k && ok; i++ {
			q := pos[order[i]]
			ok = math.Hypot(p.x-q.x, p.y-q.y) >= r+radii[order[i]]-tol
		}
		if !ok {
			continue
		}
		pos[order[k]] = p
		if place(k + 1) {
			return true
		}
	}
	return false
}

// permute tries every order of the plates, as in Heap's algorithm
func permute(n int) bool {
	if n == 1 {
		return place(0)
	}
	for i := 0; i < n; i++ {
		if permute(n - 1) {
			return true
		}
		if n%2 == 0 {
			order[i], order[n-1] = order[n-1], order[i]
		} else {
			order[0], order[n-1] = order[n-1], order[0]
		}
	}
	return false
}

func main() {
	fmt.Scan(&h, &w, &radii[0], &radii[1], &radii[2])
	tol = eps * (h + w)
	// pushing every plate down and to the left as far as it goes leaves each
	// one held by two walls or plates placed before it, so some order of the
	// plates and some choice of two such supports finds a placement
	for i := range order {
		order[i] = i
	}
	if !permute(plates) {
		fmt.Println(0)
		return
	}
	parts := make([]string, plates)
	for i, p := range pos {
		parts[i] = fmt.Sprintf("%.4f %.4f", p.x, p.y)
	}
	fmt.Println(strings.Join(parts, " "))
}
