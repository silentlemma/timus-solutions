package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
)

const (
	box  = 2 // the starting cell is a square of half-side box * R around the disk
	span = 4 // a site cuts a cell only within twice its reach: squared, 4 times
	eps  = 1e-9
)

type pt struct{ x, y float64 }

// clip keeps the part of the convex polygon with (p - m) . d <= 0.
func clip(poly []pt, m, d pt) []pt {
	var out []pt
	n := len(poly)
	for k := 0; k < n; k++ {
		p, q := poly[k], poly[(k+1)%n]
		sp := (p.x-m.x)*d.x + (p.y-m.y)*d.y
		sq := (q.x-m.x)*d.x + (q.y-m.y)*d.y
		if sp <= 0 {
			out = append(out, p)
		}
		if (sp < 0 && sq > 0) || (sq < 0 && sp > 0) {
			t := sp / (sp - sq)
			out = append(out, pt{p.x + t*(q.x-p.x), p.y + t*(q.y-p.y)})
		}
	}
	return out
}

// inside tells whether a lies in the convex polygon, counterclockwise.
func inside(poly []pt, a pt) bool {
	n := len(poly)
	for k := 0; k < n; k++ {
		p, q := poly[k], poly[(k+1)%n]
		if (q.x-p.x)*(a.y-p.y)-(q.y-p.y)*(a.x-p.x) < -eps {
			return false
		}
	}
	return true
}

// farthest gives the largest distance from c to a point of the polygon
// inside the disk of radius r around the origin.
func farthest(poly []pt, c pt, r float64) float64 {
	best := 0.0
	n := len(poly)
	for k := 0; k < n; k++ {
		p, q := poly[k], poly[(k+1)%n]
		if p.x*p.x+p.y*p.y <= r*r {
			best = math.Max(best, math.Hypot(p.x-c.x, p.y-c.y))
		}
		// where the edge crosses the circle: |p + t (q - p)| = r
		ux, uy := q.x-p.x, q.y-p.y
		a, b, cc := ux*ux+uy*uy, p.x*ux+p.y*uy, p.x*p.x+p.y*p.y-r*r
		disc := b*b - a*cc
		if a > 0 && disc >= 0 {
			for _, t := range []float64{(-b - math.Sqrt(disc)) / a, (-b + math.Sqrt(disc)) / a} {
				if t >= 0 && t <= 1 {
					best = math.Max(best, math.Hypot(p.x+t*ux-c.x, p.y+t*uy-c.y))
				}
			}
		}
	}
	// on an arc inside the cell the distance peaks at the circle point
	// opposite the site, if that point is in the cell
	o := pt{r, 0}
	if norm := math.Hypot(c.x, c.y); norm > 0 {
		o = pt{-r * c.x / norm, -r * c.y / norm}
	}
	if inside(poly, o) {
		best = math.Max(best, math.Hypot(o.x-c.x, o.y-c.y))
	}
	return best
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	var r float64
	fmt.Fscan(in, &n, &r)
	sites := make([]pt, n)
	for i := range sites {
		fmt.Fscan(in, &sites[i].x, &sites[i].y)
	}
	sq := func(a, b pt) float64 { return (a.x-b.x)*(a.x-b.x) + (a.y-b.y)*(a.y-b.y) }
	side, answer := box*r, 0.0
	for _, c := range sites {
		poly := []pt{{-side, -side}, {side, -side}, {side, side}, {-side, side}}
		order := make([]int, n)
		for j := range order {
			order[j] = j
		}
		sort.Slice(order, func(a, b int) bool { return sq(sites[order[a]], c) < sq(sites[order[b]], c) })
		for _, j := range order {
			d := sq(sites[j], c)
			if d == 0 {
				continue // the site itself, or another one at the same point
			}
			reach := 0.0
			for _, v := range poly {
				reach = math.Max(reach, sq(v, c))
			}
			if d > span*reach {
				break
			}
			o := sites[j]
			poly = clip(poly, pt{(o.x + c.x) / 2, (o.y + c.y) / 2}, pt{o.x - c.x, o.y - c.y})
		}
		answer = math.Max(answer, farthest(poly, c, r))
	}
	fmt.Printf("%.8f\n", answer)
}
