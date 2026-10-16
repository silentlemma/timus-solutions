package main

import (
	"fmt"
	"math"
)

const eps = 1e-9

type point struct{ x, y float64 }

func cross(a, b point) float64 { return a.x*b.y - a.y*b.x }

// chord is where the refracted line of sight enters the planet and where
// it would leave it again
func chord(r, eta, x, y, dx, dy float64) (point, point) {
	// the first crossing of the line of sight with the circle
	a, halfB, c := dx*dx+dy*dy, x*dx+y*dy, x*x+y*y-r*r
	t := (-halfB - math.Sqrt(math.Max(0, halfB*halfB-a*c))) / a
	enter := point{x + dx*t, y + dy*t}
	length := math.Hypot(dx, dy)
	ux, uy := dx/length, dy/length
	// split the direction into the inward normal and the tangent; Snell's
	// law shrinks the tangent part by eta
	nx, ny := -enter.x/r, -enter.y/r
	along := ux*nx + uy*ny
	tx, ty := (ux-along*nx)/eta, (uy-along*ny)/eta
	inward := math.Sqrt(math.Max(0, 1-tx*tx-ty*ty))
	vx, vy := inward*nx+tx, inward*ny+ty
	// the chord from the entry point along v has length -2 (e . v)
	span := -2 * (enter.x*vx + enter.y*vy)
	return enter, point{enter.x + vx*span, enter.y + vy*span}
}

func main() {
	var r, eta, ax, ay, adx, ady, bx, by, bdx, bdy float64
	if _, err := fmt.Scan(&r, &eta, &ax, &ay, &adx, &ady, &bx, &by, &bdx, &bdy); err != nil {
		return
	}
	p1, q1 := chord(r, eta, ax, ay, adx, ady)
	p2, q2 := chord(r, eta, bx, by, bdx, bdy)
	d1 := point{q1.x - p1.x, q1.y - p1.y}
	d2 := point{q2.x - p2.x, q2.y - p2.y}
	w := point{p2.x - p1.x, p2.y - p1.y}
	den := cross(d1, d2)
	var seen bool
	if math.Abs(den) < eps {
		// parallel chords meet only if they lie on one line
		seen = math.Abs(cross(w, d1)) < eps*math.Max(1, math.Hypot(d1.x, d1.y))
	} else {
		s, t := cross(w, d2)/den, cross(w, d1)/den
		seen = eps < s && s < 1-eps && eps < t && t < 1-eps
	}
	if seen {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
