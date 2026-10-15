package main

import (
	"fmt"
	"math"
)

const (
	eps    = 1e-9
	sides  = 4
	points = sides + 1
)

var (
	px, py    [points]float64 // the mouse, then the corners of the book
	cx, cy, r float64
)

// positive inside the book (the corners go counterclockwise)
func side(i int, x, y float64) float64 {
	a, b := 1+i, 1+(i+1)%sides
	return (px[b]-px[a])*(y-py[a]) - (py[b]-py[a])*(x-px[a])
}

func outside(x, y float64) bool {
	for i := 0; i < sides; i++ {
		if side(i, x, y) < -eps {
			return true
		}
	}
	return false
}

// whether the segment passes through the inside of the book
func blocks(ax, ay, bx, by float64) bool {
	lo, hi := 0.0, 1.0
	for i := 0; i < sides; i++ {
		f0, f1 := side(i, ax, ay), side(i, bx, by)
		if f0 <= eps && f1 <= eps {
			return false
		}
		if f0 < f1 && f0 <= eps {
			lo = math.Max(lo, (eps-f0)/(f1-f0))
		}
		if f1 < f0 && f1 <= eps {
			hi = math.Min(hi, (f0-eps)/(f0-f1))
		}
	}
	return hi-lo > eps
}

// the closest point of the disk outside the book that (sx, sy) sees
func nearest(sx, sy float64) float64 {
	best := math.Inf(1)
	if d := math.Hypot(sx-cx, sy-cy); d > eps {
		qx, qy := cx+(sx-cx)*r/d, cy+(sy-cy)*r/d
		if outside(qx, qy) && !blocks(sx, sy, qx, qy) {
			best = math.Max(0, d-r)
		}
	}
	for i := 0; i < sides; i++ {
		if side(i, sx, sy) > eps {
			continue
		}
		// the part of side i inside the disk, as a parameter range on it
		a, b := 1+i, 1+(i+1)%sides
		ex, ey := px[b]-px[a], py[b]-py[a]
		qa := ex*ex + ey*ey
		qb := (px[a]-cx)*ex + (py[a]-cy)*ey
		qc := (px[a]-cx)*(px[a]-cx) + (py[a]-cy)*(py[a]-cy) - r*r
		disc := qb*qb - qa*qc
		if disc <= 0 {
			continue
		}
		lo := math.Max(0, (-qb-math.Sqrt(disc))/qa)
		hi := math.Min(1, (-qb+math.Sqrt(disc))/qa)
		if (hi-lo)*math.Sqrt(qa) <= eps {
			continue
		}
		t := ((sx-px[a])*ex + (sy-py[a])*ey) / qa
		t = math.Min(math.Max(t, lo), hi)
		best = math.Min(best, math.Hypot(px[a]+t*ex-sx, py[a]+t*ey-sy))
	}
	return best
}

func main() {
	for i := 1; i < points; i++ {
		fmt.Scan(&px[i], &py[i])
	}
	fmt.Scan(&cx, &cy, &r, &px[0], &py[0])
	// the mouse goes straight or around corners of the book; Dijkstra over
	// the mouse and the corners gives each its shortest way from the start
	var dist [points]float64
	var done [points]bool
	for i := range dist {
		dist[i] = math.Inf(1)
	}
	dist[0] = 0
	for step := 0; step < points; step++ {
		u := -1
		for w := 0; w < points; w++ {
			if !done[w] && (u < 0 || dist[w] < dist[u]) {
				u = w
			}
		}
		done[u] = true
		for w := 1; w < points; w++ {
			gap := (u - w + sides) % sides
			joined := gap == 1 || gap == sides-1
			if u == 0 {
				joined = !blocks(px[0], py[0], px[w], py[w])
			}
			if w != u && joined {
				dist[w] = math.Min(dist[w], dist[u]+math.Hypot(px[w]-px[u], py[w]-py[u]))
			}
		}
	}
	answer := math.Inf(1)
	for k := 0; k < points; k++ {
		answer = math.Min(answer, dist[k]+nearest(px[k], py[k]))
	}
	fmt.Printf("%.5f\n", answer)
}
