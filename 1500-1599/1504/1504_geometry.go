package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
)

const (
	eps  = 1e-9
	box  = 2 // the starting cell is a square of half-side box * R around the table
	span = 4 // a piece cuts a cell only within twice its reach: squared, 4 times
)

type pt struct{ x, y float64 }

func norm2(p pt) float64 { return p.x*p.x + p.y*p.y }

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

// seat finds a point of the table edge where piece i is the nearest: the
// Voronoi cell of the piece is convex and reaches the edge exactly when its
// farthest vertex from the centre is at least R away.
func seat(pieces []pt, i int, r float64) (pt, bool) {
	c := pieces[i]
	side, limit := box*r, r*r-eps
	poly := []pt{{-side, -side}, {side, -side}, {side, side}, {-side, side}}
	k := len(pieces)
	dist := make([]float64, k)
	order := make([]int, k)
	for j := range pieces {
		dist[j] = norm2(pt{pieces[j].x - c.x, pieces[j].y - c.y})
		order[j] = j
	}
	sort.Slice(order, func(a, b int) bool { return dist[order[a]] < dist[order[b]] })
	for _, j := range order {
		if j == i {
			continue
		}
		reach := 0.0
		for _, v := range poly {
			reach = math.Max(reach, norm2(pt{v.x - c.x, v.y - c.y}))
		}
		if dist[j] > span*reach {
			break // farther than twice the cell's reach: cannot cut it
		}
		o := pieces[j]
		poly = clip(poly, pt{(o.x + c.x) / 2, (o.y + c.y) / 2}, pt{o.x - c.x, o.y - c.y})
		far := 0.0
		for _, v := range poly {
			far = math.Max(far, norm2(v))
		}
		if far < limit {
			return pt{}, false
		}
	}
	v := poly[0]
	for _, w := range poly {
		if norm2(w) > norm2(v) {
			v = w
		}
	}
	// the segment from the piece to that vertex lies in the cell and crosses
	// the edge: solve |c + t (v - c)| = R
	u := pt{v.x - c.x, v.y - c.y}
	a, b, cc := norm2(u), c.x*u.x+c.y*u.y, norm2(c)-r*r
	t := math.Min(1, (-b+math.Sqrt(math.Max(0, b*b-a*cc)))/a)
	p := pt{c.x + t*u.x, c.y + t*u.y}
	l := math.Sqrt(norm2(p))
	return pt{p.x * r / l, p.y * r / l}, true
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var r float64
	var k int
	fmt.Fscan(in, &r, &k)
	pieces := make([]pt, k)
	weight := make([]int, k)
	order := make([]int, k)
	for i := range pieces {
		fmt.Fscan(in, &pieces[i].x, &pieces[i].y, &weight[i])
		order[i] = i
	}
	sort.Slice(order, func(a, b int) bool { return weight[order[a]] > weight[order[b]] })
	for _, i := range order {
		if p, ok := seat(pieces, i, r); ok {
			fmt.Printf("%.10f %.10f\n", p.x, p.y)
			return
		}
	}
}
