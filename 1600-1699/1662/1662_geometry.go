package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

const eps = 1e-7

type pt struct{ x, y float64 }

// edge keeps a start, a direction, the outward unit normal and its offset.
type edge struct{ ax, ay, ex, ey, nx, ny, c float64 }

// circles gives the common points of two circles.
func circles(a pt, ra float64, b pt, rb float64, out []pt) []pt {
	dx, dy := b.x-a.x, b.y-a.y
	d2 := dx*dx + dy*dy
	if d2 == 0 {
		return out
	}
	along := (d2 + ra*ra - rb*rb) / (2 * d2)
	h2 := ra*ra/d2 - along*along
	if h2 < -eps {
		return out
	}
	h := math.Sqrt(math.Max(0, h2))
	x, y := a.x+dx*along, a.y+dy*along
	return append(out, pt{x - dy*h, y + dx*h}, pt{x + dy*h, y - dx*h})
}

// lineCircle gives the common points of the line nx*x + ny*y = c (unit
// normal) and a circle.
func lineCircle(nx, ny, c float64, centre pt, radius float64, out []pt) []pt {
	off := nx*centre.x + ny*centre.y - c
	h2 := radius*radius - off*off
	if h2 < -eps {
		return out
	}
	h := math.Sqrt(math.Max(0, h2))
	x, y := centre.x-nx*off, centre.y-ny*off
	return append(out, pt{x - ny*h, y + nx*h}, pt{x + ny*h, y - nx*h})
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	pts := make([]pt, n)
	for i := range pts {
		fmt.Fscan(in, &pts[i].x, &pts[i].y)
	}
	var small, big float64
	fmt.Fscan(in, &small, &big)
	turn := 0.0
	for i := range pts {
		a, b := pts[(i+n-1)%n], pts[i]
		turn += a.x*b.y - b.x*a.y
	}
	side := -1.0
	if turn > 0 {
		side = 1
	}
	edges := make([]edge, n)
	for i := range pts {
		a, b := pts[(i+n-1)%n], pts[i]
		ex, ey := b.x-a.x, b.y-a.y
		length := math.Hypot(ex, ey)
		nx, ny := side*ey/length, -side*ex/length
		edges[i] = edge{a.x, a.y, ex, ey, nx, ny, nx*a.x + ny*a.y}
	}
	reach, keep := (big+eps)*(big+eps), (small-eps)*(small-eps)
	fits := func(p pt) bool {
		for _, v := range pts {
			if (p.x-v.x)*(p.x-v.x)+(p.y-v.y)*(p.y-v.y) > reach {
				return false
			}
		}
		outside := false
		for _, e := range edges {
			if e.nx*p.x+e.ny*p.y > e.c {
				outside = true
			}
			t := ((p.x-e.ax)*e.ex + (p.y-e.ay)*e.ey) / (e.ex*e.ex + e.ey*e.ey)
			t = math.Min(1, math.Max(0, t))
			dx, dy := p.x-e.ax-t*e.ex, p.y-e.ay-t*e.ey
			if dx*dx+dy*dy < keep {
				return false
			}
		}
		return outside
	}
	// the goat's area is where the discs of radius R around the vertices meet,
	// and when any of it is far enough from the bed, so is one of its corners
	// or a crossing of its boundary with the boundary of the bed grown by r
	var found []pt
	for i := range pts {
		for j := range pts {
			found = found[:0]
			if i < j {
				found = circles(pts[i], big, pts[j], big, found)
			}
			found = circles(pts[i], big, pts[j], small, found)
			found = lineCircle(edges[j].nx, edges[j].ny, edges[j].c+small, pts[i], big, found)
			for _, p := range found {
				if fits(p) {
					fmt.Printf("%.6f %.6f\n", p.x, p.y)
					return
				}
			}
		}
	}
	fmt.Println("No solution")
}
