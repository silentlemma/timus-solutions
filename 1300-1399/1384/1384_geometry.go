package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

const eps = 1e-9

// line: a x + b y + c, positive inside
type line struct{ a, b, c float64 }

type point struct{ x, y float64 }

// distanceToFence: distance from an inner point to the fence, or -1 outside.
func distanceToFence(pts []point, px, py float64) float64 {
	n := len(pts)
	inside := false
	best := math.Inf(1)
	for i := 0; i < n; i++ {
		p, q := pts[i], pts[(i+1)%n]
		if (p.y > py) != (q.y > py) && px < p.x+(py-p.y)*(q.x-p.x)/(q.y-p.y) {
			inside = !inside
		}
		dx, dy := q.x-p.x, q.y-p.y
		t := math.Max(0, math.Min(1, ((px-p.x)*dx+(py-p.y)*dy)/(dx*dx+dy*dy)))
		best = math.Min(best, math.Hypot(px-p.x-t*dx, py-p.y-t*dy))
	}
	if inside {
		return best
	}
	return -1
}

// onCircle: points o + t u whose distance to v equals base + slope t.
func onCircle(o, u point, base, slope float64, v point, out []point) []point {
	// |o + t u - v|^2 = (base + slope t)^2, or qa t^2 + 2 hb t + qc = 0
	wx, wy := o.x-v.x, o.y-v.y
	qa := u.x*u.x + u.y*u.y - slope*slope
	hb := wx*u.x + wy*u.y - base*slope
	qc := wx*wx + wy*wy - base*base
	disc := hb*hb - qa*qc
	if disc < -eps*(hb*hb+math.Abs(qa*qc)) {
		return out
	}
	// the stable form of the roots, also when qa is next to zero
	q := -(hb + math.Copysign(math.Sqrt(math.Max(0, disc)), hb))
	if math.Abs(qa) > eps {
		out = append(out, point{o.x + q/qa*u.x, o.y + q/qa*u.y})
	}
	if math.Abs(q) > eps {
		out = append(out, point{o.x + qc/q*u.x, o.y + qc/q*u.y})
	}
	return out
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	pts := make([]point, n)
	for i := range pts {
		fmt.Fscan(in, &pts[i].x, &pts[i].y)
	}
	var lines []line
	for i := 0; i < n; i++ {
		p, q := pts[i], pts[(i+1)%n]
		length := math.Hypot(q.x-p.x, q.y-p.y)
		a, b := -(q.y-p.y)/length, (q.x-p.x)/length
		lines = append(lines, line{a, b, -(a*p.x + b*p.y)})
	}
	// only reflex vertices can be the nearest point of the fence from inside
	var reflex []point
	for i := 0; i < n; i++ {
		p, q, r := pts[(i+n-1)%n], pts[i], pts[(i+1)%n]
		if (q.x-p.x)*(r.y-q.y)-(q.y-p.y)*(r.x-q.x) < 0 {
			reflex = append(reflex, q)
		}
	}
	var cand []point
	// three lines: a_i x + b_i y + c_i = r for all three, by Cramer's rule
	for i := range lines {
		for j := i + 1; j < len(lines); j++ {
			for l := j + 1; l < len(lines); l++ {
				p, q, s := lines[i], lines[j], lines[l]
				det := p.a*(q.b-s.b) - p.b*(q.a-s.a) + (q.a*s.b - s.a*q.b)
				if math.Abs(det) < eps {
					continue
				}
				rx := -p.c*(q.b-s.b) - p.b*(s.c-q.c) + (s.c*q.b - q.c*s.b)
				ry := p.a*(s.c-q.c) + p.c*(q.a-s.a) + (s.a*q.c - q.a*s.c)
				cand = append(cand, point{rx / det, ry / det})
			}
		}
	}
	// two lines and a reflex vertex: on the bisector, as far from the vertex
	for i := range lines {
		for j := i + 1; j < len(lines); j++ {
			p, q := lines[i], lines[j]
			da, db, dc := p.a-q.a, p.b-q.b, p.c-q.c
			norm := da*da + db*db
			if norm < eps {
				continue
			}
			o, u := point{-dc * da / norm, -dc * db / norm}, point{-db, da}
			for _, v := range reflex {
				cand = onCircle(o, u, p.a*o.x+p.b*o.y+p.c, p.a*u.x+p.b*u.y, v, cand)
			}
		}
	}
	// a line and two reflex vertices: on their perpendicular bisector
	for i := range reflex {
		for j := i + 1; j < len(reflex); j++ {
			v, w := reflex[i], reflex[j]
			o, u := point{(v.x + w.x) / 2, (v.y + w.y) / 2}, point{-(w.y - v.y), w.x - v.x}
			for _, p := range lines {
				cand = onCircle(o, u, p.a*o.x+p.b*o.y+p.c, p.a*u.x+p.b*u.y, v, cand)
			}
		}
	}
	// three reflex vertices: the centre of their circle
	for i := range reflex {
		for j := i + 1; j < len(reflex); j++ {
			for l := j + 1; l < len(reflex); l++ {
				p, q, r := reflex[i], reflex[j], reflex[l]
				d := 2 * (p.x*(q.y-r.y) + q.x*(r.y-p.y) + r.x*(p.y-q.y))
				if math.Abs(d) < eps {
					continue
				}
				s1, s2, s3 := p.x*p.x+p.y*p.y, q.x*q.x+q.y*q.y, r.x*r.x+r.y*r.y
				cand = append(cand, point{
					(s1*(q.y-r.y) + s2*(r.y-p.y) + s3*(p.y-q.y)) / d,
					(s1*(r.x-q.x) + s2*(p.x-r.x) + s3*(q.x-p.x)) / d,
				})
			}
		}
	}
	best := 0.0
	for _, c := range cand {
		best = math.Max(best, distanceToFence(pts, c.x, c.y))
	}
	fmt.Printf("%.2f\n", best)
}
