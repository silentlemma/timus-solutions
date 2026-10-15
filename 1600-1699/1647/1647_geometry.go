package main

import (
	"fmt"
	"math"
)

const (
	corners = 3
	rounds  = 200 // bisection steps, far beyond double precision
)

type point struct{ x, y float64 }

type mark struct {
	at float64
	p  point
}

func shoelace(poly []point) float64 {
	twice := 0.0
	for i := range poly {
		a, b := poly[(i+len(poly)-1)%len(poly)], poly[i]
		twice += a.x*b.y - b.x*a.y
	}
	return math.Abs(twice) / 2
}

func main() {
	var pts [corners]point
	for i := range pts {
		if _, err := fmt.Scan(&pts[i].x, &pts[i].y); err != nil {
			return
		}
	}
	var sides [corners]float64
	perimeter := 0.0
	for i := range pts {
		a, b := pts[i], pts[(i+1)%corners]
		sides[i] = math.Hypot(b.x-a.x, b.y-a.y)
		perimeter += sides[i]
	}
	var marks []mark // arc positions of the corners, twice round
	pos := 0.0
	for lap := 0; lap < 2; lap++ {
		for i := range pts {
			marks = append(marks, mark{pos, pts[i]})
			pos += sides[i]
		}
	}
	// at gives the coast point at arc length s from the first corner
	at := func(s float64) point {
		s = math.Mod(s, perimeter)
		for i := 0; i < corners; i++ {
			if s <= sides[i] || i == corners-1 {
				t := math.Min(s/sides[i], 1)
				a, b := pts[i], pts[(i+1)%corners]
				return point{a.x + (b.x-a.x)*t, a.y + (b.y-a.y)*t}
			}
			s -= sides[i]
		}
		return pts[0]
	}
	// area cut off by the coast from s to t (s < t) and the chord
	area := func(s, t float64) float64 {
		poly := []point{at(s)}
		for _, m := range marks {
			if s < m.at && m.at < t {
				poly = append(poly, m.p)
			}
		}
		return shoelace(append(poly, at(t)))
	}
	half, total := perimeter/2, shoelace(pts[:])
	excess := func(s float64) float64 { return area(s, s+half) - total/2 }
	// the excess changes sign over half a turn, as the other part is the
	// complement, so a chord splitting both evenly always exists
	lo, hi := 0.0, half
	low := excess(lo) > 0
	for r := 0; r < rounds; r++ {
		mid := (lo + hi) / 2
		if (excess(mid) > 0) == low {
			lo = mid
		} else {
			hi = mid
		}
	}
	s := (lo + hi) / 2
	a, b := at(s), at(s+half)
	fmt.Printf("YES\n%.12f %.12f\n%.12f %.12f\n", a.x, a.y, b.x, b.y)
}
